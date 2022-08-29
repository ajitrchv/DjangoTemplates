from audioop import reverse
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
   #   try:
        return HttpResponseRedirect(reverse('my_app:example'))
   #   except:
   #       return HttpResponse('Unable to redirect')