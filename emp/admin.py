from django.contrib import admin
from .models import *

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working' , 'emp_id' , 'phone' )
    list_editable=('working' , 'phone')
    search_fields=('name', 'phone')
    # list_filter=('working', 'emp_id')

admin.site.register(Emp, EmpAdmin)
admin.site.register(Testimonial)