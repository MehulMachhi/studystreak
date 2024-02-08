from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.sites.shortcuts import get_current_site

############# Login Serializer ############


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email"]


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["username", "password"]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    # is_active = serializers.BooleanField(default=False, write_only=True)
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
            "is_active",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            # "is_active":{"write_only":True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            is_active=False,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(
        max_length=55, style={"input_type": "password"}, write_only=True
    )
    password = serializers.CharField(
        max_length=55,
        style={"input_type": "password"},
        validators=[validate_password],
        write_only=True,
    )
    password2 = serializers.CharField(
        max_length=55, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["current_password", "password", "password2"]

    def validate(self, attrs):
        password = attrs["password"]
        password2 = attrs["password2"]
        user = self.context.get("user")
        success = user.check_password(attrs["current_password"])

        if password == password2 and success:
            user.set_password(password)
            user.save()
            return attrs
        raise serializers.ValidationError("password do not match")


# from studystreak_api import utils
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


class PasswordResetSerializer(serializers.Serializer):
    email_id = serializers.EmailField()

    class Meta:
        fields = ["email_id"]

    def validate(self, attrs):
        email = attrs["email_id"]
        if User.objects.filter(email=email).exists():
            request = self.context.get("request")
            user = User.objects.get(email=email)
            # request = 
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print(uid)
            token = PasswordResetTokenGenerator().make_token(user)
            link = f"http://{get_current_site(request).domain}"
            print(link)
            link = f"{link}/api/user/resetpassword/{uid}/{token}"
            print(link)
            # send email

            context = {"link": link}
            html_message = render_to_string(
                "emails/forgot-password.html", context=context
            )
            plain_message = strip_tags(html_message)

            send_mail(
                subject="Reset Your Password",
                message=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=True,
                html_message=html_message,
            )
            return attrs
        raise serializers.ValidationError("This email is not registered!")


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=55,
        style={"input_type": "password"},
        validators=[validate_password],
        write_only=True,
    )
    password2 = serializers.CharField(
        max_length=55, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        fields = ["password", "password2"]

    def validate(self, attrs):
        password = attrs["password"]
        password2 = attrs["password2"]
        uid = self.context.get("uid")
        token = self.context.get("token")
        print(token)
        id = smart_str(urlsafe_base64_decode(uid))  # type: ignore
        user = User.objects.get(id=id)

        # try:
        #     if not PasswordResetTokenGenerator().check_token(user, token):
        #         raise serializers.ValidationError("Link is expired or already used!")

        #     if password == password2:
        #         user.set_password(password)
        #         user.save()
        #         return attrs
        #     raise serializers.ValidationError("password do not match")

        # except DjangoUnicodeDecodeError as indentifier:
        #     PasswordResetTokenGenerator().check_token(user,token)
        try:
            if PasswordResetTokenGenerator().check_token(user, token):
                print("token is correct")
                if password == password2:
                    user.set_password(password)
                    user.save()
                    print("save done")
                    return attrs
                raise serializers.ValidationError("password do not match")

            raise serializers.ValidationError("Link is expired or already used!")

        except DjangoUnicodeDecodeError:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError("Token is not valid or expired.")


class RedirectLinkSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=55,
        style={"input_type": "password"},
        validators=[validate_password],
        write_only=True,
    )
    password2 = serializers.CharField(
        max_length=55,
        style={"input_type": "password"},
        validators=[validate_password],
        write_only=True,
    )

    class Meta:
        fields = ["password", "password2"]

    def validate(self, attrs):
        password = attrs["password"]
        password2 = attrs["password2"]
        uid = self.context.get("uid")
        token = self.context.get("token")
        id = smart_str(urlsafe_base64_decode(uid))
        user = User.objects.get(id=id)
        print(id)
        print(token)

        try:
            if PasswordResetTokenGenerator().check_token(user, token):
                print("token is correct")
                if password == password2:
                    user.set_password(password)
                    user.save()
                    return attrs
                raise serializers.ValidationError("password do not match")

        except DjangoUnicodeDecodeError:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError("Token is not valid or expired.")

    # class RedirectSerializer(serializers.Serializer):

    #   password = serializers.CharField(max_length=50, style={'input_type':'password'}, validators=[validate_password], write_only=True)
    #   password = serializers.CharField(max_length=50, style={'input_type':'password'}, validators=[validate_password], write_only=True)

    #   class Meta:
    #     fields = ['password', 'password2']

    #   def validate(self, attrs):
    #     password = attrs['password']
    #     password2 = attrs['password2']

    #     uid = self.context.get('uid')
    #     token = self.context.get('token')
    #     id = smart_str(urlsafe_base64_decode(uid))
    #     user = User.objects.get(id=id)

    #     try:
    #       if PasswordResetTokenGenerator.check_token(user, token):
    #         if password == password2:
    #           user.save()
    #           return attrs
    #         raise serializers.ValidationError('')


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "full_name",
        ]

    def get_full_name(self, obj):
        return obj.get_full_name()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name"]
        