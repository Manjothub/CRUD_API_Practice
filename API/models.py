from django.db import models

class Bookslibrarry(models.Model):
    book_title = models.CharField(max_length=50,null=True)
    book_author = models.CharField(max_length=10,null=True)
    book_description = models.CharField(max_length=250,null=True)
    book_issue_date = models.DateField(null=True)