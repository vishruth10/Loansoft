from django.contrib import admin
from django.contrib import admin
from account.models import *
admin.site.register(Lecturers)
admin.site.register(History)
admin.site.site_header = "LoanSoft"
admin.site.site_title = "MIT Mysore Admin Portal"
admin.site.index_title = "Welcome to MIT Mysore"
# Register your models here.
