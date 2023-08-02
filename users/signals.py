from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,Calorie_Disturb,Calorie_Intake,Alert_Button


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_Alert_Button(sender, instance, created, **kwargs):
    if created:
        Alert_Button.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_calorie_disturb(sender, instance, created, **kwargs):
    if created:
        Calorie_Disturb.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_calorie_intake(sender, instance, created, **kwargs):
    if created:
        Calorie_Intake.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()


