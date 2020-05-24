from django.urls import path 
from snippets import views


# http://127.0.0.1:8000/snippets/2/

urlpatterns = [
    path('snippets/all', views.snippet_list),
    path('snippets/<int:snippet_id>/', views.snippet_detail),
]
