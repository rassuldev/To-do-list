from django.db import models


#class Category(models.Model):
#    name = models.CharField()

#    def __str__(self):
#        return self.name


class ToDoListItem(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
#    name_cat = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
# Create your models here.
    def __str__(self):
        return self.content
    class Meta:
        ordering = ['completed']