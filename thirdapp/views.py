from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,DetailView,TemplateView
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
