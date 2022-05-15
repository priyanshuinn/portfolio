from django.db import models
from django.utils.timezone import now
    

class ContactUS(models.Model):
    message  = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    subject = models.TextField()
    created = models.DateTimeField(default=now, editable=False)
