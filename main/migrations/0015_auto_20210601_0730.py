# Generated by Django 3.1.3 on 2021-06-01 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210510_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='logo',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='acredatsiya',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='acredatsiya',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='adistemelikkabinet',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='adistemelikkabinet',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aqparat',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aqparat',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='baza',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='baza',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='biliktilik',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='biliktilik',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='birlestikter',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='birlestikter',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='icon',
            name='link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='icon',
            name='main_title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='icon',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='icon',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='address_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='email_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='email_info_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='facebook_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='instagram_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='knopka',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='knopka_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='menu_info1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='menu_info1_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='menu_info2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='menu_info2_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='menu_info3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='menu_info3_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='partner_info1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='partner_info1_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='partner_info2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='partner_info2_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='partner_info3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='partner_info3_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='phone_info1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='phone_info1_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='phone_info2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='phone_info2_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='whatsapp_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='youtube_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='jasmaman',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='jasmaman',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='jetistikter',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='jetistikter',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='jumysqaornalasu',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='jumysqaornalasu',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='karta',
            name='main_title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kollejtarihi',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kollejtarihi',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='languages',
            name='code',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='languages',
            name='extra_title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='languages',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='oquadisteme',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='oquadisteme',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='oquurdisi',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='oquurdisi',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='qabyldau',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='qabyldau',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='qashyqtyq',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='qashyqtyq',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='qurylym',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='qurylym',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sabaqkeste',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sabaqkeste',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='saualnama',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='saualnama',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='seriktester',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='seriktester',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='main_title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='main_title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='studentjetistik',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='studentjetistik',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='facebook',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='instagram',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='position',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='surname',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='telegram',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='whatsapp',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='transvalue',
            name='code',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='transvalue',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='vide_link',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Missiya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='upload')),
                ('title', models.TextField(blank=True)),
                ('short_description', models.TextField(blank=True)),
                ('status', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('lang', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='main.languages')),
            ],
        ),
    ]
