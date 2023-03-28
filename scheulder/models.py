from django.db import models
from django.urls import reverse
# Create your models here.


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Usługa'
        verbose_name_plural = 'Usługi'

    def __str__(self):
        return f"{self.service_name}"




class Event(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)    
    number = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    paid = models.BooleanField(default=False,null=True)
    
    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")
        ordering = ["time"]

    def __str__(self):
        return f"{self.service}"

    def get_absolute_url(self):
        return reverse("calendar:detail", kwargs={"pk": self.pk})
    

