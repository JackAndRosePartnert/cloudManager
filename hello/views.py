# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response

def hello(request):
    return render_to_response("hello.html",RequestContext(request))
