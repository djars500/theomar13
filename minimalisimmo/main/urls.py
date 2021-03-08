from django.urls import path
from . import views
urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path("<slug:url>/", views.Article_List.as_view(),name="article_list"),
    path('article/<slug:url>/', views.ArticleDetail.as_view(), name='article_detail')

]

