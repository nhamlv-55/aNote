from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, render, get_object_or_404
from elmusico.forms import *
import urllib2
import re
import time
import csv
import os



def zhing(request):
	# proxy = "115.79.35.108:3128"
	# proxyHandler = urllib2.ProxyHandler({'http': '115.79.35.1087:3128'})
	# opener = urllib2.build_opener(proxyHandler)
	# urllib2.install_opener(opener)

	respond = urllib2.urlopen("http://mp3.zing.vn")

	return render_to_response('base_pakdd.html')