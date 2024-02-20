# from django.db import models
# from user.models import User
# from category.models import Category
# from user.models import User

# class Ticket(models.Model):
#     STATUS_CHOICES = [
#         ('open', 'Open'),
#         ('in_progress', 'In Progress'),
#         ('closed', 'Closed'),
#     ]
#     id=models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE,default=Category.CATEGORY_CHOICES)
#     status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def _str_(self):
#         return self.title
    
# models.py
from django.db import models
from user.models import User
from cms import settings

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
        
    ]
    id=models.AutoField(primary_key=True)
    issue = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name = "tickets",null=True)
    solution= models.TextField(blank=True, null=True)

    def __str__(self):
        return self.issue