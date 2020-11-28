from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to = 'user_images')

	def __str__(self):
		return f'Создан профиль {self.user.username}'

	def save(self):
		super().save()

		image = Image.open(self.image.path)

		if image.height > 256 or image.width > 256:
			resize = (256, 256)
			image.thumbnail(resize)
			image.save(self.image.path)
