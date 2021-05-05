from django.contrib import admin
from main.models import *

# Register your models here.

class InformationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Information, InformationAdmin)


class SliderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Slider, SliderAdmin)



class IconAdmin(admin.ModelAdmin):
    pass
admin.site.register(Icon, IconAdmin)


class AboutAdmin(admin.ModelAdmin):
    pass
admin.site.register(About, AboutAdmin)



class SpecialtyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Specialty, SpecialtyAdmin)



class ComentaryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comentary, ComentaryAdmin)


class NewsAdmin(admin.ModelAdmin):
    pass
admin.site.register(News, NewsAdmin)


class KartaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Karta, KartaAdmin)



class RegisterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Register, RegisterAdmin)



class GaleryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Galery, GaleryAdmin)



class TeacherAdmin(admin.ModelAdmin):
    pass
admin.site.register(Teacher, TeacherAdmin)



class BazaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Baza, BazaAdmin)


class QabyldauAdmin(admin.ModelAdmin):
    pass
admin.site.register(Qabyldau, QabyldauAdmin)



class BiliktilikAdmin(admin.ModelAdmin):
    pass
admin.site.register(Biliktilik, BiliktilikAdmin)


class VideoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Video, VideoAdmin)



class KollejTarihiAdmin(admin.ModelAdmin):
    pass
admin.site.register(KollejTarihi, KollejTarihiAdmin)


class LicenseAdmin(admin.ModelAdmin):
    pass
admin.site.register(License, LicenseAdmin)



class AcredatsiyaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Acredatsiya, AcredatsiyaAdmin)



class QurylymAdmin(admin.ModelAdmin):
    pass
admin.site.register(Qurylym, QurylymAdmin)



class OquAdistemeAdmin(admin.ModelAdmin):
    pass
admin.site.register(OquAdisteme, OquAdistemeAdmin)



class AdistemelikKabinetAdmin(admin.ModelAdmin):
    pass
admin.site.register(AdistemelikKabinet, AdistemelikKabinetAdmin)



class JasMamanAdmin(admin.ModelAdmin):
    pass
admin.site.register(JasMaman, JasMamanAdmin)



class BirlestikterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Birlestikter, BirlestikterAdmin)


class JetistikterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Jetistikter, JetistikterAdmin)


class QashyqtyqAdmin(admin.ModelAdmin):
    pass
admin.site.register(Qashyqtyq, QashyqtyqAdmin)


class OquUrdisiAdmin(admin.ModelAdmin):
    pass
admin.site.register(OquUrdisi, OquUrdisiAdmin)


class SabaqKesteAdmin(admin.ModelAdmin):
    pass
admin.site.register(SabaqKeste, SabaqKesteAdmin)


class StudentJetistikAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentJetistik, StudentJetistikAdmin)


class AqparatAdmin(admin.ModelAdmin):
    pass
admin.site.register(Aqparat, AqparatAdmin)


class JumysqaOrnalasuAdmin(admin.ModelAdmin):
    pass
admin.site.register(JumysqaOrnalasu, JumysqaOrnalasuAdmin)


class SeriktesterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Seriktester, SeriktesterAdmin)


class SaualnamaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Saualnama, SaualnamaAdmin)