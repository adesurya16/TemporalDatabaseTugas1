from django.urls import path
from . import views

urlpatterns = [
    path('question', views.home, name="index"),
    path('entity', views.showentity, name="entity"),
    path('relational', views.showrelational, name="relational"),
    path('query', views.inputquery, name="query"),
    path('about', views.showabout, name="about"),
    path('question/<int:id>', views.index, name="question"),
]