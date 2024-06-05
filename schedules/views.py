from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status

from .models import ScheduleModel
from .serializers import SchedulesSerializer


class ScheduleView(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(
        query_serializer=SchedulesSerializer,
    )
    def post(self, request, *args, **kwargs):
        try:
            print(request.data)
            serializer = SchedulesSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid(raise_exception=True):
                print(request.data)
                schedule = serializer.create(request.data)
                if schedule:
                    print(request.data)
                    return Response({"data": "scheduled!"}, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(data=error, status=error.code)
        
    def get(self, request, format=None):
        print("asdasd")
        items = ScheduleModel.objects.all()
        serializer = SchedulesSerializer(items, many=True)
        print(serializer.data)
        if serializer.data: 
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"data": []}, status=status.HTTP_204_NO_CONTENT)