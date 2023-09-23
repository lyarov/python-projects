from django.db import models
from django.contrib.auth.models import User
# Create your models here.


CARD_TYPE_CHOICES = (('Student', 'Student'), ('Common', 'Common'), ('School', 'School'), ('Elderly', 'Elderly'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    c_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES, default='Common')

    def __str__(self):
        return self.user.username
