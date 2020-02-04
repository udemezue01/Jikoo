from django.db import models
from post.models import Post



class Hashtag(models.Model):

	title 		 = 	models.CharField(max_length = 3000)
	post 		 = 	models.ManyToManyField(Post)

	def __str__():
		return self.title




