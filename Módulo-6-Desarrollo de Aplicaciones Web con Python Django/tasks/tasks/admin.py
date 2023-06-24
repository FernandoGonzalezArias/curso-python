from django.contrib import admin

from tasks.models import Task, State, Comments

admin.site.register(Task)
admin.site.register(State)
admin.site.register(Comments)