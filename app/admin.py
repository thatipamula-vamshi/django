from django.contrib import admin
from app.models import JobPost,Location,Author,Skills

class JobAdmin(admin.ModelAdmin):
    list_display = ['__str__','title','date',"salary"]
    list_filter=('salary','date')
    search_fields =('title','description','salary')
    search_help_text = 'write your query here and hit enter'
    #fields = (('title','description'),'salary')
    #exclude = ('salary',)

    fieldsets= (
        ('basic inormation',{
            'fields': ('title','description')
        }),
        ('more information',{
            'classes':('collapse','wide'),
            'fields':(('expiry','salary'),'slug',)
        })
    )


# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)