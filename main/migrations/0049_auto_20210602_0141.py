# Generated by Django 3.1.3 on 2021-06-01 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_auto_20210602_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='oquurdisi',
            name='pdf',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='oquurdisi',
            name='pdf_title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='oquurdisi',
            name='word',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='oquurdisi',
            name='word_title',
            field=models.TextField(blank=True),
        ),
    ]
