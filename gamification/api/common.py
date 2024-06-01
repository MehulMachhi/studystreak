from coursedetail.models import Lesson
from Courses.models import Course
from Create_Test.models import Exam, FullLengthTest, module
from LiveClass.models import Live_Class

from ..models import FlashCard

class ModelMapper:
    
    MODEL_MAPPER: dict = {
        "flashcard":( FlashCard, 'Flash Card'),
        "lesson": (Lesson,'Lesson'),
        "course": (Course,'Course'),
        "exam": (Exam,'Exam'),
        "fulllengthtest": (FullLengthTest,'Full Length Test'),
        "module": (module,'Mock Test'),
        "liveclass":( Live_Class, 'Live Class'),
    }
    
    def get_models_repr(self) ->list:
        return [i[1] for i in self.MODEL_MAPPER.values()]
    
    def get_model_for_rep(self,model_rep:str):
        for i in self.MODEL_MAPPER.values():
            if model_rep == i[1]:
                return i[0]
        return None
    
    def get_model_dict(self):
        return { k:v[1] for k,v in self.MODEL_MAPPER.items()}