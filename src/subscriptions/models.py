from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("advanced", "Advanced Perm"),
            ("pro", "Pro Perm"),
            ("basic", "Basic Perm"),
        ]
