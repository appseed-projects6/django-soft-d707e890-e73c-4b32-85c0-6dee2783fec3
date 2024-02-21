# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Userpreferences(models.Model):

    #__Userpreferences_FIELDS__
    dark_mode = models.CharField(max_length=255, null=True, blank=True)

    #__Userpreferences_FIELDS__END

    class Meta:
        verbose_name        = _("Userpreferences")
        verbose_name_plural = _("Userpreferences")


class Userextra(models.Model):

    #__Userextra_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__Userextra_FIELDS__END

    class Meta:
        verbose_name        = _("Userextra")
        verbose_name_plural = _("Userextra")



#__MODELS__END
