from django.db import models

class Blog(models.Model):
	blog_title = models.CharField(max_length=150)
	blog_url = models.CharField(max_length=150, null=True, blank=True)
	release_date = models.CharField(max_length=15)
	writer = models.CharField(max_length=100)
	blog_detail = models.TextField()
	# file will be uploaded to MEDIA_ROOT / images
	blog_photo = models.ImageField(upload_to ='uploads/', blank=True, 
	                               null=True, default='media/uploads/k8s.png')
    
	def __str__(self):
		return self.blog_title