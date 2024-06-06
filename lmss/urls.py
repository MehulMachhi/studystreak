from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

# from assessment.views import assessmentRetUpdDelView
from auth.views import callback
from coursedetail.views import (
                                LessonListView, NoteCreateView, NoteViewSet)
from Courses.views import (Course_list_forpackage, CourseInstructorListView,
                           CourseListView, CourseRetUpdDelView,
                           CourseTutorListView, YoutubeDataApiView)
from Create_Test.views import (
                             FLTCreateView,
                               FLTTestListView, FLTTestRetrieveView,
                               MockTestStudentSubmit, ResponsesView,
                               UpdateStudentFields, createexamview,FLTStudentAddFields,
                               moduleListView, StudentSpeakingBlock)
from exam.views import ( AnswerViewSet,
                      
                        ExamViewSet, SpeakingBlockRetrieveView, SpeakingBlockView, SpeakingPracticeSetView)
from ExamResponse.views import (ExamBlockAnswerView, FLTAnswerCreateView,
                                PracticeAnswersView,
                                PracticeTestAnswerCreateView,
                                
                                SpeakingAnswerView, SpeakingBlockAnswerView,StudentAnswerListView)

from LiveClass.views import (AddBookSlot, Liveclass_Create_View,
                             
                             StudentLiveClassEnrollmentAPIView,
                             StudentRemoveLiveClassAPIView,
                             liveclass_list_view, liveclass_listwithid_view)
from master.views import (AdditionalResourceListAPIView,
                          BatchListByPackageView, CategoryListView,
                         
                          CourseMaterialListView, 
                        
                          CreateBatchAPIView, CuponListView, LanguageListView,
                       
                        LevelListView,
                           Live_Class_Type_List_View,
                          OutcomesListView,
                          PackageTypeListView,
                           RequirementsListView,
                          RequirementsRetUpdDelView, 
                        
                       
                       TestTypeViewset, batchListView,
                          )
from package.views import (CoursePackageView, EnrollPackageStudentView,
                           EnrollPackageView, PackageCreateView,
                           PackageListView,
                           UserWisePackageWithCourseID)
from payment.views import CreateOrderAPIView, TransactionView
from QuestionBank.views import *  # noqa: F403
from Reading_Exam.views import *  # noqa: F403
from Speaking_Exam.views import *  # noqa: F403
from students.views import (BatchIdwiseStudentGetView,
                          
                         
                            Student_List_View_Dashboard,
                             StudentRetUpdDelView,
                            StudentView, )
from studystreak_api.views import (ChangePasswordView,
                                 LoginView, PasswordResetView,
                                   ProfileView, RegistrationView,
                                   SendPasswordResetView,
                                   UserResetPasswordView, confirm_user,
                                   get_csrf_token)

from Writing_Exam.views import *  # noqa: F403

router = DefaultRouter()

router.register("api/exam-blocks", ExamViewSet, basename="exam-blocks")
router.register(
    "api/exam-blocks-answers", AnswerViewSet, basename="exam-blocks-answers"
)

