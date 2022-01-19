from django.db import models
from matplotlib.pyplot import title

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=218,null=False, blank=False)
    description = models.CharField(max_length=512,null=True, blank=True)
    code = models.CharField(max_length=28,null=False,blank=False)
    deadline = models.DateField(null=False, blank=False)
    status = models.CharField(max_length=10,choices=[("True","complete"),("False","incomplete")],default="False")

    def __str__(self):
        return f"{self.code} {self.title}"
