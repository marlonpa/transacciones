from django.urls import reverse_lazy, path
from django.contrib.auth.decorators import login_required
from modulos.transaccion import views
from modulos.transaccion.views import ListarTra, TransaccionViewSet

urlpatterns = [

    path('lis/tra/',
         login_required(ListarTra.as_view(), login_url=reverse_lazy('users:login')),
         name='ltd'),
    path('reg/tra', views.upload_doc, name='rtd'),
    path('list', TransaccionViewSet.as_view(), name='list')


]