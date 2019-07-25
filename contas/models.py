from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    creation_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    date = models.DateTimeField()
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.description
