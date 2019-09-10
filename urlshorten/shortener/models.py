from django.db import models

# Create your models here.
class Url(models.Model):
	short_id=models.SlugField(max_length=6,primary_key=True)
	http_url=models.URLField(max_length=200)
	publish_date=models.DateTimeField(auto_now=True)
	count=models.IntegerField(default=0)
	class Meta:
		verbose_name_plural="Urls"
	def __str__(self):
		return (self.http_url)