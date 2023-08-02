from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

class Post(models.Model):
	title = models.CharField(max_length=100,blank=True)
	file = models.FileField(null=True,blank=True,upload_to='Files')
	content = models.CharField(max_length=100,blank=True)
	allow=models.CharField(null=True,blank=True,max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})




# timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
        
# class Alert(models.Model):
# 	content = models.CharField(max_length=100)
# 	date_changed = models.DateTimeField(default=timezone.now)
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.content
