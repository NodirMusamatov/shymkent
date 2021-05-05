from django.http import JsonResponse
from django.shortcuts import render
from main.models import Information, Slider, Icon, About, Specialty, Comentary, News, Register, Galery
from main.models import Teacher, Baza, Qabyldau, Biliktilik, Video, KollejTarihi, License, Acredatsiya, Karta
from main.models import Qurylym, OquAdisteme, AdistemelikKabinet, JasMaman, Birlestikter, Jetistikter, Qashyqtyq
from main.models import OquUrdisi, SabaqKeste, StudentJetistik, Aqparat, JumysqaOrnalasu, Seriktester, Saualnama
import math

# Create your views here.

def indexHandler(request):
    informations = Information.objects.all()
    sliders = Slider.objects.filter(status=0).order_by('-rating')
    icons = Icon.objects.filter(status=0).order_by('-rating')
    abouts = About.objects.filter(status=0).order_by('-rating')
    specialtys = Specialty.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    comentarys = Comentary.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    news = News.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    kartas = Karta.objects.all()

    return render(request, 'index.html', {
        'informations': informations,
        'sliders': sliders,
        'icons': icons,
        'abouts': abouts,
        'specialtys': specialtys,
        'comentarys': comentarys,
        'news': news,
        'galerys': galerys,
        'kartas': kartas
    })