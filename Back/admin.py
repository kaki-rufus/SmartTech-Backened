from django.contrib import admin
from .models import *

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# Members
class MembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')

# contacts
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone')

admin.site.register(About, AboutAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Home)
