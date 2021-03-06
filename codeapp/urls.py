from django.urls import path 
from .import views 
from .views import LikeView

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:python_id>/', views.detail, name='detail'),
	path('like/<int:pk>/', LikeView, name='like_python'),
	path('about/', views.about, name='about'),
]