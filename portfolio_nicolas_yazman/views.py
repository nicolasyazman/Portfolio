from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git

@csrf_exempt
def update_server(request):
    repo = git.Repo('Portfolio')
    origin = repo.remotes.origin
    origin.pull()
    return HttpResponse('Updated Server with the latest Git code')

@csrf_exempt
def home_page(request):
    return HttpResponse('Home page. Hello world and welcome!')
