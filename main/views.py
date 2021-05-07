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


def QabyldauHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    qabyldau = Qabyldau.objects.filter(status=0).order_by('-rating')

    return render(request, 'qabyldau.html', {
        'informations': informations,
        'galerys': galerys,
        'qabyldau': qabyldau
    })




def BiliktilikHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    biliktilik = Biliktilik.objects.filter(status=0).order_by('-rating')

    return render(request, 'biliktilik.html', {
        'informations': informations,
        'galerys': galerys,
        'biliktilik': biliktilik
    })



def LicenseHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    license = License.objects.filter(status=0).order_by('-rating')

    return render(request, 'license.html', {
        'informations': informations,
        'galerys': galerys,
        'license': license
    })


def AcredatsiyaHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    acredatsiya = Acredatsiya.objects.filter(status=0).order_by('-rating')

    return render(request, 'acredatsiya.html', {
        'informations': informations,
        'galerys': galerys,
        'acredatsiya': acredatsiya
    })


def QurylymHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    qurylym = Qurylym.objects.filter(status=0).order_by('-rating')

    return render(request, 'qurylym.html', {
        'informations': informations,
        'galerys': galerys,
        'qurylym': qurylym
    })


def OquAdistemeHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    adisteme = OquAdisteme.objects.filter(status=0).order_by('-rating')

    return render(request, 'oqu-adisteme.html', {
        'informations': informations,
        'galerys': galerys,
        'adisteme': adisteme
    })



def AdistemelikKabinetHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    kabinet = AdistemelikKabinet.objects.filter(status=0).order_by('-rating')

    return render(request, 'adisteme-kabineti.html', {
        'informations': informations,
        'galerys': galerys,
        'kabinet': kabinet
    })


def JasMamanHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    maman = JasMaman.objects.filter(status=0).order_by('-rating')

    return render(request, 'jas-maman.html', {
        'informations': informations,
        'galerys': galerys,
        'maman': maman
    })


def BirlestikHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    birlestik = Birlestikter.objects.filter(status=0).order_by('-rating')

    return render(request, 'birlestik.html', {
        'informations': informations,
        'galerys': galerys,
        'birlestik': birlestik
    })

def JetistikHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    jetistik = Jetistikter.objects.filter(status=0).order_by('-rating')


    return render(request, 'jetistik.html', {
        'informations': informations,
        'galerys': galerys,
        'jetistik': jetistik
    })


def OquHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    oqu = Qashyqtyq.objects.filter(status=0).order_by('-rating')


    return render(request, 'oqu.html', {
        'informations': informations,
        'galerys': galerys,
        'oqu': oqu
    })


def OquUrdisiHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    oqu = OquUrdisi.objects.filter(status=0).order_by('-rating')


    return render(request, 'oqu-urdisi.html', {
        'informations': informations,
        'galerys': galerys,
        'oqu': oqu
    })


def KesteHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    keste = SabaqKeste.objects.filter(status=0).order_by('-rating')


    return render(request, 'keste.html', {
        'informations': informations,
        'galerys': galerys,
        'keste': keste
    })


def StudentHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    student = StudentJetistik.objects.filter(status=0).order_by('-rating')


    return render(request, 'student.html', {
        'informations': informations,
        'galerys': galerys,
        'student': student
    })



def AqparatHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    aqparat = Aqparat.objects.filter(status=0).order_by('-rating')


    return render(request, 'aqparat.html', {
        'informations': informations,
        'galerys': galerys,
        'aqparat': aqparat
    })


def JumysqaOrnalasuHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    jumys = JumysqaOrnalasu.objects.filter(status=0).order_by('-rating')


    return render(request, 'jumysqa-ornalasu.html', {
        'informations': informations,
        'galerys': galerys,
        'jumys': jumys
    })


def PartnerHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    partner = Seriktester.objects.filter(status=0).order_by('-rating')


    return render(request, 'partner.html', {
        'informations': informations,
        'galerys': galerys,
        'partner': partner
    })


def SaualnamaHandler(request):
    informations = Information.objects.all()
    galerys = Galery.objects.filter(status=0).order_by('-rating').filter(is_main=True)
    saualnama = Saualnama.objects.filter(status=0).order_by('-rating')


    return render(request, 'saualnama.html', {
        'informations': informations,
        'galerys': galerys,
        'saualnama': saualnama
    })