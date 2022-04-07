from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    View funtion for index page
    '''
    return render(request, 'reddit/index.html')
