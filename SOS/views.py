from rest_framework.response import Response
from rest_framework import status
from .models import Hopitals,article
from .serializers import hospitalsSerializers,ArticleSerial
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.decorators import api_view
from django.conf import settings
import googlemaps
from rest_framework import filters
from django_filters.rest_framework import FilterSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import  ModelViewSet
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
import django_filters




class AddingArticle(CreateAPIView):
   
    queryset = article.objects.all()
    serializer_class = ArticleSerial
    permission_classes = (AllowAny,)
    @swagger_auto_schema(
         operation_description="Adding annother articles",
         responses={200,ArticleSerial}
    )
    def y():
        return 0 
    
    
    
    
class GetAllArticles(ListAPIView):
    permission_classes=[AllowAny]
    queryset=article.objects.all()
    serializer_class=ArticleSerial   
    filter_backends=[filters.SearchFilter]
    filterset_fields=['Category']
    search_fields=['^Category']
    
    
    


class UnseulHopital(APIView):

    def get(self,request,id):
        try:
            hospital = Hopitals.objects.get(id=id)
            serial = hospitalsSerializers(hospital)
        except:
            message={"msg":"id inexitant"}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

        return Response(serial.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            hospital = Hopitals.objects.get(id=id)
            serial = hospitalsSerializers(hospital)
        except:
            message = {"msg": "id inexitant"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            hoptal=Hopitals.objects.get(id=id)
        except Hopitals.DoesNotExist:
            messagee={"message":"cet hopital n'exite pas"}
            return Response(messagee,status=status.HTTP_400_BAD_REQUEST)
        hoptal.delete()
        messagee={"message":"cet hopital a été effacé"}
        return Response(messagee,status=status.HTTP_204_NO_CONTENT)
        
class touslesHopital(APIView):

    def get(self, request):
        hospitals = Hopitals.objects.all()
        serial = hospitalsSerializers(hospitals, many=True)
        return Response(serial.data)

class AddHospita(CreateAPIView):
    queryset=Hopitals.objects.all()
    serializer_class=hospitalsSerializers
    permission_classes=(AllowAny,)



@api_view(['GET'])
def getNearHospital(request,lat,lng):
    api_key=settings.GOOGLE_API_KEY
    client_go = googlemaps.Client(api_key)
    lati=float(lat)

    lngi=float(lng)
    try:
        search_string = "hospital"
        distance = 5000
        result = client_go.places_nearby(
                location=(lati,lngi),
                keyword=search_string,
                radius=distance)
       # list=[]
        #for i in result:
         #   listho=[i['']]



        return Response(result.get('results'))
    except: 
        message={"location":"not found"}
        return (message)