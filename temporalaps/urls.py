from django.urls import path
from . import views

urlpatterns = [
    path('question', views.home, name="index"),
    path('entity', views.showentity, name="entity"),
    path('relational', views.showrelational, name="relational"),
    path('query', views.inputquery, name="query"),
    path('about', views.showabout, name="about"),
    path('question/<int:id>', views.index, name="question"),
    path('answer/<int:id>', views.answerquestion, name="answer"),
    path('project/<int:id>', views.insertProject, name="insert"),
    path('project/update/<int:id>', views.updateProject, name="update"),
    path('answer/<int:id>',views.answerquestion, name="answer"),
    path('insert/anggota', views.insertAnggota, name="insertanggota"),
]