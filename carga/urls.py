from django.urls import path, include
from carga import views
from carga.views import OpCreate, OpUpdate, PedidoCreate, PedidoDetailView, PedidoUpdate, ProformasListView, RemitoUpdate, AnticipadoListView, ContraListView, ClienteCrear

urlpatterns = [ 
    path('', views.index, name='index'),
    path('detalle/<int:pk>', PedidoDetailView.as_view(), name='detalleop'),
    path('cargar/', OpCreate.as_view(), name='cargar'),
    path('editar/<int:pk>/', OpUpdate.as_view(), name='editop'),
    path('crearpedido/<int:pk>/', PedidoCreate.as_view(), name='nuevopedido'),
    path('editarpedido/<int:pk>/', PedidoUpdate.as_view(), name='editarpedido'),
    path('editarremito/<int:pk>/', RemitoUpdate.as_view(), name='editarremito'),
    path('dudaproforma/', ProformasListView.as_view(), name='proformapend' ),
    path('anticipado/', AnticipadoListView.as_view(), name='anticipados' ),
    path('contraentr/', ContraListView.as_view(), name='contras' ),
    path('cliente/', ClienteCrear.as_view(), name='cliente' ),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]