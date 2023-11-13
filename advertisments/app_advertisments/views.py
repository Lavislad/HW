from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Advertisement
from .forms import AdvertisementsForm
from django.db.models import Count

#Функции для ссылок
def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements, 'title': title}
    return render(request, 'app_advertisments/index.html', context)

def top_sellers(request):
    users = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context = {
        'users': users,
    }
    return render(request, 'app_advertisments/top-sellers.html')

def register(request):
    return render(request, 'app_auth/register.html')

def advertisement_post(request):
    form = AdvertisementsForm()
    if request.method == 'POST':
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            advertisements = Advertisement(**form.cleaned_data)
            advertisements.user = request.user
            advertisements.save()
            #url = reverse('main-page')
            return redirect('main-page')
    context = {'form': form}
    return render(request, 'app_advertisments/advertisement-post.html', context)

def advertisement(request):
    return render(request, 'app_advertisments/advertisement.html')

def login(request):
    return render(request, 'app_auth/login.html')

def profile(request):
    return render(request, 'app_auth/profile.html')

def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {
        'advertisement': advertisement
    }
    return render(request, 'app_advertisments/advertisement.html', context)
