from django.urls import path 
from . import views
from django.conf.urls.static import static 
from tweetwave.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL, STATIC_ROOT

app_name = 'submission'

urlpatterns = [
    path('', views.index, name='index'),
    path('confession/', views.saved, name='saved'),
]  + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)