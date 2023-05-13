from .models import *
from  rest_framework import serializers

class ArticleSerial(serializers.ModelSerializer):
    filter_fields = ('Category')
    search_fields=['Category']
    class Meta:
        model=article
        fields='__all__'



class hospitalsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Hopitals
        fields='__all__'
