from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    user=models.OneToOneField(to=User,on_delete=models.CASCADE,related_name="userprofile")
    picture=models.ImageField(default='profile_pics/default.png',upload_to='profile_pics')

    def __str__(self):
        return self.user.username




# Signal to create profile automatically after user creation

def create_profile_for_user(sender, instance, created, *args, **kwargs):
    if created:
        Profile(user=instance).save()
    else:
        pass

post_save.connect(create_profile_for_user,sender=User)
