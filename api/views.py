from typing import Any
from django.http import HttpResponse
from rest_framework.views import View
from datetime import datetime
from random import randrange
from django.shortcuts import render, redirect
from .repositories import ClassRepository
from .serializers import ClassSerializer
from .forms import ClassForm

MAIN_VIEW = 'Class View'

class ClassView(View):

    def __init__(self, **kwargs: Any) -> None:
        self.repository = ClassRepository(collection_name='classes')

    def get(self, request):
        repository = ClassRepository(collection_name='classes')
        classes = list(repository.get_all())
        serializer = ClassSerializer(data=classes, many=True)
        if (serializer.is_valid()):
            classes_data = serializer.data
            print(classes_data)
            return render(request, "home.html", {"classes": classes})
        else:
            return render(request, "home.html")
    
    def post(self, request):
        class_data = {
            "nome": request.POST.get("nome"),
            "responsavel": request.POST.get("responsavel"),
        }
        self.repository.insert(class_data)
        
        return redirect(MAIN_VIEW)

    def put(self, request):
        class_id = request.POST.get("class_id")
        class_data = {
            "nome": request.POST.get("nome"),
            "responsavel": request.POST.get("responsavel"),
        }
        query = {"_id": class_id}
        self.repository.update(query, class_data)
        return redirect(MAIN_VIEW)

    def delete(self, request):
        class_id = request.POST.get("class_id")
        query = {"_id": class_id}
        self.repository.delete(query)
        return redirect(MAIN_VIEW)


class ClassInsert(View):
    def get(self, request):
        class_form = ClassForm()

        return render(request, "add_class.html", {"form":class_form})
    
    def post(self, request):
        weather_form = ClassForm(request.POST)
        if weather_form.is_valid():
            serializer = ClassSerializer(data=weather_form.data)
            if (serializer.is_valid()):
                repository = ClassRepository(collection_name='classes')
                repository.insert(serializer.validated_data)
            else:
                print(serializer.errors)
        else:
            print(weather_form.errors)

        return redirect(MAIN_VIEW)
    
    
class ClassEdit(View):
  
  repository = ''
  
  def __init__(self,) -> None:
    self.repository = ClassRepository(collection_name='classes')
  
  def post(self, id, request):
      class_form = ClassForm(request.POST)
      if class_form.is_valid():
          serializer = ClassSerializer(data=class_form.data)
          if (serializer.is_valid()):
              repository = ClassRepository(collection_name='classes')
              repository.update(id, serializer.validated_data)
          else:
              print(serializer.errors)
      else:
          print(class_form.errors)

      return redirect(MAIN_VIEW)
  
  def get(self, request, id):
      class_data = self.repository.get_by_id(id)
      class_form = ClassForm(initial=class_data)
      return render(request, "edit_class.html", {"form":class_form, "obj_id": id})