from django.shortcuts import render
from . import models
from django.views.generic import TemplateView,CreateView,ListView,FormView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from . forms import UserForm,AddPersonForm,AddDietForm,DetailForm
from django.views import View
from .models import User,Diet,Day
from django.urls import reverse_lazy

class IndexPage(FormView):
    template_name = "diet/index.html"
    form_class = UserForm
    success_url=None

    def form_valid(self,form):
        name=form.cleaned_data['name']
        day = int(form.cleaned_data['day'])
        return redirect('view_page',name=name,day=day)
    

class NewPersonPage(CreateView):
    template_name = "diet/new_person.html"
    form_class = AddPersonForm
    success_url = reverse_lazy('index')

class DietForm(CreateView):
    template_name='diet/add_diet.html'
    form_class = AddDietForm
    success_url = reverse_lazy('index')

class DetailForm(CreateView):
    template_name="diet/add_details.html"
    form_class = DetailForm
    success_url = reverse_lazy('index')

class ViewPage(DetailView):
    template_name = "diet/view_page.html"
    model = Day


    






    


# Create your views here.
