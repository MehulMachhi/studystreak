from rest_framework import serializers

from .models import (
    Category,
    City,
    Country,
    CourseOverview,
    Language,
    Level,
    Outcomes,
    PackageType,
    QuestionType,
    Requirements,
    Section,
    SEOMetakeywords,
    State,
    TestType,
    batch,
    CourseMaterial,
    AdditionalResource,
    LessonAssignment,
    LessonAttachment,
    Cupon,
    Live_Class_Type
)

from package.serializers import PackageListSerializers

# from .models import


class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

        depth = 1


class CategoryRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

        depth = 1


class LevelListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class LevelRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"

        # depth = 1


class RequirementsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = "__all__"
        depth = 1


class RequirementsRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = "__all__"
        depth = 1


class OutcomesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Outcomes
        fields = "__all__"


class OutcomesRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Outcomes
        fields = "__all__"


class LanguageListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class LanguageRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class CourseOverviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseOverview
        fields = "__all__"


class CourseOverviewRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseOverview
        fields = "__all__"


class SEOMetakeywordsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SEOMetakeywords
        fields = "__all__"


class SEOMetakeywordsRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = SEOMetakeywords
        fields = "__all__"


class PackageTypeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = "__all__"


class PackageTypeRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = "__all__"


class CountryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CountryRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class CountryInterestedListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class StateListSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"


class StateRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"


class CityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class CityRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class SectionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class SectionRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


###################################################


class batchListSerializers(serializers.ModelSerializer):
    class Meta:
        model = batch
        fields = "__all__"
        depth = 1

class batchListSerializersCreateBatch(serializers.ModelSerializer):
    add_package = PackageListSerializers()
    class Meta:
        model = batch
        fields = "__all__"
        depth = 1

class batchListSerializersCreateBatch(serializers.ModelSerializer):
    # add_package = PackageListSerializers()

    class Meta:
        model = batch
        fields = "__all__"

    # def create(self, validated_data):
    #     add_package_data = validated_data.pop('add_package')
    #     batch_instance = batch.objects.create(**validated_data)

    #     # Assuming 'add_package' is a ForeignKey field in the batch model
    #     package_instance = PackageListSerializers.create(PackageListSerializers(), validated_data=add_package_data)
    #     batch_instance.add_package = package_instance
    #     batch_instance.save()

    #     return batch_instance


class QuestionTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = "__all__"


class TestTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestType
        fields = "__all__"


class CourseMaterialListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = "__all__"


class CourseMaterialRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = "__all__"

class AdditionalResourceListSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdditionalResource
        fields = "__all__"

class LessonAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonAssignment
        fields = '__all__'
        depth=1

class LessonAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonAttachment
        fields = '__all__'
        depth=1

class CuponListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = '__all__'


class Live_Class_Type_List_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Live_Class_Type
        fields = '__all__'
        depth = 1