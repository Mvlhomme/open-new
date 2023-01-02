from django.contrib import admin
from .models import CompteBeneficiaire

class CompteBeneficiaireAdmin(admin.ModelAdmin):
	list_display = ('user', 'nomBanque', 'nomBeneficiaire', 'iban', 'bic_swift', 'pays', 'date_send')

admin.site.register(CompteBeneficiaire, CompteBeneficiaireAdmin)