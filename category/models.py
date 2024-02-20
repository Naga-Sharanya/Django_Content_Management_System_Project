from django.db import models
from django.db.models import Q

from cms import settings

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category

# class Content(models.Model):
#     id=models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     #category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='contents')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name = "created_by",null=True)
#     updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name = "updated_by",null=True)
#     image=models.ImageField()

#     def __str__(self):
#         return self.title
    
    
class Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="created_by", null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="updated_by", null=True)
    image = models.ImageField()
    archived = models.BooleanField(default=False)# New field
    is_deleted = models.BooleanField(default=False) # New field to mark if the content is soft deleted or not
    


    def __str__(self):
        return self.title
