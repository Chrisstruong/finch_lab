from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"#connect to html

class About(TemplateView):
    template_name = "about.html"

# class Dog:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio

# dogs = [
#     Dog("Dog1", "https://images.unsplash.com/photo-1517849845537-4d257902454a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1035&q=80",
#           "Gorillaz are once again disrupting the paradigm and breaking convention in their round the back door fashion with Song Machine, the newest concept from one of the most inventive bands around."),
#     Dog("Dog2",
#           "https://images.unsplash.com/photo-1561037404-61cd46aa615b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80", "Welcome 👋 The Amazing Beebo was working on a new bio but now he's too busy taking over the world."),
#     Dog("Dog3", "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2069&q=80",
#           "Joji is one of the most enthralling artists of the digital age. New album Nectar arrives as an eagerly anticipated follow-up to Joji's RIAA Gold-certified first full-length album BALLADS 1, which topped the Billboard R&B / Hip-Hop Charts and has amassed 3.6B+ streams to date."),
# ]

class DogList(TemplateView):
    template_name = "dog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["dogs"] = Dog.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["dogs"] = Dog.objects.all()
            context["header"] = "Trending Dogs"
        return context

class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'img', 'bio', 'verified_dog']
    template_name = 'dog_create.html'
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})

class DogDetail(DetailView):
    model = Dog
    template_name = 'dog_detail.html'


class DogUpdate(UpdateView):
    model = Dog
    fields = ['name','img', 'bio', 'verified_dog']
    template_name = 'dog_update.html'
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk':self.object.pk})
    

class DogDelete(DeleteView):
    model = Dog
    template_name = 'dog_delete_confirmation.html'
    success_url = '/dogs/'
