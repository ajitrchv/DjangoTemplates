from audioop import reverse
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    # try:
        return HttpResponseRedirect(reverse('example'))
    # except:
    #     return HttpResponse('Unable to redirect')