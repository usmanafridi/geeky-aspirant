from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100, blank=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} - {self.subscribed_at}'


class Feedback(models.Model):
    feedback = models.TextField(default=None)
    name = models.CharField(max_length=255, default=None)
    subject = models.CharField(max_length=300, default=None)
    email = models.EmailField(default=None)
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.commented_at}'
