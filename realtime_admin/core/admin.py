from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib import admin
from django.db.models.signals import post_save, post_delete

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'client', 'value']


def save_order(sender, instance, **kwargs):
    data = {
        'type': 'admin_event',
        'product': 'Beer',
        'client': 'Channels',
        'value': 23
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("admin_change_list", data)


def delete_order(sender, instance, **kwargs):
    print(instance.id)


post_save.connect(save_order, sender=Order)
post_delete.connect(delete_order, sender=Order)

admin.site.register(Order, OrderAdmin)
