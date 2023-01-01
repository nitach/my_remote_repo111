from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from testapp.models import Beer
from django.urls import reverse_lazy

# Create your views here.
class BeerListView(ListView):
    model=Beer

class BeerDetailView(DetailView):
    model=Beer

class BeerCreateView(CreateView):
    model=Beer
    fields='__all__'

class BeerUpdateView(UpdateView):
    model=Beer
    fields=['color','taste','Brand']

class BeerDeleteView(DeleteView):
    model=Beer
    success_url=reverse_lazy('list')

