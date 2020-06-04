from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.shortcuts import render, HttpResponseRedirect



def Index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))


   


    
