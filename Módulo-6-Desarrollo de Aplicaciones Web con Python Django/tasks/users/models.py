from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    def __str__(self) ->str:
        return f"{self.first_name}, {self.last_name}"
