from django.shortcuts import render
from django.db.models import Value,F
from django.http import HttpResponse, HttpResponseRedirect
from .models import newuser, products, vote
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.


def startingpage(request):
    return render(request, "firstpage.html")


def signuppage(request):
    return render(request, "signuppage.html")


def loginpage(request):
    return render(request, "login.html")


def authentication(request):
    usernam = request.POST.get('username')
    passwordd = request.POST.get('passs')
    user = authenticate(request, username=usernam, password=passwordd)
    if user is not None:
        login(request, user)
        goto = reverse('listpage')
        return HttpResponseRedirect(goto)
    else:
        return render(request, "login.html", {"eror": "username or password is wrong"})


def chosenproductpage(request):
    return render(request, "chosenproductpage.html")


def vvote(request,pvote,uvote):
    theproduct=products.objects.all().filter(name=pvote)[0]
    if vote.objects.filter(product=uvote).exists():

        vote.objects.filter(product=uvote).update(count=F('count')+1)
        votecount=vote.objects.filter(product=uvote)[0]
        return render(request,"chosenproductpage.html",{ "vote": votecount.count, "product": pvote, "username": votecount.user})
    
    else:
        rate=vote.objects.create(product=theproduct,user=request.user)
        vote.objects.filter(product=uvote).update(count=F('count')+1)
        votecount=vote.objects.filter(product=uvote)
        return render(request,"chosenproductpage.html",{ "vote": votecount.count, "product": rate.product, "username": rate.user})


def signup(request):
    if request.method == 'POST':
        x_val = request.POST.get('username')
        y_val = request.POST.get('pass')
        if newuser.objects.filter(username=x_val).exists():
            return render(request, "signuppage.html", {'eror': 'user alredy exists'})
        else:
            user = newuser.objects.create(username=x_val)
            user.set_password(y_val)
            user.save()
            return render(request, 'login.html')


def productlist(request):
    if request.user.is_authenticated:
        queryset = products.objects.all()
        return render(request, 'productlistpage.html', {"product": list(queryset), "vote": vote.objects.all(), "e": Value(request.user)})
    else:
        return render(request, "login.html")
