from django.contrib import admin
from django.urls import path
from api.views import ClassView,  ClassInsert, ClassEdit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/salas/', ClassView.as_view(), name='Class View'),
    path('api/salas/criar/', ClassInsert.as_view(), name='Insert Class'),
    path('api/salas/<str:id>/atualizar/', ClassEdit.as_view(), name='Update Class')
]
