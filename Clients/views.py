from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm


# Create your views here.
def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    if request.method == "POST":
        client.delete()
        return redirect('/client-vault')
    context = {
        "client":client
    }
    return render(request, 'Clients/confirm_delete.html', context)


def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/client-vault')
    else:
        form = ClientForm(instance=client)
    return render(request, 'Clients/edit_client.html', {"form":form})


def add_client(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/client-vault")
    
    context = {
        "form":form
    }
    return render(request, "Clients/add_clients.html", context)

def client_vault(request):
    clients = Client.objects.all()
    context = {
        "clients":clients
    }
    return render(request, "Clients/client_vault.html", context)


