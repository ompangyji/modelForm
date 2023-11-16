from django.urls import path
from . import views

app_name = 'articles'

#유지보수랑 재사용을 위해서 아래와 같은 방식으로 작성한다.
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/update/', views.update, name='update'),
]