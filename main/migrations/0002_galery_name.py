# Generated by Django 3.1.3 on 2021-05-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galery',
            name='name',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]