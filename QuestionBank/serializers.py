from rest_framework import serializers
from .models import *


'''######### ReadingListSerializers #########'''

class ReadingQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadingQuestion
        fields = '__all__'

class ReadingQuestionTypeNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadingQuestionTypeName
        fields = '__all__'

class ReadingPassageNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadingPassageName
        fields = '__all__'

class Reading_QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reading_Question
        fields = '__all__'

class ReadingOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadingOption
        fields = '__all__'



'''######### ReadingRetUpdDelSerializers #########'''

class ReadingQuestionRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadingQuestion
        fields = '__all__'

class ReadingQuestionTypeNameRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadingQuestionTypeName
        fields = '__all__'

class ReadingPassageNameRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadingPassageName
        fields = '__all__'

class Reading_QuestionRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadingOption
        fields = '__all__'

class ReadingOptionRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadingOption
        fields = '__all__'


'''######### ListeningListSerializers #########'''

class ListeningQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListeningQuestion
        fields = '__all__'

class ListeningQuestionTypeNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListeningQuestionTypeName
        fields = '__all__'

class Listening_QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listening_Question
        fields = '__all__'

class Listening_OptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listening_Options
        fields = '__all__'



'''######### ListeningRetUpdDelSerializers #########'''

class ListeningQuestionRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListeningQuestion
        fields = '__all__'

class ListeningQuestionTypeNameRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListeningQuestionTypeName
        fields = '__all__'

class Listening_QuestionRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listening_Question
        fields = '__all__'

class Listening_OptionsRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listening_Options
        fields = '__all__'


'''######### WritingListSerializers #########'''

class WritingQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = WritingQuestion
        fields = '__all__'

class WritingQuestionTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = WritingQuestionType
        fields = '__all__'

'''######### WritingRetUpdDelSerializers #########'''

class WritingQuestionRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = WritingQuestion
        fields = '__all__'

class WritingQuestionTypeRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = WritingQuestionType
        fields = '__all__'
        
        
        
'''######### SpeakingListSerializers #########'''

class SpeakingQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeakingQuestion
        fields = '__all__'

class SpeakingQuestionTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeakingQuestionType
        fields = '__all__'


'''######### SpeakingRetUpdDelSerializers #########'''

class SpeakingQuestionRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeakingQuestion
        fields = '__all__'

class SpeakingQuestionTypeRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeakingQuestionType
        fields = '__all__'        
        
        