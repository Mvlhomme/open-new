from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserProfileForm, UserForm
from .models import Account, UserProfile
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from comptebeneficiaire.models import CompteBeneficiaire


def fr_register(request):
	print('Je suis 1')
	if request.method == 'POST':
		print('Je suis 2')
		form = RegistrationForm(request.POST)
		print('Je suis 3')
		if form.is_valid():
			print('Je suis 4')

			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']

			pays = form.cleaned_data['pays']
			city = form.cleaned_data['city']
			langue = form.cleaned_data['langue']
			devise = form.cleaned_data['devise']
			
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']

			username = email.split("@")[0]

			first_name = form.cleaned_data['first_name']

			user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
			
			user.pays = pays
			user.city = city
			user.langue = langue
			user.devise = devise
			user.save()

			profile = CompteBeneficiaire()
			profile.user_id = user.id
			profile.nomBanque = "__"
			profile.nomBeneficiaire ="__"
			profile.iban = "__"
			profile.bic_swift = "__"
			profile.pays = "__"
			profile.save()

			plus_profile = UserProfile()
			plus_profile.user_id = user.id
			plus_profile.job = "__"
			plus_profile.birthday = "__"
			plus_profile.profile_picture = 'default/default-user.png'
			plus_profile.sexe = "__"
			plus_profile.code_postale = "__"
			plus_profile.adresse = "__"
			plus_profile.nationality = "__"
			plus_profile.save()


			messages.success(request, 'Enrégistrement réussir.')
			return redirect('fr_login')
	else:
		form = RegistrationForm()
		
	context = {
		'form': form,
	}
	return render(request, 'fr/register.html', context)



def fr_login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']

		user = auth.authenticate(email=email, password=password)

		if user is not None:
			auth.login(request, user)
			messages.success(request, 'Vous êtes maintenant connecté !')
			return redirect('fr_dashboard')
		else:
			messages.error(request, 'Identifiant de connexion invalid !')
			return redirect('fr_login')

	return render(request, 'fr/login.html')



@login_required(login_url = 'fr_login')
def fr_logout(request):
	auth.logout(request)
	messages.success(request, 'Vous êtes déconnecté.')
	return redirect('fr_login')



def fr_profile(request):
	userprofile = get_object_or_404(UserProfile, user=request.user)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'SUCCESSFULL')
			return redirect('fr_profile')
	else:
		user_form = UserForm(instance=request.user)
		profile_form = UserProfileForm(instance=userprofile)

	context = {
		'user_form': user_form,
		'profile_form': profile_form,
		'userprofile': userprofile,
	}
	return render(request, 'fr/profile.html', context)



def fr_dashboard(request):
	return render(request, 'fr/dashboard.html')


def fr_reset(request):
	return render(request, 'fr/password/reset.html')

