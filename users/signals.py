from users.models import Profile
from django.db.models.signals import post_save, post_delete
import django.dispatch
from django.contrib.auth.models import User

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
        )


post_save.connect(receiver=createProfile, sender=User)

