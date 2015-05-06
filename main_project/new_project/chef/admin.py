from django.contrib import admin
from chef.models import NewUserProfile, NewRestaurantProfile
from chef.models import Category, Page, Skill, PostNewJob, Applicant, UserType

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Page, PageAdmin)
admin.site.register(NewUserProfile)
admin.site.register(NewRestaurantProfile)
admin.site.register(PostNewJob)
admin.site.register(Applicant)
admin.site.register(UserType)



