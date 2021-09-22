from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Clientes, Op, Pedido, Remito

class CargaOp(forms.ModelForm):
    observaciones = forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}), required=False)
    class Meta:
        model = Op

        fields = [
            'fecha',
            'cliente',
            'tipoop', 
            'fact', 
            'condicion', 
            'despacho', 
            'vendedor', 
            'observaciones',
            'estadoop',
            'deudaop',
            'archivoop',
        ]

class EditarOp(forms.ModelForm):
    despacho = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}), required=False)
    observaciones = forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}), required=False)
    class Meta:
        model = Op

        fields = [
            'fecha',
            'cliente',
            'tipoop', 
            'fact', 
            'condicion', 
            'despacho', 
            'vendedor', 
            'observaciones',
            'estadoop',
            'deudaop',
            'archivoop',
        ]


class CargarPedido(forms.ModelForm):
    
    class Meta:
        model = Pedido

        fields = [
            'proforma1',
            'npedido1',
            'nfactura1',
            'nrecibo1',
            'proforma2',
            'npedido2',
            'nfactura2',
            'nrecibo2',
        ]

class EditarPedido(forms.ModelForm):
    
    class Meta:
        model = Pedido

        fields = [
            'proforma1',
            'npedido1',
            'nfactura1',
            'nrecibo1',
            'proforma2',
            'npedido2',
            'nfactura2',
            'nrecibo2',
        ]

class EditarRemito(forms.ModelForm):
    
    class Meta:
        model = Remito

        fields = [
            'fecharem1',
            'nrem1',
            'rem1',
            'fecharem2',
            'nrem2',
            'rem2',
        ]

class NuevoCLi(forms.ModelForm):
    email = forms.CharField(required=False)
    class Meta:
        model = Clientes

        fields = [
            'codcli',
            'razsoc',
            'email',
        ]