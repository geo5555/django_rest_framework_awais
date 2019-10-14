from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

class FivePerDayUserThrottle(UserRateThrottle):
    rate = '5/day'

@api_view(['GET', 'POST'])
#@throttle_classes([FivePerDayUserThrottle])
def index(request):
    print(request.user)
    print(request.auth)
    if request.method == 'GET':
        return Response(data={'message':'this is a get request'}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        return Response(data=request.data, status=status.HTTP_200_OK)

class MessageView(APIView):
    def get(self, request):
        return Response(data="this is a class based view hit by get request", status=status.HTTP_200_OK)
    def post(self, request):
        return Response(data="this is a class based view hit post request", status=status.HTTP_200_OK)