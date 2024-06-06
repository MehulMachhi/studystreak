from django.apps import apps
class __ModelMapper:
    def __init__(self) -> None:
        print('loading ModelMapper')

    MODEL_MAPPER: dict = {
        "flashcard": ('gamification', 'FlashCard', 'Flash Card'),
        "lesson": ('coursedetail', 'Lesson', 'Lesson'),
        "course": ('Courses', 'Course', 'Course'),
        "exam_block": ('exam', 'Exam', 'Exam Block'),
        "flt": ('Create_Test', 'FullLengthTest', 'Full Length Test'),
        "practice_test": ('Create_Test', 'module', 'Practice Test'),
        "live_class": ('LiveClass', 'Live_Class', 'Live Class'),
    }

    def get_models_repr(self) -> list:
        return [i[2] for i in self.MODEL_MAPPER.values()]

    def get_model_for_rep(self, model_rep: str, **kwargs):
        """User `return_rep` to return the model's representation for the frontend"""
        if kwargs.get("return_rep"):
            for k, v in self.MODEL_MAPPER.items():
                if model_rep == v[1].lower() or model_rep == k or model_rep == v[2]:
                    return v[-1]

        else:
            for k, v in self.MODEL_MAPPER.items():
                if model_rep == v[1].lower() or model_rep == k or model_rep == v[2]:
                    return apps.get_model(v[0], v[1])
        return None

    def get_model_dict(self):
        return {k: v[2] for k, v in self.MODEL_MAPPER.items()}


model_mapper = __ModelMapper()
