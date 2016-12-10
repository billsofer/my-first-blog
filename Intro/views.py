from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
import datetime



# Create your views here.

def intro(request):
	this_date = timezone.now()
	context = {'currentdate':this_date}
	return render(request, 'intro_more.html', context)
