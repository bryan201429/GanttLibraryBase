# from django.urls import include, re_path
# from . import views
# from rest_framework.urlpatterns import format_suffix_patterns
#
# urlpatterns = [
#     re_path(r'^$', views.index, name='index'),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('',views.index, name='index'),
    # path('forms/', views.forms, name='forms'),

    path('data/', views.data_list),

    path('data/task/', views.task_add, name='task_add'),
    path('data/task/<int:pk>', views.task_update, name='task_update'),
    path('data/link', views.link_add, name='link_add'),
    path('data/link/<int:pk>', views.link_update, name='link_update'),
]
urlpatterns = format_suffix_patterns(urlpatterns)