from django.shortcuts import render,redirect
import requests
import csv

# Create your views here.
def index(request):
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    r = requests.get(url,stream=True)
    f = (line.decode('utf-8') for line in r.iter_lines())
    reader = list(csv.reader(f))
    lst =[]
    todays = 0
    previous = 0
    for row in reader[1:]:
        temp = {
            'province':row[0],
            'country':row[1],
            'affected_people':row[-1]
        }
        todays += int(row[-1])
        previous += int(row[-2])
        lst.append(temp)
    context = {
        'todays':todays,
        'previous':previous,
      'coronas':lst
    }
    return render(request,'index.html',context)
