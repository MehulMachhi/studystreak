from coursedetail.models import Lesson
from Courses.models import Course
from Create_Test.models import Exam, FullLengthTest, module

from .models import FlashCard

MODEL_MAPPER = {
    'flashcard':FlashCard,
    'lesson':Lesson,
    'course':Course,
    'mock':Exam,
    'fulllengthtest':FullLengthTest,
    'practicetest':module,
    
}