from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.signup),
    path('registration/', views.registration),
    path('login/', views.login),
    path('login_data/', views.login_form),
    path('table/', views.table),
    path('update_view/<int:uid>/', views.update_view),
    path('update_form_data/', views.update_form_data),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name="delete")
]
