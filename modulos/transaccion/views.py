import datetime
from rest_framework import viewsets, generics
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from modulos.transaccion.form import UploadDocumentForm
from modulos.transaccion.models import Transaccion, Archivo
import pandas as pd
from modulos.transaccion.serializers import TransaccionSerializer
from rest_framework.filters import  SearchFilter, OrderingFilter
from rest_framework.pagination import  PageNumberPagination



#Clase listar
from modulos.users.models import Users
from transacciones import settings


class ListarTra(ListView):
    template_name = 'tra/lis.html'
    model = Transaccion
    paginate_by = 30
    qs = None
    permission_required = 'users.view_users'

    def get_queryset(self):
        if self.request.user.is_superuser:
            self.qs = Transaccion.objects.all()
        elif self.request.user.is_admin:
            self.qs = Transaccion.objects.all()
        else:
            raise Http404

        nom = self.request.GET.get('nom', None)

        if nom:
            self.qs = self.qs.filter(name__icontains=nom)

        return self.qs

    def get_context_data(self, **kwargs):
        context = super(ListarTra, self).get_context_data(**kwargs)
        tot = len(self.qs)
        context["tot"] = tot
        context['tit_cont'] = 'Transactions'
        context['sub_tit_cont'] = ' List'
        nom = self.request.GET.get('nom', None)

        if nom:
            context["nom"] = nom
        return context


def upload_doc(request):
    form = UploadDocumentForm()
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)

        if form.is_valid():
            ar = form.save(form)
            ar.fecha = datetime.date.today()
            ar.user = request.user
            ar.save()

            consulta = Archivo.objects.filter().last()



            datos = pd.read_csv('media/{}'.format(consulta.name), header=0, delimiter=";")
            id = datos['transaction_id'].values
            fecha = datos['transaction_date'].values
            monto = datos['transaction_amount'].values
            id_cliente = datos['client_id'].values
            cliente = datos['client_name'].values

            for f in fecha:
                print(f)
            for i in id:
                print(i)
            for m in monto:
                print(m)
            for ic in id_cliente:
                print(ic)
            for c in cliente:
                print(c)

            t = Transaccion.objects.create(
                transaction_id=i,
                transaction_date=f,
                transaction_amount=m,
                client_id=ic,
                client_name=c,
                archivo=consulta
            )

            t.save()

    return render(request, 'tra/UploadFile.html', {'form': form})

"""
class TransaccionViewSet(viewsets.ModelViewSet):
    serializer_class = TransaccionSerializer
    queryset = Transaccion.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('transaction_id', 'transaction_date', 'transaction_amount', 'client_id', 'client_name')
    ordering_fields = ('id',)
    pagination_class = PageNumberPagination"""


class TransaccionViewSet(generics.ListAPIView):
    serializer_class = TransaccionSerializer
    queryset = Transaccion.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('transaction_id', 'transaction_date', 'transaction_amount', 'client_id', 'client_name')
    ordering_fields = ('id',)
    pagination_class = PageNumberPagination
