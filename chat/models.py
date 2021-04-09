import datetime
from django.db import models


class Message(models.Model):
    author = models.CharField(max_length=30, null=False)
    email = models.EmailField(default=None, null=False)
    text = models.TextField(null=False, max_length=100)
    pub_date = models.DateTimeField("create date", default=datetime.datetime.now())
    update_date = models.DateTimeField("update date", null=True, blank=True)

    def __str__(self):
        return f"{self.author}'s message"
