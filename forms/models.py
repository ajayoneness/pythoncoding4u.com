from django.db import models




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.name
