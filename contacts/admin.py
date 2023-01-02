from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
	list_display = ('nom', 'email', 'sujet', 'date_send')

admin.site.register(Contact, ContactAdmin)
