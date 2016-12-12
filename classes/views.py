from django.shortcuts import render
from django.utils import timezone
import datetime

# Create your views here.
def classes_list(request):
	this_date = timezone.now()
	# classes = Class.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'classes/classes_list.html', {'currentdate':this_date})

def classes_detail(request):
	this_date = timezone.now()
	# classes = Class.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'classes/classes_detail.html', {'currentdate':this_date})