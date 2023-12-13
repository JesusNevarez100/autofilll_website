from django.shortcuts import render, get_object_or_404, redirect
from .forms import DealershipForm, LienholderForm
from .models import Lienholder, Dealership
# Create your views here.



def edit_lienholder(request, lienholder_id):
    lienholder = get_object_or_404(Lienholder, id=lienholder_id)
    if request.method == 'POST':
        lienholder_form = LienholderForm(request.POST, instance=lienholder)
        if lienholder_form.is_valid():
            lienholder_form.save()
            return redirect('/account-information')  # Replace 'vehicle_list' with the URL name for the list view of all vehicles
    else:
        lienholder_form = LienholderForm(instance=lienholder)
    return render(request, 'account_information/edit_lienholder.html', {'lienholder_form': lienholder_form})

def delete_lienholder(request, lienholder_id):
    lienholder = get_object_or_404(Lienholder, id=lienholder_id)
    if request.method == "POST":
        lienholder.delete()
        return redirect('/account-information')
    context = {
        "lienholder":lienholder
    }
    return render(request, 'vehicle_inventory_system/confirm_delete.html', context)


def lienholder_information(request):
    lienholder_form = LienholderForm()
    if request.method == "POST":
        lienholder_form = LienholderForm(request.POST)
        if lienholder_form.is_valid():
            lienholder_form.save()
        return redirect("/account-information")
    context = {
        "lienholder_form":lienholder_form
    }
    return render(request, "account_information/enter_lienholder_info.html", context)

def edit_dealer(request, dealer_id):
    dealer = get_object_or_404(Dealership, id=dealer_id)
    if request.method == 'POST':
        form = DealershipForm(request.POST, instance=dealer)
        if form.is_valid():
            form.save()
            return redirect('/account-information')  # Replace 'vehicle_list' with the URL name for the list view of all vehicles
    else:
        form = DealershipForm(instance=dealer)
    return render(request, 'account_information/edit_dealer.html', {'form': form})


def dealer_information(request):
    form = DealershipForm()
    if request.method == "POST":
        form = DealershipForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/account-information")
    context = {
        "form":form
    }
    return render(request, "account_information/enter_dealership_info.html", context)


def account_information_home(request):
    dealership = Dealership.objects.all()
    lienholders = Lienholder.objects.all()
    context = {
        'dealership':dealership,
        'lienholders': lienholders
    }
    return render(request, 'account_information/account_information_home.html', context)



