from django.contrib import admin
from chef.models import UserProfile
from chef.models import Category, Page, Skill

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

