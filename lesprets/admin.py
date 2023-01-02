from django.contrib import admin
from .models import Demande_De_Pret

class DemandePretAdmin(admin.ModelAdmin):
	list_display = ('nom', 'email', 'whatsapp', 'montant_du_credit', 'date_send')

admin.site.register(Demande_De_Pret, DemandePretAdmin)
