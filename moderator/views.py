from django.shortcuts import render, redirect
from submission.models import Confession
from moderator.models import Advert
from django.contrib.auth.decorators import login_required

def countFlags():
    flags = Confession.objects.all().filter(flag=True)
    return len(flags)

@login_required()
def index(request):
    confessions = Confession.objects.all()
    context = {'confessions': confessions, 'number': countFlags()}
    return render(request, 'moderator/index.html', context)

@login_required()
def approve(request, uuid):
    confession = Confession.objects.get(uuidField=uuid)
    confession.approved = True
    confession.save()
    return redirect('moderator:index')

@login_required()
def remove(request, uuid):
    confession = Confession.objects.get(uuidField=uuid)
    confession.delete()
    return redirect('moderator:index')

@login_required()
def approved(request):
    confessions = Confession.objects.all().filter(approved=True)
    context = {'confessions': confessions, 'number': countFlags()}
    return render(request, 'moderator/approved.html', context)


@login_required()
def pending(request):
    confessions = Confession.objects.all().filter(approved=False)
    context = {'confessions': confessions, 'number': countFlags()}
    return render(request, 'moderator/pending.html', context)

@login_required()
def flagged(request):
    flags = Confession.objects.all().filter(flag=True)
    number = len(flags)
    context = {'flags': flags, 'number': number}
    return render(request, 'moderator/flagged.html', context)

@login_required()
def adverts(request):
    adverts = Advert.objects.all()
    context = {'adverts': adverts, 'number': countFlags()}
    return render(request, 'moderator/adverts.html', context)
