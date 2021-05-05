from django.db import models

# Create your models here.
class Information(models.Model):
    address = models.CharField(max_length=300, blank=True)
    address_name = models.CharField(max_length=300, blank=True)
    facebook_info = models.CharField(max_length=300, blank=True)
    instagram_info = models.CharField(max_length=300, blank=True)
    whatsapp_info = models.CharField(max_length=300, blank=True)
    youtube_info = models.CharField(max_length=300, blank=True)
    email_info = models.CharField(max_length=300, blank=True)
    email_info_link = models.CharField(max_length=300, blank=True)
    phone_info1 = models.CharField(max_length=300, blank=True)
    phone_info1_link = models.CharField(max_length=300, blank=True)
    phone_info2 = models.CharField(max_length=300, blank=True)
    phone_info2_link = models.CharField(max_length=300, blank=True)
    partner_info1 = models.CharField(max_length=300, blank=True)
    partner_info1_link = models.CharField(max_length=300, blank=True)
    partner_info2 = models.CharField(max_length=300, blank=True)
    partner_info2_link = models.CharField(max_length=300, blank=True)
    partner_info3 = models.CharField(max_length=300, blank=True)
    partner_info3_link = models.CharField(max_length=300, blank=True)
    menu_info1 = models.CharField(max_length=300, blank=True)
    menu_info1_link = models.CharField(max_length=300, blank=True)
    menu_info2 = models.CharField(max_length=300, blank=True)
    menu_info2_link = models.CharField(max_length=300, blank=True)
    menu_info3 = models.CharField(max_length=300, blank=True)
    menu_info3_link = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return self.address

class Slider(models.Model):
    main_title = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='upload')
    mini_description = models.CharField(max_length=500, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)


    def __str__(self):
        return self.main_title


class Icon(models.Model):
    main_title = models.CharField(max_length=300, blank=True)
    description = models.CharField(max_length=500, blank=True)
    #icon = models.ImageField(upload_to='upload', blank=True)
    name = models.CharField(max_length=300, blank=True)
    title = models.CharField(max_length=300, blank=True)
    mini_description = models.CharField(max_length=500, blank=True)
    link = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class About(models.Model):
    # icon = models.ImageField(upload_to='upload', blank=True)
    logo = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=300, blank=True)
    count = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)


    def __str__(self):
        return self.name


class Specialty(models.Model):
    main_title = models.CharField(max_length=300, blank=True)
    mini_description = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    description = models.CharField(max_length=500, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0, blank=True)


    def __str__(self):
        return self.title

class Comentary(models.Model):
    photo = models.ImageField(upload_to='upload')
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    mini_description = models.CharField(max_length=500, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0, blank=True)


    def __str__(self):
        return self.last_name

class News(models.Model):
    title = models.CharField(max_length=300)
    mini_description = models.CharField(max_length=500, blank=True)
    photo1 = models.ImageField(upload_to='upload')
    photo2 = models.ImageField(upload_to='upload')
    photo3 = models.ImageField(upload_to='upload')
    name = models.CharField(max_length=300)
    date = models.IntegerField(default=0)
    description = models.CharField(max_length=500, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0, blank=True)


    def __str__(self):
        return self.title


class Register(models.Model):
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.last_name

class Galery(models.Model):
    name = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0, blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    photo = models.ImageField(upload_to='upload')
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    facebook = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, blank=True)
    whatsapp = models.CharField(max_length=300, blank=True)
    telegram = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    is_main = models.BooleanField(default=0, blank=True)

    def __str__(self):
        return self.last_name


class Baza(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Qabyldau(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Biliktilik(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=300)
    vide_link = models.CharField(max_length=300)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class KollejTarihi(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class License(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Acredatsiya(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Qurylym(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class OquAdisteme(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class AdistemelikKabinet(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class JasMaman(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Birlestikter(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Jetistikter(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Qashyqtyq(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class OquUrdisi(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class SabaqKeste(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class StudentJetistik(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Aqparat(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class JumysqaOrnalasu(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Seriktester(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Saualnama(models.Model):
    photo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    short_description = models.CharField(max_length=600, blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title




