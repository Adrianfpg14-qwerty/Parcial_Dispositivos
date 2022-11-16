from dataclasses import field
from statistics import mode

from rest_framework import serializers
from Apps.ap_dispositivos.models import AP_Dispositivos

class ApDispositivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AP_Dispositivos
        fields = "__all__"