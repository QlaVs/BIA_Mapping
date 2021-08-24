from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_new/', add_new, name='add'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
    path('json/', get_json, name='get_json'),
    path('json/<int:pk>', get_json, name='get_json'),
    path('json/user', get_specific_user, name='specific_user'),
    path('mass_redact/', mass_redact, name='mass_redact'),
    path('add_city/', add_new_city, name='add_new_city'),
    path('add_ac/', add_new_ac, name='add_new_ac'),
    path('add_user/', add_new_user, name='add_new_user'),

    # path('delete_instance/', delete_city, name='delete_city'),
    # path('delete_instance/', delete_ac, name='delete_ac'),
    # path('delete_instance/', delete_user, name='delete_user'),
    # path('parse/', parse, name='parse')
]
