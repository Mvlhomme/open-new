from django.shortcuts import render, redirect, get_object_or_404
from .forms import CompteBeneficiaireForm
from django.contrib import messages
from comptebeneficiaire.models import CompteBeneficiaire
from django.contrib.auth.decorators import login_required



@login_required(login_url='fr_login')
def fr_mabanque(request):
	try:
		userbene = get_object_or_404(CompteBeneficiaire, user=request.user)
	except:
		return redirect('fr')
	if request.method == 'POST':
		form = CompteBeneficiaireForm(request.POST, instance=userbene)
		if form.is_valid():
			form.save()
			messages.success(request, 'SUCCESSFULL')
			return redirect('fr_mabanque')
	else:
		form = CompteBeneficiaireForm(instance=userbene)

	comptes = CompteBeneficiaire.objects.get(user_id=request.user.id)

	context = {'form': form, 'comptes': comptes, 'userbene':userbene,}

	return render(request, 'fr/mabanque.html', context)