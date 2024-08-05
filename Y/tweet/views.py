from django.shortcuts import render
from .models import tweet
from .forms import tweetform , UserRegisterationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# # Create your views here.
def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweets = tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = tweetform(request.POST , request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user= request.user
            tweet.save()
            return redirect('tweet:tweet_list')
    else:
        form = tweetform()
    return render(request,'tweet_form.html',{'form': form})

@login_required
def tweet_edit(request, tweet_id):
    Tweet = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = tweetform(request.POST , request.FILES, instance=Tweet)
        if form.is_valid():
            Tweet=form.save(commit=False)
            Tweet.user= request.user
            Tweet.save()
            return redirect('tweet:tweet_list')    
    else:
        form = tweetform(instance=Tweet)
    return render(request,'tweet_form.html',{'form': form})

@login_required
def tweet_delete(request, tweet_id):
    Tweet = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST' :
        Tweet.delete()
        return redirect('tweet:tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': Tweet})
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request , user)
            return redirect('tweet:tweet_list')
    else:
        form = UserRegisterationForm()

    return render(request, 'registration/register.html', {'form': form})
