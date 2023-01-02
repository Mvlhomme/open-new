from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
	def create_user(self, first_name="None", last_name="None", email="kits@gmail.com", username="None", password=None):
		if not email:
			raise ValueError('Utilisateur doit avoir une adresse électronique')

		if not username:
			raise ValueError('Utilisateur doit avoir un nom utilisateur')

		user = self.model(
			email= self.normalize_email(email),
			username = username,
			last_name=last_name,
			password=password,
			first_name = first_name,
		)

		user.set_password(password)
		user.is_active = True
		user.save(using=self._db)
		return user 

	def create_superuser(self, first_name, last_name, email, username, password):
		user = self.create_user(
			email = self.normalize_email(email),
			username = username,
			password = password,
			first_name = first_name,
			last_name = last_name,
		)

		user.is_admin = True
		user.is_active = True
		user.is_staff = True
		user.is_superadmin = True 
		user.save(using=self._db)
		return user 




class Account(AbstractBaseUser):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length=100, unique=True)
	phone_number = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	langue = models.CharField(max_length=50)
	pays = models.CharField(max_length=50)
	devise = models.CharField(max_length=50)

	#required
	date_joined = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(auto_now_add=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_superadmin = models.BooleanField(default=False)

	USERNAME_FIELD ='email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

	objects = MyAccountManager()

	def full_name(self):
		return f'{self.first_name} {self.last_name}'


	def __str__(self):
		return self.email 

	def has_perm(self, perm, obj=None):
		return self.is_admin 

	def has_module_perms(self, add_label):
		return True


class UserProfile(models.Model):
	user = models.OneToOneField(Account, on_delete=models.CASCADE)
	job = models.CharField(blank=True, max_length=100)
	birthday = models.CharField(blank=True, max_length=100)
	profile_picture = models.ImageField(blank=True, upload_to='userprofile')
	sexe = models.CharField(blank=True, max_length=20)
	code_postale = models.CharField(blank=True, max_length=100)
	adresse = models.CharField(blank=True, max_length=100)
	nationality = models.CharField(blank=True, max_length=100)

	def __str__(self):
		return self.user.first_name

