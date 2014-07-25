from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

import logging
logr = logging.getLogger(__name__)

# Create your models here.

class UserProfile(models.Model):

	user = models.OneToOneField(User)
	likes_cheese = models.BooleanField(default=False)
	favorite_hamster_name = models.CharField(max_length=50)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0]) # create profiles as needed

@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kwargs):
	if kwargs.get('created', False):
		up = UserProfile.objects.create(user=kwargs.get('instance'))
		logr.debug("UserProfile created: %s" % up)
