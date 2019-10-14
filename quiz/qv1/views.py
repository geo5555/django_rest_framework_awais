from django.shortcuts import render
from rest_framework.views import APIView
from qv1.models import Question, Quiz
from qv1.serializers import QuizSerializer,QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class QuizView(APIView):

    def get_object(self):
        try:
            return Quiz.objects.all()
        except:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request):
        queryset = self.get_object()
        serializer = QuizSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        print("post called")
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        queryset = Quiz.objects.get(id=request.data['id'])
        print(request.data)
        print("delete was called")
        queryset.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)