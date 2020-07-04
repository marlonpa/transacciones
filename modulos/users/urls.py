from django.urls import reverse_lazy, path
from django.contrib.auth.decorators import login_required

from modulos.users.views import Login, salir, Panel, Lus, Rus, Uus, CambiarEstado

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('salir/', salir, name='salir'),
    path('start/', login_required(Panel.as_view(),
         login_url=reverse_lazy('users:login')), name='base'),
    path('lis/usu/',
         login_required(Lus.as_view(), login_url=reverse_lazy('users:login')),
         name='lus'),
    path('reg/usu/',
         login_required(Rus.as_view(), login_url=reverse_lazy('users:login')),
         name='rus'),
    path('upd/<int:pk>/usu/',
         login_required(Uus.as_view(), login_url=reverse_lazy('users:login')),
         name='uus'),
    path('cam/<int:pk>/est/',
         login_required(CambiarEstado, login_url=reverse_lazy('users:login')),
         name='cest'),
]