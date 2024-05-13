from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Order, OrderItem


def order_payment(obj):
    if not obj.stripe_id:
        return ''

    url = obj.get_stripe_url()
    html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
    return mark_safe(html)


order_payment.short_description = 'Stripe payment'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    order_payment, 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
