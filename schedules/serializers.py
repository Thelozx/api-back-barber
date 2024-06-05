from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import ScheduleModel

class SchedulesSerializer(serializers.ModelSerializer):
	class Meta:
		model = ScheduleModel
		fields = '__all__'
	def create(self, user_data):
		schedule_data = ScheduleModel.objects.create(day_of_week=user_data['day_of_week'], barber_name=user_data['barber_name'], hour=user_data['hour'], type=user_data['type'])
		schedule_data.save()
		return schedule_data