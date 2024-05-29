from typing import Optional
import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import ObjectDoesNotExist


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk)
            + six.text_type(timestamp)
            + six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()


def get_user_role(user)-> Optional[None | str]:
    role = None
    try:
        if user.student:
            role = "student"
    except ObjectDoesNotExist:
        pass
        # role = "admin"

    if user.is_superuser:
        role = "admin"

    return role
