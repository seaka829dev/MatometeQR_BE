from django.contrib import admin
from .models import QRInfo

# Register your models here.
class QRInfoAdmin(admin.ModelAdmin): 
    list_display = ('id', 'title1', 'title2')

admin.site.register(QRInfo, QRInfoAdmin)