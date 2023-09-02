from django.contrib import admin
from core.models import New ,Setting
from core.models import *


# Register your models here.


admin.site.register(Setting)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Contact)

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display=('title', 'like', 'content','views','created_ad','update_at')
    search_fields=('title','content')
    readonly_fields=('like', 'dislike', 'views')
