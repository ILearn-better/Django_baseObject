from django.contrib import admin
from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    #list_display: used to set different string which show in list
    #list_display =['title','author','author_name']

    list_display = ['title', 'author']
    #search_fields =['title','content','author']#the usage of author is wrong.
    search_fields = ['title', 'content', 'author_username',
                     'author_first_name',
                     'author_last_name']


    readonly_fields = ['author']
    def save_model(self, request, obj, form, change):
        if not change:#if not change but to set up,the author name is the user's name.
            obj.author =request.user
        super(BlogAdmin,self).save_model(request,obj,form,change)
    #pass

# Register your models here.
