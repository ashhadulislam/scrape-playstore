from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import generic
from django.template import loader

# from . import scripts

#to serve files as download
from django.views.static import serve


from .scripts import scripts
import os

def index(request):
    # template = loader.get_template('app_reviews/index.html')
    # return HttpResponse(None,template.render( request))
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'app_reviews/index.html')


def get_reviews(request):
	
	if request.POST["app_url"]=="":
		url="blanks"
	else:
		url=str(request.POST["app_url"])

	if request.POST["stop_words"]=="":
		stop_words=None
	else:
		stop_words=[x.strip() for x in request.POST['stop_words'].split(',')]
	print('stop_words',stop_words)

	print("data is",url)
	word_cloud_image_location=None
	status,xls_name,word_cloud_image_location=scripts.get_reviews(url,stop_words)
	print("After processing reviews ",status,xls_name,word_cloud_image_location)
	# status,xls_name=scripts.get_reviews(url,stop_words)
	if status == False:
		result_string="Sorry, process failed"
	else:
		result_string="Extracted succesfully"
		reviews_csv=xls_name
		wc_img_url=word_cloud_image_location
		print(wc_img_url , " is it there? ", os.path.exists(wc_img_url))
		context = {'result_string': result_string, 'reviews_csv':reviews_csv,'word_cloud_image_url':wc_img_url}
		#return the excel file
		# return serve(request, os.path.basename(xls_name), os.path.dirname(xls_name))
		return render(request, 'app_reviews/index.html',context)


	# result_placeholder="<div>"+result_string+"</div>"
	# print(result_string)
	# context = {'result_string': result_string}
	# return render(request, 'app_reviews/index.html',context)

def get_reviews_csv(request):
	if request.POST["reviews_csv"]=="":
		xls_name="blanks"
		return render(request, 'app_reviews/index.html',None)
	else:
		xls_name=str(request.POST["reviews_csv"])
		print("File is at ", xls_name)
		return serve(request, os.path.basename(xls_name), os.path.dirname(xls_name))





# class IndexView(generic.ListView):
#     # template = loader.get_template('app_reviews/index.html')
#         # context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return "hello"
