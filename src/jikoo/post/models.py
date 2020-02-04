from django.db import models
from django.conf import settings









class Post(models.Model):

	user 			=	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	text 			= 	models.CharField(max_length = 5000, blank = True, null = True)
	photo 			= 	models.FileField(blank = True, null = True)
	video 			= 	models.FileField(blank = True, null = True)

	created_at 		= 	models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.text


	def parse_hashtag(self):
		pass


	def parse_mention(self):
		pass




