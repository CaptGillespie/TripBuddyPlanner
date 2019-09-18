from __future__ import unicode_literals
from django.db import models
from apps.login_app.models import User
from datetime import datetime 

class TripManager(models.Manager):
    def jobValidator(self, postData):
        errors = {}
        date_format = "%d/%m/%Y %H:%M:%S"
        start = datetime.strptime(postData["start_date"], date_format)
        end = datetime.strptime(postData["end_date"], date_format)
        now = datetime.now()

        if len(postData["destination"]) < 3:
            errors["destination"] = "Cryptic is one thing, vague is another, tell them where they're going!"
        if len(postData['plan']) < 3:
            errors["plan"] = "Are you just going to wander around? Elaborate!"
        if start < now:
            errors["start_date"] = "You can't go back in time!"
        if end < start:
            errors["end_date"] = "Unless you're going back in time...?"
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=45, default='jobtitle')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    plan = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="trips")
    objects = TripManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trips = models.ManyToManyField(User, related_name="tourists")
    def __str__(self):
        return self.destination

