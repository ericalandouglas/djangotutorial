from django.db import models
from django.conf import settings
from time import time

# Create your models here.

def get_upload_file_name(instance, filename):
	#return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)
	return settings.UPLOAD_FILE_PATTERN % (str(time()).replace('.', '_'), filename)

class Article(models.Model):

	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)
	thumbnail = models.FileField(upload_to=get_upload_file_name)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/articles/get/%i/" % self.id

	def get_thumbnail(self):
		thumb = str(self.thumbnail)
		if not settings.DEBUG:
			thumb = thumb.replace('assets/', '')
		return thumb

class Comment(models.Model):
	
	first_name = models.CharField(max_length=200)
	second_name = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	article = models.ForeignKey(Article)
