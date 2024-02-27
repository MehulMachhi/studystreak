from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
    LessonAttachment,
    LessonAssignment,
    Cupon,
    Live_Class_Type
)
from .serializers import (
    CategoryListSerializers,
    CategoryRetUpdDelSerializers,
    CityListSerializers,
    CityRetUpdDelSerializers,
    CountryListSerializers,
    CountryRetUpdDelSerializers,
    CourseOverviewListSerializers,
    CourseOverviewRetUpdDelSerializers,
    LanguageListSerializers,
    LanguageRetUpdDelSerializers,
    LevelListSerializers,
    LevelRetUpdDelSerializers,
    OutcomesListSerializers,
    OutcomesRetUpdDelSerializers,
    PackageTypeListSerializers,
    PackageTypeRetUpdDelSerializers,
    QuestionTypeSerializers,
    RequirementsListSerializers,
    RequirementsRetUpdDelSerializers,
    SectionListSerializers,
    SEOMetakeywordsListSerializers,
    SEOMetakeywordsRetUpdDelSerializers,
    StateListSerializers,
    StateRetUpdDelSerializers,
    TestTypeSerializers,
    batchListSerializers,
    CountryInterestedListSerializers,
    CourseMaterialListSerializers,
    CourseMaterialRetUpdDelSerializers,
    AdditionalResourceListSerializers,
    LessonAssignmentSerializer,
    LessonAttachmentSerializer,
    CuponListSerializers,
    batchListSerializersCreateBatch,
    Live_Class_Type_List_Serializers,
    SectionRetUpdDelSerializers
)

# Create your views here.


class CategoryListView(generics.ListCreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class CategoryRetUpdDelView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRetUpdDelSerializers


class LevelListView(generics.ListCreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Level.objects.all()
    serializer_class = LevelListSerializers


class LevelRetUpdDelView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelRetUpdDelSerializers


class RequirementsListView(generics.ListCreateAPIView):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsListSerializers


class RequirementsRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsRetUpdDelSerializers


class OutcomesListView(generics.ListCreateAPIView):
    queryset = Outcomes.objects.all()
    serializer_class = OutcomesListSerializers


class OutcomesRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outcomes.objects.all()
    serializer_class = OutcomesRetUpdDelSerializers


class LanguageListView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageListSerializers


class LanguageRetUpdDelView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageRetUpdDelSerializers


class CourseOverviewListView(generics.ListCreateAPIView):
    queryset = CourseOverview.objects.all()
    serializer_class = CourseOverviewListSerializers


class CourseOverviewRetUpdDelView(generics.ListCreateAPIView):
    queryset = CourseOverview.objects.all()
    serializer_class = CourseOverviewRetUpdDelSerializers


class SEOMetakeywordsListView(generics.ListCreateAPIView):
    queryset = SEOMetakeywords.objects.all()
    serializer_class = SEOMetakeywordsListSerializers


class SEOMetakeywordsRetUpdDelView(generics.ListCreateAPIView):
    queryset = SEOMetakeywords.objects.all()
    serializer_class = SEOMetakeywordsRetUpdDelSerializers


class PackageTypeListView(generics.ListCreateAPIView):
    queryset = PackageType.objects.all()
    serializer_class = PackageTypeListSerializers


class PackageTypeRetUpdDelView(generics.ListCreateAPIView):
    queryset = PackageType.objects.all()
    serializer_class = PackageTypeRetUpdDelSerializers


###############################################


class CountryListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializers

class CountryInterestedListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryInterestedListSerializers

class CountryRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryRetUpdDelSerializers


class StateListView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateListSerializers


class StateRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateRetUpdDelSerializers


class CityListView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializers


class CityRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CityRetUpdDelSerializers


class SectionListView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionListSerializers


class SectionRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionRetUpdDelSerializers


"""############################################"""


class batchListView(generics.ListCreateAPIView):
    queryset = batch.objects.all()
    serializer_class = batchListSerializers


class batchRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = batch.objects.all()
    serializer_class = batchListSerializers


class QuestionTypeView(generics.ListCreateAPIView):
    serializer_class = QuestionTypeSerializers
    queryset = QuestionType.objects.all()


class TestTypeViewset(ModelViewSet):
    serializer_class = TestTypeSerializers
    queryset = TestType.objects.all()


# class BatchListByPackageView(generics.ListAPIView):
#     serializer_class = batchListSerializers
#     print("11")

#     def get_queryset(self):
#         # package = self.kwargs['package']
#         # print("00")
#         # return batch.objects.filter(add_package=package)
#         return batch.objects.filter(add_package = self.kwargs["package_id"])
class BatchListByPackageView(generics.ListAPIView):
    serializer_class = batchListSerializers

    def get_queryset(self):
        return batch.objects.filter(add_package=self.kwargs['package_id'])

class CourseMaterialListView(generics.ListAPIView):
    serializer_class = CourseMaterialListSerializers

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return CourseMaterial.objects.filter(course_id=course_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        count = queryset.count()
        return Response({'count': count, 'data': serializer.data})
    
class CourseMaterialRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseMaterial.objects.all()
    serializer_class = CourseMaterialRetUpdDelSerializers


class AdditionalResourceListAPIView(generics.ListAPIView):
    serializer_class = AdditionalResourceListSerializers

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return AdditionalResource.objects.filter(course_id=course_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        count = queryset.count()
        return Response({'count': count, 'data': serializer.data})


class LessonAssignmentListAPIView(generics.ListAPIView):
    serializer_class = LessonAssignmentSerializer

    def get_queryset(self):
        lesson_id = self.kwargs['lesson_id']
        return LessonAssignment.objects.filter(lesson_id=lesson_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        count = queryset.count()
        return Response({'count': count, 'data': serializer.data})

class LessonAttachmentListAPIView(generics.ListAPIView):
    serializer_class = LessonAttachmentSerializer

    def get_queryset(self):
        lesson_id = self.kwargs['lesson_id']
        return LessonAttachment.objects.filter(lesson_id=lesson_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        count = queryset.count()
        return Response({'count': count, 'data': serializer.data})

class CuponListView(generics.ListAPIView):
    queryset = Cupon.objects.all()
    serializer_class = CuponListSerializers


class CreateBatchAPIView(generics.ListCreateAPIView):
    queryset = batch.objects.all()                                        ####createbatchview
    serializer_class = batchListSerializersCreateBatch


class Live_Class_Type_List_View(generics.ListCreateAPIView):
    queryset = Live_Class_Type.objects.all()                                        ####createbatchview
    serializer_class = Live_Class_Type_List_Serializers