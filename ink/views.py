from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Inkstains on my heart.....")
    context_dict = {'boldmessage': "that long to remain closed"}
    return render(request, 'ink/index.html', context_dict)
