from rest_framework.serializers import ModelSerializer
from qv1.models import Question,Quiz

class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        #fields = ('name','description')
        fields = '__all__'

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

