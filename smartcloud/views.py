#!/usr/bin/python
#coding:utf-8

from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

import sys 
sys.path.append("..")
#from log.log import MessageLog
#LOG = MessageLog("/var/log/smartcloud/smartcloud.log")

def home(request):
	return render_to_response('index.html',RequestContext(request))

def getHtml(request,arg):
#	try:
		url=request.path
		url=url[1:]
		return render_to_response(url,RequestContext(request))
#	except Exception,e:
#		LOG.INFO("template does not exist!!")
#		raise Http404
