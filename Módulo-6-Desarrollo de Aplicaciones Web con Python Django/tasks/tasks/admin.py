from django.contrib import admin

from tasks.models import Task, State, Comments

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user', 'state_name')
    list_filter = ('titulo', 'user')
    search_fields = ('titulo', 'due_task')
    
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('task', 'body')
    

admin.site.register(Task, TaskAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Comments, CommentsAdmin)