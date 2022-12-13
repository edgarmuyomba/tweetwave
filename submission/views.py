from django.shortcuts import render, redirect
from .models import Confession

def index(request):
    context = {}
    return render(request, 'submission/index.html', context)

def saved(request):
    if request.method == 'POST':
        tweet = request.POST['tweet']
        try:
            media = request.FILES['attachment']
        except:
            media = None
        newTweet = Confession(text=tweet, media=media)
        newTweet.save()
        return redirect('submission:index')

