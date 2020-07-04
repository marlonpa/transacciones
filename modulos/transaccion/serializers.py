from rest_framework import serializers
from modulos.transaccion.models import Transaccion

class TransaccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaccion
        fields = ['transaction_id', 'transaction_date', 'transaction_amount', 'client_id', 'client_name']


