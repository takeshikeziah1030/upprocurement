from django.urls import path
from  . import views
from .views import ProcurementUpdateView, ProcurementCreateView, ProcurementDeleteView, introView, PendingUpdateView
#from .views import NewRequestCreateView 
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'accounts'


urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('upload/', views.upload, name='upload'),
    path('intro/', views.introView.as_view(), name='intro'),
    path('list', views.ProcurementList.as_view(), name ='list'),
    path('complete', views.CompleteList.as_view(), name ='complete'),
    path('<int:pk>', views.ProcurementDetail.as_view(), name = 'details'),
    path('new/', views.ProcurementCreateView.as_view(), name='new'),
    path('request/', views.PendingList.as_view(), name='request'),
    path('reports', views.reports, name='reports'),
    path('chart', views.charts, name='chart'),
    path('<int:pk>/update/', views.PendingUpdateView.as_view(), name='pending_update'),
    path('<int:pk>/edit/', views.ProcurementUpdateView.as_view(), name='procurement_edit'),
    path('<int:pk>/delete/', views.ProcurementDeleteView.as_view(), name='procurement_delete'),


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)