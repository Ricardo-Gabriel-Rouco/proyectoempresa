from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from .models import Pedido, Op, Remito

@receiver(post_save, sender = Op)
def create_pedido(sender, instance, created, **kwargs):
    if created:
        Pedido.objects.create(op=instance)

@receiver(post_save, sender = Pedido)
def create_remito(sender, instance, created, **kwargs):
    if created:
        Remito.objects.create(pedido=instance)