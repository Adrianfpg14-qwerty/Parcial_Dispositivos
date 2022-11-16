from django.urls import path
from Apps.ap_dispositivos.views import ApDispositivosList, ApDispositivosDetail


app_name = "ap_dispositivos"

urlpatterns = [
    path('', ApDispositivosList.as_view()),
    path('<int:pk>', ApDispositivosDetail.as_view()),
]