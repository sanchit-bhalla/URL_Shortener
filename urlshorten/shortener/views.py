from django.shortcuts import render,redirect
from .models import Url
from django.http import HttpResponse
import string,random
from django.conf import settings
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def shorten_url(request):
	response_data = {}
	if request.method == 'POST':
		http_url=request.POST.get('http_url')
		if request.POST.get('http_url'):
			val = URLValidator()
			try:
				val(http_url)
				try:
					http_url = Url.objects.get(http_url=http_url)
					short_id = http_url.short_id
				except:
					short_id=get_short_code()
					temp=Url(http_url=http_url,short_id=short_id)
					temp.save()
				response_data["f_url"]=http_url		
				response_data["url"]=settings.SITE_URL+"/"+short_id		
				return render(request=request,template_name='shortener/generated.html',context={'short_url':response_data["url"],'full_url':response_data["f_url"]})
			except ValidationError:
				e="Please enter a valid url."
				return render(request=request,template_name='shortener/index.html',context={'response_data':e})
	return render(request=request,template_name='shortener/index.html',context={'response_data':None})

def get_url(request,short_id):
	try:
		temp2=Url.objects.get(pk=short_id)
		url=temp2.http_url
		temp2.count=temp2.count+1
		temp2.save()
		return redirect(url)
	except:
		return HttpResponse("Error rendering")

def get_short_code():
	length=6
	char=string.ascii_uppercase + string.digits + string.ascii_lowercase
	while True:
		short_id = ''.join(random.choice(char) for x in range(length))
		try:
			temp1=Url.objects.get(pk=short_id)
		except:
			return short_id

#Some useful links
#http://www.learningaboutelectronics.com/Articles/How-to-insert-data-into-a-database-from-an-HTML-form-in-Django.php/
#url validation - https://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not