from django.contrib import admin
from .models import City
from .models import DevLanguage
from .models import Vacancy

# Register your models here.
# Basically here we define entities that we should see in the console

admin.site.register(City)
admin.site.register(DevLanguage)
admin.site.register(Vacancy)

