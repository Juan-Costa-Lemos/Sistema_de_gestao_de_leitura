"""gestao_de_leitura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from gestao_leitura import views
from django.contrib.auth import views as auth_views
from usuarios import views as usuarios_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name = 'usuarios/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'usuarios/logout.html'), name='logout'),
    path('conta/',usuarios_views.novo_usuario,name='novo_usuario'),
    path('',views.home,name='home'),
    path('minhas_leituras/',views.minhas_leituras,name='minhas_leituras'),
    path('nova_leitura',views.criar,name='nova_leitura'),
    path('minhas_leituras/<int:id_leituras>',views.detalhe,name='detalhe'),
    path('nova_leitura/<int:id_leituras>',views.editar,name='editar'),
    path('excluir_leitura/<int:id_leituras>',views.excluir,name='excluir'),
]

