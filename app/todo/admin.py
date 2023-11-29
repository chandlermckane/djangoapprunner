from django.contrib import admin
from .models import List, Announcement, Feedback

admin.site.register(List)
admin.site.register(Announcement)  
admin.site.register(Feedback)