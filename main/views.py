from django.http import JsonResponse
from django.shortcuts import render
from main.models import Information, Slider, Icon, About, Specialty, Comentary, News, Register, Galery
from main.models import Teacher, Baza, Qabyldau, Biliktilik, Video, KollejTarihi, License, Acredatsiya, Karta
from main.models import Qurylym, OquAdisteme, AdistemelikKabinet, JasMaman, Birlestikter, Jetistikter, Qashyqtyq
from main.models import OquUrdisi, SabaqKeste, StudentJetistik, Aqparat, JumysqaOrnalasu, Seriktester, Saualnama
import math

# Create your views here.

def indexHandler(request):
    if request.method == 'GET':
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


    else:
        r = Register()
        last_name = request.POST.get('last_name', '')
        first_name = request.POST.get('first_name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')


        r.last_name = last_name
        r.phone = phone
        r.first_name = first_name
        r.message = message
        r.save()

        return JsonResponse({'success': True, 'errorMsg': '', '_success': True})



def NewsDetailHandler(request, news_id):
    news_items = News.objects.get(id=int(news_id))

    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    news = News.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    return render(request, 'news-detail.html', {
        'news': news,
        'news_items': news_items,
        'informations': informations,
        'galerys': galerys
    })



def SpecialtyDetailHandler(request, specialty_id):
    specialty_items = Specialty.objects.get(id=int(specialty_id))

    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    specialtys = Specialty.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    return render(request, 'specialty-detail.html', {
        'specialty_items': specialty_items,
        'informations': informations,
        'galerys': galerys,
        'specialtys': specialtys
    })


def CourseHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    specialtys = Specialty.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    return render(request, 'courses.html', {
        'informations': informations,
        'galerys': galerys,
        'specialtys': specialtys
    })


def TeacherHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    teachers = Teacher.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    return render(request, 'teacher.html', {
        'informations': informations,
        'galerys': galerys,
        'teachers': teachers
    })


def AboutHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    about = KollejTarihi.objects.filter(status=0).order_by('-rating')

    return render(request, 'about.html', {
        'informations': informations,
        'galerys': galerys,
        'about': about
    })



def BazaHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    baza = Baza.objects.filter(status=0).order_by('-rating')

    return render(request, 'baza.html', {
        'informations': informations,
        'galerys': galerys,
        'baza': baza
    })



def VideoHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    video = Video.objects.filter(status=0).order_by('-rating')

    return render(request, 'video.html', {
        'informations': informations,
        'galerys': galerys,
        'video': video
    })