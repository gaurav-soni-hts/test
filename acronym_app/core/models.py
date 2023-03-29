from django.db import models

# Create your models here.
class Acronym(models.Model):
    """An acronym that user wants to know about"""
    acronym = models.CharField(max_length=20)
    expanded_form = models.CharField(max_length=200)
    about = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False):
        self.acronym = self.acronym.upper()
        super(Acronym, self).save(force_insert,force_update)

    def __str__(self):
        return self.acronym