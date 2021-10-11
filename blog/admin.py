from django.contrib import admin
from .models import Category, Article, Contact

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('create_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('create_at', 'update_at', 'user')

    def save_model (self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user

        obj.save()

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Contact)