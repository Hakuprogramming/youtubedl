from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.youtube, name='youtube'),
    path('send_video/<str:video_id>/', views.send_video, name='send_video'),
  # video_idをパラメータで受け取る
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)