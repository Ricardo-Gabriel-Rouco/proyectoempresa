from django.shortcuts import redirect, render
from django.db.models import Q 
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Clientes, Op, Pedido, Remito
from .forms import CargaOp, CargarPedido, EditarPedido, EditarRemito, EditarOp, NuevoCLi
# Create your views here.

def index(request):
    busqueda = request.GET.get("buscar")
    ultimasop = Op.objects.filter(estadoop__contains='OK', deudaop__contains='OK').order_by('-fecha')
    
    if busqueda:
        ultimasop = Op.objects.filter(
            Q(fecha__icontains = busqueda) |
            Q(vendedor__icontains = busqueda) |
            Q(cliente__razsoc__icontains = busqueda) 
        ).distinct()
    
    return render(request, 'carga/index.html', context={'ultimasop':ultimasop})

#informe proformas dudosas
class ProformasListView(generic.ListView):
    model = Op
    template_name = 'carga/proformapend.html'

    def get_queryset(self):
        return Op.objects.filter(Q(estadoop__icontains='DUDA') | Q(deudaop__icontains='DUDA'))

#informe pedidos contra entrega
class ContraListView(generic.ListView):
    model = Op
    template_name = 'carga/contra.html'

    def get_queryset(self):
        return Op.objects.filter((Q(estadoop__icontains='OK') & Q(deudaop__icontains='OK')), Q(condicion__icontains='entrega'))

# informe proformas pendientes
class AnticipadoListView(generic.ListView):
    model = Op
    template_name = 'carga/anti.html'

    def get_queryset(self):
        return Op.objects.filter(Q(estadoop__icontains='OK') & Q(deudaop__icontains='OK'), Q(condicion__icontains='anticipado'))

#detalle cada pedido
class PedidoDetailView(generic.DetailView):
    model = Op
    template_name = 'carga/op_detail.html'

#creamos Op
class OpCreate(LoginRequiredMixin, generic.CreateView):
    model = Op
    form_class = CargaOp
    template_name = 'carga/formulario.html'
    success_url = reverse_lazy('index')

#modificamos op
class OpUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Op
    form_class = EditarOp
    template_name = 'carga/editar_op.html'
    success_url = reverse_lazy('index')

#creamos pedido
class PedidoCreate(LoginRequiredMixin, generic.CreateView):
    model = Pedido
    form_class = CargarPedido
    template_name = 'carga/editar_pedido.html'
    success_url = reverse_lazy('index')

#editamos pedido
class PedidoUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Pedido
    form_class = EditarPedido
    template_name = 'carga/editar_pedido.html'
    success_url = reverse_lazy('index')

#editamos remito
class RemitoUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Remito
    form_class = EditarRemito
    template_name = 'carga/editar_remito.html'
    success_url = reverse_lazy('index')

class ClienteCrear(LoginRequiredMixin, generic.CreateView):
    model = Clientes
    form_class = NuevoCLi
    template_name = 'carga/cliente.html'
    success_url = reverse_lazy('index')