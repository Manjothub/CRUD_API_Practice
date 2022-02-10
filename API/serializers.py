from xml.parsers.expat import model
from rest_framework import serializers
from .models import *


class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Bookslibrarry
        fields= "__all__"