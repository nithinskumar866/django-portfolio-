

# Register your models here.
from django.contrib import admin
from . views import *
from .models import About




from .models import Certificate, Project, About, Feedback

admin.site.register(Certificate)
admin.site.register(Project)
admin.site.register(About)
admin.site.register(Feedback)  # Register Feedback model to manage in Django admin
