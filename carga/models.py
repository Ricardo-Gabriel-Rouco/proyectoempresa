from typing import ClassVar
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BigAutoField, CharField

# Create your models here.

#tabla clientes
class Clientes(models.Model):
    codcli = models.IntegerField('Codigo Cliente',primary_key=True)
    razsoc = models.CharField('Razon Social', max_length=50)
    email = models.CharField('E-mail', max_length=100)

    def __str__(self):
        return self.razsoc


class Vendedores(models.Model):
    codvend = models.IntegerField('Codigo Vendedor', primary_key=True)
    nomvend = models.CharField('Nombre Vendedor', max_length=50)

    def __str__(self):
        return self.nomvend


#Tabla OP
class Op(models.Model):
    
    #tipo de paog (anticipado o contraentrega)
    anticipado = 'Anticipado'
    entrega = 'Contra Entrega'
    PAGO_OP = [
    (anticipado, 'Anticipado'),
    (entrega, 'Contra Entrega'),
    ]
    
    #tipo op (espuma/burbuja o reventa)
    espuma = 'Esp/Burb'
    reventa = 'Reventa'
    TIPO_OP = [
    (espuma, 'Esp/Burb'),
    (reventa, 'Reventa'),
    ]   
    
    #porcentaje de facturacion
    parte1 = '100%'
    mitad = '50%'
    parte2 = '0%'
    TIPO_FAC = [
    (parte1, '100%'),
    (parte2, '0%'),
    (mitad, '50%'),
    ]
    
    #transporte
    retira = 'Retira'
    transporte = 'En transporte'
    bonificado = 'Bonificado'
    camion = 'Camion'
    DESPACHO = [
    (retira, 'Retira'),
    (transporte, 'En transporte'),
    (bonificado, 'Bonificado'),
    (camion, 'Camion Faterm'),
    ]
    
    #estados
    estabien = 'OK'
    duda = 'DUDA'
    ESTADO = [
    (duda, 'DUDA'),
    (estabien, 'OK'),
    ]
    
    opid = models.BigAutoField(primary_key=True)
    fecha = models.DateField('Fecha Pedido')
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    tipoop = models.CharField('Tipo OP', max_length=10, choices=TIPO_OP)
    fact = models.CharField('Facturacion %', max_length=5, choices=TIPO_FAC, default='100%')
    condicion = models.CharField(max_length=20, choices=PAGO_OP, default='Anticipado')
    despacho = models.CharField(max_length=20, choices=DESPACHO)
    vendedor = models.ForeignKey(Vendedores,on_delete=models.PROTECT)
    observaciones = models.TextField('Observaciones', null=True, blank=True, default=' ')
    estadoop = models.CharField('Estado OP', max_length=4, choices=ESTADO, default='DUDA')
    deudaop = models.CharField('Deuda', max_length=4, choices=ESTADO, default='DUDA')
    archivoop = models.FileField('Archivo OP', upload_to='archivoop', null=True, blank=True)



#Tabla Pedidos 
class Pedido(models.Model):
    op = models.OneToOneField(Op, to_field='opid', on_delete=models.CASCADE, primary_key=True)
    proforma1 = models.IntegerField('N° Proforma 1', blank=True, null=True, default='0')
    npedido1 = models.IntegerField('N° Pedido 1', blank=True, null=True, default='0')
    nfactura1 = models.IntegerField('N° Factura 1', blank=True, null=True, default='0')
    nrecibo1 = models.IntegerField('N° Recibo 1', blank=True, null=True, default='0')
    proforma2 = models.IntegerField('N° Proforma 2', blank=True, null=True, default='0')
    npedido2 = models.IntegerField('N° Pedido 2' ,blank=True, null=True, default='0')
    nfactura2 = models.IntegerField('N° Factura 2', blank=True, null=True, default='0')
    nrecibo2 = models.IntegerField('N° Recibo 2',blank=True, null=True, default='0')
    

#Tabla remitos
class Remito(models.Model):
    pedido = models.OneToOneField(Pedido, to_field='op', on_delete=models.CASCADE)
    fecharem1 = models.DateField('Fecha remito 1', blank=True, null=True, default='2021-01-01')
    nrem1 = models.IntegerField('N° Remito 1', blank=True, null=True, default='0')
    rem1 = models.FileField('Remito 1', upload_to='remito1', null=True, blank=True)
    fecharem2 = models.DateField('Fecha remito 2', blank=True, null=True, default='2021-01-01')
    nrem2 = models.IntegerField('N° Remito 2', blank=True, null=True, default='0')
    rem2 = models.FileField('Remito 2', upload_to='remito2', null=True, blank=True)
