from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.http import HttpResponse

# Create your views here.

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request , "contacts/contact_list.html", {'contacts' : contacts})

def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Contact.objects.create(name = name , email = email , phone = phone)
        return redirect('contact_list')
    return render(request , 'contacts/contact_form.html')

def update_contact(request , pk):
    contact = get_object_or_404(Contact,pk=pk)
    if request.method == 'POST':
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.save()
        return redirect('contact_list')
    return render(request,'contacts/contact_form.html', {'contact': contact})

def delete_contact(request , pk):
    contact = get_object_or_404(Contact , pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request ,'contacts/contact_confirm_delete.html', {'contact': contact})