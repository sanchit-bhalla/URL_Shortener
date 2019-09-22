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

# auto_now - 	 updates the value of field to current time and date every time the Model.save() is called.
# auto_now_add - updates the value with the time and date of creation of record.

# URLField is used to store URL, where as SlugField is used to store a alphanumeric/varchar value that relates to the title or some description of the model.
# Example
# URL - https://clipmyurl.herokuapp.com/jvitMr
# slug - jvitMr 