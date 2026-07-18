from django.db import models

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course}"
