from django.db import models

# Create your models here.

class User(models.Model):
    AGE_BRACKET = [
        ('0-10', '0-10'),
        ('11-20', '11-20'),
        ('21-30', '21-30'),
        ('31-40', '31-40'),
    ]
    username = models.CharField(max_length=100, unique=True)
    age = models.CharField(max_length=100, choices=AGE_BRACKET, default='0-10')
    
    def __str__(self):
        return self.username


class Content(models.Model):
    item = models.CharField(max_length=100)
    
    def __str__(self):
        return self.item 
    
class Message(models.Model):
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    content = models.ForeignKey(Content, related_name='content', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content.item
    