from django.urls import path
from .views import home,index, profile, RegisterView,logout_view,real_time_ingest,live_dashboard
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('logout_view/',logout_view,name='logout_view'),
    path('index/', index, name='users-index'),
    path('Air_db',views.Air_db,name='Air_db'),

    path("live-dashboard/", live_dashboard, name="live_dashboard"),
    path("api/realtime/", real_time_ingest, name="real_time_ingest"),
    ]


 