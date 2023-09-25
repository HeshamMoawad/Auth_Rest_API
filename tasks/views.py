from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.http import  HttpRequest
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.status import HTTP_406_NOT_ACCEPTABLE
from .serializers import TaskSerializer
from .models import (
    Task ,
    Tasks_Status ,
    Agent ,
)




# Create your views here.


def tasks_list(request:HttpRequest):
    return render(
    request ,
    'tasks_list.html',
    context={
        'user':request.user ,
        })



def tasks_login(request:HttpRequest):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if not isinstance(user,type(None)):
            login(request,user)   
            return tasks_list(request)
        else :
            return render(request,'login.html',context={})
    elif request.method == 'GET' :
        if request.user.is_authenticated :
            return tasks_list(request)
        else :
            return render(request,'login.html',context={})


def tasks_logout(request:HttpRequest):
    logout(request)
    return redirect('login')




############################################ More Info For Task

def task_info(request:HttpRequest,id:int):
    task = Task.objects.get(id=id)
    return render(request,'task_info.html',context={'task':task})





########################################### Rest FBV


@api_view(['GET'])
def analtics(request:HttpRequest,agentName:str):
    agent = Agent.objects.get(username=agentName)
    tasks = Task.objects.filter(agent=agent)
    completed = [TaskSerializer(task).data for task in tasks if task.status == Tasks_Status[1][0] ]
    pending = [TaskSerializer(task).data for task in tasks if task.status == Tasks_Status[0][0] ]
    cancelled = [TaskSerializer(task).data for task in tasks if task.status == Tasks_Status[2][0] ]
    analytics = {
        'completed' : completed,
        'percentage' : round((len(completed)/(len(completed)+len(pending))*100),1) ,
        'pending': pending,
        'cancelld': cancelled,
    }
    return Response(analytics)


@api_view(['POST'])
def add_note (request:HttpRequest):
    try :
        task = Task.objects.get(id=request.POST['id'])
        task.agent_note = request.POST['agent_note']
        if 'checkbox' in request.POST.keys():
            task.status = request.POST['checkbox']
        print(request.POST.keys())
        task.save()
        print(request.POST)
        return redirect('login')
    except Exception as e:
        print(e)
        return Response({},status=HTTP_406_NOT_ACCEPTABLE)



########################################### Rest CBV



class TasksListAPI(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        agent = Agent.objects.get(username=user.username)
        return Task.objects.filter(agent=agent)
