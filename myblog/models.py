from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
	#ForeignKey = di gunakan untuk link ke model yang lain
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

#models.Model digunakan untuk menandakan bahwa class Post adalah django Model, yang isinya akan di simpan ke database

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

#__str__ di gunakan untuk mengambil string (str) dalam kasus ini title

