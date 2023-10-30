from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Property(models.Model):
    name = models.CharField(max_length=50)
    profiles = models.ManyToManyField(
        'Profile',
        through='Residence',
        through_fields=('property', 'profile'),
    )
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    properties = models.ManyToManyField(
        Property,
        through='Residence',
        through_fields=('profile', 'property'),
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Meter(models.Model):
    name = models.CharField(max_length=50)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Residence(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return(self.property.__str__() + ', ' + self.profile.user.__str__())

class Reading(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=3) # cubic meter
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)
