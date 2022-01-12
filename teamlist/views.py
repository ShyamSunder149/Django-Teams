from django.shortcuts import render
from django.http import HttpResponse
from teamlist.models import *

# Create your views here.
def index(request):
    return render(request,'index.html',)

def addteams(request):
    if request.method == 'GET':
        return render(request,'addteams.html')
    if request.method == 'POST':
        data = request.POST
        name = data.get('teamname')
        count = data.get('count')
        teamtype = data.get('type')
        a = TeamsList.objects.create(name=name,no_of_members=count,team_type=teamtype)
        return render(request,'success.html')

def listteams(request):
    a = TeamsList.objects.all()
    return render(request,'listteams.html',{'a':a})

def delete(request):
    if request.method == 'GET':
        return render(request,'delete.html')
    if request.method == 'POST':
        data = request.POST
        name = data.get('teamname')
        a = TeamsList.objects.all()
        flag = 0
        for i in a:
            if i.name == name:
                i.delete()
                return render(request,'success.html')
                flag = 1
        if flag==0:
            return HttpResponse('Team name not found in Database')
def update(request):
    if request.method == 'GET':
        return render(request,'update.html')
    if request.method == 'POST':
        data = request.POST
        name = data.get('teamname')
        count = data.get('count')
        teamtype = data.get('type')
        a = TeamsList.objects.all()
        flag = 0
        for i in a:
            if i.name == name:
                i.no_of_members = count
                i.team_type = teamtype
                i.save()
                return render(request,'success.html')
                flag = 1
        if flag == 0:
            return HttpResponse('Team name not found in Database')