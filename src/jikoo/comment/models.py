from django.db import models

from django.conf import settings

from post.models import Post

# Create your models here.


class Comment(models.Model):

	user 			=	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	target 			= 	models.ForeignKey(Post, on_delete = models.CASCADE)
	text	 		=	models.CharField(max_length = 5000, blank = True)
	photo 			= 	models.FileField(blank = True, null = True)
	video 			= 	models.FileField(blank = True, null = True)

	created_at 		= 	models.DateTimeField(auto_now_add = True)


	def __str__(self):
		return self.text



