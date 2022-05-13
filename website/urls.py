from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_veiw(), name='home' ),
]