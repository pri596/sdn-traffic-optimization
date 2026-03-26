from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)



from django.db import models

class NetworkData(models.Model):
    src_ip = models.CharField(max_length=20)
    dst_ip = models.CharField(max_length=20)
    protocol = models.IntegerField()            # 6=TCP, 17=UDP, 1=ICMP
    duration_ms = models.FloatField()           # flow duration in milliseconds
    packet_count = models.IntegerField()        # total packets in the flow
    bytes = models.BigIntegerField()            # total bytes transferred
    congestion_level = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.src_ip} → {self.dst_ip} ({self.congestion_level})"
