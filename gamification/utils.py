def check_exam_block_answers_existance(exam_block):...

import json

from django.db.models import Sum
from django_redis import get_redis_connection

from ExamResponse.models import Studentanswer
from gamification.models import PointHistory


def check_practice_sets(instance:Studentanswer,set_type):
    sets = getattr(
                instance.Practise_Exam, set_type
            ).all()

    for exam_block in sets:
        if not Studentanswer.objects.filter(
            user=instance.user,
            exam=exam_block,
            Practise_Exam=instance.Practise_Exam,
        ).exists():
            return None

    try:
        getattr(instance.user, "student")
    except AttributeError:
        return
    
def save_points_and_publish_message(gamification_object,user,*args, **kwargs) -> dict:
    '''saves the points and return the status if the data was published on websocket'''
    obj, created = PointHistory.objects.get_or_create(
        student = user.student,
        gamification=gamification_object
    )
    points = obj.gamification.points
    total_points = PointHistory.objects.filter(student=user.student).aggregate(total = Sum('gamification__points'))['total']
    data =  {
        "type": "points",
        "points": points,
        "user_id": user.id,
        "total_points": total_points,
        'model':gamification_object.content_type.model
    }
    
    if created:
       return publish_message(data)
    return False
    
def publish_message(message:dict) -> bool:
    'publish the given message to redis'
    try:
        connection = get_redis_connection("default")
        payload = json.dumps(message)
        connection.publish("events", payload)
    
    except Exception as e:
        print(e)
        return False