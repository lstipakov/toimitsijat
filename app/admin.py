from django.contrib import admin

from .models import Task, Parent, Child, Arena, Match

class TaskAdmin(admin.ModelAdmin):
    fields = ['task_type']
    list_display = ('__str__', 'parents',)

class ParentAdmin(admin.ModelAdmin):    
    list_display = ('__str__', 'get_tasks','children',)

class ChildAdmin(admin.ModelAdmin):    
    list_display = ('__str__', 'get_parents',)

def luo_toimitsijalista(modeladmin, request, queryset):
    for q in queryset.all():
        q.luo_toimitsijalista()
        q.save()

class MatchAdmin(admin.ModelAdmin):
    actions = [luo_toimitsijalista]
    list_display = ('__str__', 'date', 'kello', 'kuulutus', 'jäähy_1', 'jäähy_2', 'pöytäkirja', 'titu', 'kuvaaja')

admin.site.register(Task, TaskAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Arena)
admin.site.register(Match, MatchAdmin)
