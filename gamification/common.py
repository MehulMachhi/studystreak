from coursedetail.models import Lesson
from Courses.models import Course
from Create_Test.models import Exam, FullLengthTest, module
from LiveClass.models import Live_Class

from .models import FlashCard

MODEL_MAPPER = {
    'flashcard':FlashCard,
    'lesson':Lesson,
    'course':Course,
    'exam':Exam,
    'fulllengthtest':FullLengthTest,
    'module':module,
    'liveclass':Live_Class,
    
    
}