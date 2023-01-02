from django.shortcuts import render, redirect
from .forms import DemandeDePretForm
from django.contrib import messages

def fr_request_form(request):
	if request.method == 'POST':
		form = DemandeDePretForm(request.POST)
		if form.is_valid():
			nom = form.cleaned_data['nom']
			email = form.cleaned_data['email']
			telephone = form.cleaned_data['telephone']
			whatsapp = form.cleaned_data['whatsapp']
			pays = form.cleaned_data['pays']
			ville = form.cleaned_data['ville']
			montant_du_credit = form.cleaned_data['montant_du_credit']
			duree_de_remboursement = form.cleaned_data['duree_de_remboursement']

			form.save()
			messages.success(request, 'Succès! Votre Demande de pr a été envoyé avec succès !')
	else:
		form = DemandeDePretForm()
	context = {'form': form,}
	return render(request, 'fr/request-form.html', context)
