# Generated by Django 2.2.4 on 2020-10-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20201002_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=120),
        ),
    ]
