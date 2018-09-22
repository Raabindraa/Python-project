from django.urls import path

from polls import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('blog', views.ourblog, name='blog'),
    path('home', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('showDate',views.date,name='date'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/detail', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
