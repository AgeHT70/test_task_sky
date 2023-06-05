from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from sales_chain.models import Contact, Product, ChainLink


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_date')


@admin.register(ChainLink)
class ChainLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'debt', 'link_to_supplier')  # 'link_to_supplier')supplier
    # list_select_related = ['supplier']
    actions = ('clear_debt',)
    list_filter = ['contact__city']

    @staticmethod
    def link_to_supplier(obj):
        if obj.supplier:
            return format_html(
                '<a href="{}">{}</a>',
                reverse('admin:sales_chain_chainlink_change', args=[obj.supplier_id]),
                obj.supplier,
            )

    @admin.action(description='Clear debt for ChainLink')
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
