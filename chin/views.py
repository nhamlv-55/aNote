#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, render, get_object_or_404
import urllib2
import re
import time
import csv

# Create your views here.
def chin(request):
	temp = "的"
	if request.GET.has_key('query'):
		temp=request.GET['query'].strip()
	variables = RequestContext(request, {
		'temp': temp,
		})
	return render_to_response(
		'chin_temp/chin.html',
		# {'user': request.user},
		variables
	)