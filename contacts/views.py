from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def fr_contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			nom = form.cleaned_data['nom']
			email = form.cleaned_data['email']
			sujet = form.cleaned_data['sujet']
			message = form.cleaned_data['message']
			form.save()
			messages.success(request, 'Succès! Votre message a été envoyé avec succès !')
	else:
		form = ContactForm()

	context = {'form': form,}
	return render(request, 'fr/contact.html', context)
