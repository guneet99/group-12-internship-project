# Generated by Django 2.2.4 on 2020-10-06 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20201007_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calorie_Disturb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momday', models.CharField(blank=True, default='No', max_length=120, null=True)),
                ('tuesday', models.CharField(blank=True, default='No', max_length=120, null=True)),
                ('wednesday', models.CharField(blank=True, default='No', max_length=120, null=True)),
                ('thursday', models.CharField(blank=True, default='No', max_length=120, null=True)),
                ('friday', models.CharField(blank=True, default='No', max_length=120, null=True)),
                ('saturday', models.CharField(blank=True, default='No', max_length=120, null=True)),
                ('sunday', models.CharField(blank=True, default='No', max_length=120, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Calorie_Required',
        ),
    ]
