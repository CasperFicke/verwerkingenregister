# contacts/views.py

# django
from django.shortcuts import render

# local
from .forms import ContactForm
from . models import Contact

# index
def indexView(request):
  context = { 'form': ContactForm(), 'contacts': Contact.objects.all()}
  return render(request, 'contacts/index.html', context)

# create contact
def create_contact(request):
  if request.method=='POST':
    form = ContactForm(request.POST or None)
    if form.is_valid():
      contact = form.save()
      context = {'contact': contact}
      return render(request, 'contacts/partials/contact.html', context)
  return render(request, 'contacts/partials/form.html', {'form': ContactForm})