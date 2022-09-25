from django.db import models
from django.contrib.auth.models import User


#class Category(models.Model):
#    name = models.CharField()

#    def __str__(self):
#        return self.name


class ToDoListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
#    name_cat = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
# Create your models here.
    def __str__(self):
        return self.content
    class Meta:
        ordering = ['-created']