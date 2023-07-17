from django.shortcuts import render
import json
import sys
from django.http import HttpResponse
import requests
# Create your views here.

def index(request):
    
        if (request.method=='POST'):
            city=request.POST['city']
            if(city==""):
                return render(request,'base.html')
            
            else:
                res=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=33bf3d23be0f4c46e802b7a5530f9ceb')
                json_data=res.json()
                data = {
                "city":city,
                "country_code":str(json_data['sys']['country']),
                "temperature":str(json_data['main']['temp']) + 'k' ,
                "pressure":str(json_data['main']['pressure']) + 'hPa',
                "humidity":str(json_data['main']['humidity']) + '%',
                "coordinate":str(json_data['coord']['lon']) + str(json_data['coord']['lat']),
                }
                return render(request,'index.html',data)
        else:
            return render(request,'base.html')
  

