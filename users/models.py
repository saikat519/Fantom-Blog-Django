from PIL import Image
from django.db import models
from django.conf import settings
# Create your models here.
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    birth_day = models.DateField(null=True,blank=True)
    bio = models.TextField(max_length=1000,blank=True)
    image = models.ImageField(blank=True,null=True,default='users/default.png',upload_to='users')
    slug = models.SlugField(editable=False)
    
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args,**kwargs)


        img = Image.open(self.image.path)

        if img.height >200 or img.width >200:
            new_size=(200,200)
            img.thumbnail(new_size)
            img.save(self.image.path)

    def __str__(self):

        return self.user.username


def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile,sender=settings.AUTH_USER_MODEL)
