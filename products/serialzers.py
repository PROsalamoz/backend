from rest_framework import serializers
from .models import Delivery_Person


class Delivery_PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Delivery_Person
        fields = '__all__'

