from django.shortcuts import render, render
from .models import Client
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

# Create your views here. 
def home(request):
    return render(request, 'home.html')

def list_clients(request):
    data = {}
    data['list'] = []
    data['error'] = []
    try:
        data['list'] = Client.objects.all()
    except:
         data['error'].append("Erro ao carregar clientes! ")
    return render(request, 'clients.html', data)


@csrf_exempt
def update_client(request): 
    if request.method == 'POST':
        id = int(request.POST.get('id', -1))
        nome = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        try:
            client = Client.objects.get(id=id)
            client.name = nome
            client.phone = phone
            client.email = email
            client.save()
        except:
            raise Http404("Error 200 - ERROR - SAVE")
    else:
        raise Http404("Error 201 - POST not found")

    
@csrf_exempt
def new_client(request): 
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'POST':
        id = int(request.POST.get('id', -1))
        nome = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        try:
            if (id == -1):
                client = Client(name=nome, phone=phone, email=email)
                client.save()
            else:
                client = Client.objects.get(id=id)
                client.name = nome
                client.phone = phone
                client.email = email
                client.save()
        except:
            data['error'].append("Erro ao cadastrar cliente! ")
            return render(request, 'clients.html', data)
        try:
            data['list'] = Client.objects.all()
        except:
            data['error'].append("Erro ao carregar clientes! ")
            return render(request, 'clients.html', data)
        return render(request, 'clients.html', data)
    else:
        data['error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'clients.html', data)

def delete_client(request):
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'GET':
        id = int(request.GET.get('id'))
        try:
            cliente = Client.objects.get(id=id)
            cliente.delete()
        except:
            data['error'].append("Erro ao deletar cliente! ")
            return render(request, 'clients.html', data)
        try:
            data['list'] = Client.objects.all()
        except:
            data['error'].append("Erro ao carregar clientes! ")
            return render(request, 'clients.html', data)
        return render(request, 'clients.html', data)
    else:
        data['error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'clients.html', data)
    

def update_client(request):
    data = {}
    data['list'] = []
    data['error'] = []
    data['client'] = []
    if request.method == 'GET':
        id = request.GET.get('id')
        try:
            data['client'].append(Client.objects.get(id=id))
        except:
            data['error'].append("Erro ao carregar cliestes! ")
            return render(request, 'clients.html', data)
        try:
            data['list'] = Client.objects.all()
        except:
            data['error'].append("Erro ao carregar clientes! ")
            return render(request, 'clients.html', data)
        return render(request, 'clients.html', data)
    else:
        data['Error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'clients.html', data)