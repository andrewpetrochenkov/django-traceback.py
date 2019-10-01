from django.db import models


class Traceback(models.Model):
    type = models.TextField()
    value = models.TextField()
    traceback = models.TextField()
    path = models.TextField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'django_traceback'
        ordering = ['-created_at']
