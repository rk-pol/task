from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('logout/', views.logout_view, name='logout_view'),
	path('sign_in/', views.Sign_inView.as_view(), name='Sign_inView'),
	path('registrate/', views.registrate.as_view(), name='registrate'),
	path('article/<int:id_article>', views.article, name='article'),
]