from django.contrib import admin
from apitest.models import ApiTest, ApiStep


# Register your models here.
class ApistepAdmin(admin.TabularInline):

    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id', 'apitest']
    model = ApiStep
    extra = 1


class ApitestAdmin(admin.ModelAdmin):

    list_display = ['apitestname', 'apitester', 'apitestresult', 'create_time', 'id']
    inlines = [ApistepAdmin]
