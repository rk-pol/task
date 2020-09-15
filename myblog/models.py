from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=250,blank=True, null=True)
	author = models.CharField(max_length=250,blank=True, null=True)
	dt_article = models.DateTimeField(auto_now_add=True)
	description = models.TextField(blank=True, null=True)
	short_description = models.CharField(max_length=120,blank=True, null=True)
	image = models.ImageField(upload_to='media/uploads/')
	published = models.DateTimeField(blank=True, null=True)
	created = models.DateTimeField(blank=True, null=True)
	updated = models.DateTimeField(blank=True, auto_now=True, null=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'

	def __str__(self):
		return '%s' %(self.title)
