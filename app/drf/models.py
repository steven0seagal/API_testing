from django.db import models

# Create your models here.
class WarehouseDRF(models.Model):
    id = models.AutoField(primary_key=True)
    object_name = models.CharField(max_length=255)
    number_of_objects = models.IntegerField()

    def __str__(self):
        return self.object_name