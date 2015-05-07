from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response, render, get_object_or_404
from rotten.forms import *
import urllib2
import re
import time
import csv
import os


def search(request):
    query = request.GET.get('query')
    if query:
        # There was a query entered.
        results = SomeModel.objects.filter(somefield=query)
    else:
        # If no query was entered, simply return all objects
        results = SomeModel.objects.all()
    return render(request, 'search.html', {'results': results})



# --------------------------------------
def json_handling(content):
	results =[]
	pattern = r'"id":"[0-9]+",["]title["]:["][^"]+["]'
	# regex = re.compile(pattern)
	raw_results = re.findall(pattern, content)
	for r in raw_results:
		x = r[6:-1]
		x= x.split('","title":"')
		
		results.append(x)
	return results

def find(query, no_of_item):
	name = "+".join(query.split())
	results=[]
	no_of_loops = no_of_item/50+1
	url="http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=tgqqv4k8s86yufchv23st4f7&page_limit=50"
	url+="&q="+name
	i=0
	while i < no_of_loops:
		try:
			response = urllib2.urlopen(url+"&page="+str(i+1))
			content = response.read()
			results.extend(json_handling(content))
			i+=1
		except:
			time.sleep(50.0/1000.0)
	return results[:no_of_item]

def find_last_fm(query, no_of_item):
	name = "+".join(query.split())
	results=[]
	no_of_loops = no_of_item/50+1
	base_url="http://ws.audioscrobbler.com/2.0/?method=album.search&album="
	tale = "&api_key=b5712a5d3cabe3a63b2cb666cc14d61a&format=json"
	url=base_url+name+tale
	i=0
	while i < no_of_loops:
		try:
			response = urllib2.urlopen(url+"&page="+str(i+1))
			content = response.read()
			# results.extend(json_handling(content))
			i+=1
		except:
			time.sleep(50.0/1000.0)
	return content


# ---------------------DEV------------------------------
def rotten_page_dev(request):
	form = SearchForm()
	show_results = True
	results = []
	content = "c"
	if request.GET.has_key('query'):
		query = request.GET['query'].strip()
		if query:
			form = SearchForm({'query': query})
			results=find(query, 10)
			
	variables = RequestContext(request, {
		'form': form,
		'results': results,
		# 'content': str(content)
		})
	return render_to_response('rotten_dev.html', variables)



def rotten_similar_dev(request, id):
	base_url = "http://api.rottentomatoes.com/api/public/v1.0/movies/"
	type_url = "/similar.json?apikey=tgqqv4k8s86yufchv23st4f7"
	query_url = base_url+str(id)+type_url
	variables = RequestContext(request, {
		'url': str(query_url),
		'id': id,
		'status': "panel1"
		})
	return render_to_response('rotten_similar_dev.html', variables)
