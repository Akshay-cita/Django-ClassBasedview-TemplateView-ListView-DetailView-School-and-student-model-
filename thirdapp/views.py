from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from thirdapp import models
# Create your views here.
# class cbview(View): #CLASS BASED VIEWS
#     def get(self,request):
#         return render(request,'first.html')
class IndexView(TemplateView):
    template_name='index.html'

class SchoolListView(ListView):
    context_object_name='schools'
    model=models.School
    template_name='school_list.html'



class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model=models.School
    template_name='school_details.html'
class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model=models.School
    template_name='school_form.html'

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model= models.School
    template_name='school_form.html'

class SchoolRemoveView(DeleteView):
    model=models.School
    success_url = reverse_lazy("basic_app:list")
    template_name='school_confirm_delete.html'
