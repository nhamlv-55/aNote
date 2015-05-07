from django.shortcuts import render

# Create your views here.
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
def moodring(request):

	return render_to_response(
		'moodring_temp/moodring.html',
	)