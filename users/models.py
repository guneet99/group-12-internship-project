from django.db import models
from django.contrib.auth.models import User
from PIL import Image

Activity_Choice = (
    ('Sedentary','Sedentary'),
    ('Lightly Active', 'Lightly Active'),
    ('Moderately Active','Moderately Active'),
    ('Very Active','Very Active'),
    ('Extra Active','Extra Active'),
)
Gender=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    height=models.CharField(max_length=120,null=True,blank=True)
    weight=models.CharField(max_length=120,null=True,blank=True)
    activity=models.CharField(max_length=120,choices=Activity_Choice,default='Sedentary')
    contact=models.CharField(max_length=120,null=True,blank=True)
    age=models.CharField(max_length=120,null=True,blank=True)
    first_name=models.CharField(max_length=120,null=True,blank=True)
    last_name=models.CharField(max_length=120,null=True,blank=True)
    gender=models.CharField(max_length=120,choices=Gender,default='Male')
    # activity_type=models.CharField(max_length=120,null=True,blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Alert_Button(models.Model):
    alert_button=models.CharField(max_length=120,null=True,blank=True,default="on")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}_alert_status'


class Calorie_Intake(models.Model):
	monday=models.CharField(max_length=120,null=True,blank=True,default='0')
	tuesday=models.CharField(max_length=120,null=True,blank=True,default='0')
	wednesday=models.CharField(max_length=120,null=True,blank=True,default='0')
	thursday=models.CharField(max_length=120,null=True,blank=True,default='0')
	friday=models.CharField(max_length=120,null=True,blank=True,default='0')
	saturday=models.CharField(max_length=120,null=True,blank=True,default='0')
	sunday=models.CharField(max_length=120,null=True,blank=True,default='0')
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	# author = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return f'{self.user.username}_calorie_intake'



class Calorie_Disturb(models.Model):
	monday=models.CharField(max_length=120,null=True,blank=True,default='no')
	tuesday=models.CharField(max_length=120,null=True,blank=True,default='no')
	wednesday=models.CharField(max_length=120,null=True,blank=True,default='no')
	thursday=models.CharField(max_length=120,null=True,blank=True,default='no')
	friday=models.CharField(max_length=120,null=True,blank=True,default='no')
	saturday=models.CharField(max_length=120,null=True,blank=True,default='no')
	sunday=models.CharField(max_length=120,null=True,blank=True,default='no')
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	# author = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return f'{self.user.username}_calorie_disturb'