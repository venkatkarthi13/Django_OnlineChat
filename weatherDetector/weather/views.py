from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == 'POST':
        city=request.POST['city']
        api_key="4cc12cc1c9518b156f1385491eb8f578"
        api_url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        res=urllib.request.urlopen(api_url).read()
        Json_data=json.loads(res)
        data={
            "country_code":str(Json_data['sys']['country']),
            'coordinate':str(Json_data['coord']['lon'])+' '+str(Json_data['coord']['lat']),
            'temp':str(Json_data['main']['temp'])+'k',
            'pressure':str(Json_data['main']['pressure']),
            'humidity':str(Json_data['main']['humidity'])
            
        }
    else:
        city=''
        data={}
    return render(request, "index.html",{"city":city,"data":data})
    