from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Forum(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.topic

    def get_discussions(self):
        return self.discussions.filter(parent=None)

class Discussion(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, null=False, on_delete=models.CASCADE, related_name='discussions')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    answer = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer 

    def get_discussions(self):
        return Discussion.objects.filter(parent=self)  	