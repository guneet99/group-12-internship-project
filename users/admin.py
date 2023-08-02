from django.contrib import admin
from .models import Profile,Calorie_Intake,Calorie_Disturb,Alert_Button

admin.site.register(Profile)
admin.site.register(Calorie_Intake)
admin.site.register(Calorie_Disturb)
admin.site.register(Alert_Button)