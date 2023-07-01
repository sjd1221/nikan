from django.contrib import admin
from .models import Doctor, Personnel, Person, HospitalName




class AdminDoctor(admin.ModelAdmin):
    list_display = ('Name', 'Prof', 'Mobile', 'IdDoctor', 'Prof2', 'Hospital')
    list_filter = ('Prof', 'Prof2', 'Hospital')
    search_fields = ('Name', 'Prof', 'Mobile', 'IdDoctor', 'Prof2', 'Hospital')


class AdminPersonnel(admin.ModelAdmin):
    list_display = ('Name', 'Post', 'Mobile', 'IdPersonnel', 'Section', 'Hospital')
    list_filter = ('Post', 'Section', 'Hospital')
    search_fields = ('Name', 'Post', 'Mobile', 'IdPersonnel', 'Section', 'Hospital')


class AdminPerson(admin.ModelAdmin):
    list_display = ('Name', 'Mobile', 'IdPerson', 'Hospital')
    list_filter = ('Hospital',)
    search_fields = ('Name', 'Mobile', 'IdPerson', 'Hospital')


# class AdminHospital(admin.ModelAdmin):
#     list_display = ('Name',)

admin.site.register(Doctor, AdminDoctor)
admin.site.register(Personnel, AdminPersonnel)
admin.site.register(Person, AdminPerson)
# admin.site.register(HospitalName, AdminHospital)