# router.register(
#     "api/full-length-test", FullLengthTestViewSet, basename="full-length-test"
# )
router.register("api/test-types", TestTypeViewset, basename="test-types")
urlpatterns = [
    path('api/notes/<int:lesson_id>/<int:student_id>/', NoteViewSet.as_view({'get': 'list'}), name='notes-list'),
    path("api/notes/createview/", NoteCreateView.as_view(), name="createview"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("api/li", get_csrf_token, name="csrf-token"),
    # path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("api/login/", LoginView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/lessonview/", LessonListView.as_view()),
    path(
        "api/courselistview/",
        CourseListView.as_view(),
    ),
    path(
        "api/courseretupddelview/<int:pk>/",
        CourseRetUpdDelView.as_view(),
    ),
    path("api/categoryview/", CategoryListView.as_view()),
    path("api/levelView/", LevelListView.as_view()),
    path("api/requirementsview/", RequirementsListView.as_view()),
    path(
        "api/requirementsretupddelview/<int:pk>/", RequirementsRetUpdDelView.as_view()
    ),
    path("api/outcomesview/", OutcomesListView.as_view()),
    path("api/languageview/", LanguageListView.as_view()),
    path("api/packagetypeview/", PackageTypeListView.as_view()),
    path("api/packagecreateview/", PackageCreateView.as_view(), name="package-create"),
    path("api/batchview/", batchListView.as_view()),
    path("api/packagelistview/", PackageListView.as_view()),
    path("api/registration/", RegistrationView.as_view(), name="registration"),
    # path("api/profile/", ProfileView.as_view(), name="profileview"),
    path("api/changepassword/", ChangePasswordView.as_view(), name="change-password"),
    ########## api send via mail
    path("api/resetpassword/", SendPasswordResetView.as_view(), name="reset-password"),
    path(
        "api/resetpassword/<uid>/<token>/",
        PasswordResetView.as_view(),
        name="reset-with-link",
    ),
    ########## reset password user id with token
    path(
        "api/user/resetpassword/<uid>/<token>/",
        UserResetPasswordView.as_view(),
        name="password_reset",
    ),
    # path("api/QuestionType", QuestionTypeView.as_view()),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/confirm/<uid>/<token>", confirm_user, name="confirm-user"),
    path(
        "api/course/<int:pk>/packages/",
        CoursePackageView.as_view(),
        name="course-packages",
    ),
    path(
        "api/userwisepackagewithcourseid/",
        UserWisePackageWithCourseID.as_view(),
        name="listofcourse",
    ),
    path("api/enroll-package/", EnrollPackageView.as_view(), name="enroll-package"),
    path("api/studentview/", StudentView.as_view(), name="studentview"),
    path(
        "api/studentretupddelview/<int:pk>/",
        StudentRetUpdDelView.as_view(),
        name="studentretupddelview",
    ),

    path(
        "api/filterbatches/<int:package_id>/",
        BatchListByPackageView.as_view(),
        name="filter_batches",
    ),
    path(
        "api/course-materials/<int:course_id>/",
        CourseMaterialListView.as_view(),
        name="coursemateriallistview",
    ),
    path(
        "api/additional-resources/<int:course_id>/",
        AdditionalResourceListAPIView.as_view(),
        name="additional-resource-list",
    ),
    path(
        "api/enrollpackagestudentview/",
        EnrollPackageStudentView.as_view(),
        name="enrollpackagestudentview",
    ),
    path("api/cuponlistview/", CuponListView.as_view(), name="cuponlistview"),
    path(
        "api/courselistforpackage/",
        Course_list_forpackage.as_view(),
        name="courselistforpackage",
    ),
    path("api/create-batch/", CreateBatchAPIView.as_view(), name="create-batch"),
    # path('accounts/google/login/', include('allauth.urls')),
    path(
        "api/liveclass_list_view/",
        liveclass_list_view.as_view(),
        name="liveclass_list_view",
    ),
    path(
        "api/liveclass_create_view/",
        Liveclass_Create_View.as_view(),
        name="liveclass_create_view",
    ),
    path(
        "api/student_list_view_dashboard/",
        Student_List_View_Dashboard.as_view(),
        name="Student_List_view_dashboard",
    ),
    path(
        "api/live_class_type_list_view/",
        Live_Class_Type_List_View.as_view(),
        name="live_class_type_list_view",
    ),

    path(
        "api/liveclass_listwithid_view/<int:batch_id>/",
        liveclass_listwithid_view.as_view(),
        name="liveclass_listwithid_view",
    ),
    path(
        "api/enroll-students-in-live-class/",
        StudentLiveClassEnrollmentAPIView.as_view(),
        name="enroll-live-class",
    ),
    path("api/createexamview/", createexamview.as_view(), name="createexamview"),
    path("api/responsesview/", ResponsesView.as_view(), name="responsesview"),
    path(
        "api/remove-live-class/<int:pk>/",
        StudentRemoveLiveClassAPIView.as_view(),
        name="remove-live-class",
    ),
    path("api/moduleListView/", moduleListView.as_view(), name="moduleListView"),
    path(
        "api/remove-live-class/<int:pk>/",
        StudentRemoveLiveClassAPIView.as_view(),
        name="remove-live-class",
    ),
    path(
        "api/studentanswerlistview/",
        StudentAnswerListView.as_view(),
        name="studentanswerlistview",
    ),
    # path(
    #     "api/coursematerialretupddelview/<int:pk>/",
    #     CourseMaterialRetUpdDelView.as_view(),
    #     name="coursematerialretupddelview",
    # ),
    # path(
    #     "api/SaveSpeakingResponse/",
    #     SpeakingAnswerListView.as_view(),
    #     name="save_speaking_response",
    # ),
    path("api/tutorcourses/", CourseTutorListView.as_view(), name="course-list"),
    path(
        "api/instructorcourses/", CourseInstructorListView.as_view(), name="course-list"
    ),
    path("api/create/order/", CreateOrderAPIView.as_view(), name="create-order"),
    path("api/confirm/order/", TransactionView.as_view(), name="confirm-order"),
    # path("api/create-meeting/", ZoomAPiView.as_view()),
    path("api/save-video-data/", YoutubeDataApiView.as_view(), name="creat"),
    path(
        "api/student-pt-submit/",
        UpdateStudentFields.as_view(),
        name="update_student_fields",
    ),
    path(
        "api/student-mocktest-submit/",
        MockTestStudentSubmit.as_view(),
        name="MockTestStudentSubmit",
    ),
    path(
        "api/student-speakingblock-submit/",
        StudentSpeakingBlock.as_view(),
        name="StudentSpeakingBlock",
    ),
    path("api/answer/practice-test/", PracticeTestAnswerCreateView.as_view()),
    path("api/answer/full-length-test/", FLTAnswerCreateView.as_view()),
    path("api/get/flt/", FLTTestListView.as_view()),
    path("api/get/flt/<int:pk>/", FLTTestRetrieveView.as_view()),
    path("api/practice-answers/<int:pk>/", PracticeAnswersView.as_view()),
    # path("api/flt-answers/<int:flt_id>/", FLTAnswers.as_view()),
    path('api/exam-block-answers/<int:pk>/',ExamBlockAnswerView.as_view()),
    path("api/create-flt/", FLTCreateView.as_view()),   
    # path("api/save-audio-file/", SaveSpeakingAnswerFileView.as_view()),

    # path('api/packageidwisestudentgetview/<int:package_id>/', PackageIdwiseStudentGetView, name='package_students_api'),
    path('api/batchidwisestudentgetview/<int:batch_id>/', BatchIdwiseStudentGetView, name='batch_students_api'),
    # path('api/courseidwisestudentgetview/<int:course_id>/', CourseIdwiseStudentGetView, name='course_students_api'),
    path('api/add-bookslot/<int:pk>/', AddBookSlot.as_view(), name='add-bookslot'),
    path('api/student-flt-submit/',FLTStudentAddFields.as_view()),
    
    #speaking block view
    path('api/speaking-block/',SpeakingBlockView.as_view()),
    path('api/speaking-block/<int:pk>/',SpeakingBlockRetrieveView.as_view()),
    path('api/speaking-block/answers/<int:pk>/',SpeakingBlockAnswerView.as_view(),),
    
    path('api/speaking-answers/',SpeakingAnswerView.as_view()), 
    # path('api/speaking/practice-test/assesement/<int:id>/',SpeakingPracticeView.as_view()),
    path('api/speaking/practice-test/<int:pk>/',SpeakingPracticeSetView.as_view()),
    # path('login/',login),
    path('api/auth/',include('auth.urls')),
    path('api/google/',callback),
    
    #Gamification APIs 
    path('api/gamification/',include('gamification.api.urls')),
    path('api/silk/', include('silk.urls', namespace='silk')),
    
] + router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
admin.site.site_header = "StudyStreak Admin"
admin.site.site_header = "StudyStreak"
admin.site.index_title = "StudyStreak"
admin.site.site_title = "StudyStreak adminsitration"
