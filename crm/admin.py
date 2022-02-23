from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm

class AdminComment(admin.StackedInline):
    model = ComentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 0


class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_data_time', 'order_name', 'order_phone', 'order_address')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_status', 'order_data_time', 'order_name', 'order_phone', 'order_address')
    list_filter = ('order_status',)
    list_editable = ('order_status',)
    list_per_page = 50

    inlines = [AdminComment]

admin.site.register(Order, AdminOrder)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)
