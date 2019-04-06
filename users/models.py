from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    def full_name(self):
        if self.first_name == '' and self.last_name == '':
            return self.username
        else:
            return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()
