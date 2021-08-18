from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import math


class PostIt(models.Model):
    post_title = models.CharField(max_length=100)
    post_body = models.TextField(max_length=300)
    posted_date = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

    def time_published(self):

        time_difference = timezone.now() - self.posted_date

        if time_difference.days == 0 and 0 <= time_difference.seconds < 60:

            seconds = time_difference.seconds

            if seconds == 1:
                return f'{str(seconds)} second ago'

            else:
                return f'{str(seconds)} seconds ago'

        if time_difference.days == 0 and 60 <= time_difference.seconds < 3600:

            minutes = math.floor(time_difference.seconds / 60)

            if minutes == 1:
                return f'{str(minutes)} minute ago'
            else:
                return f'{str(minutes)} minutes ago'

        if time_difference.days == 0 and 3600 <= time_difference.seconds < 86400:

            hours = math.floor(time_difference.seconds / 3600)

            if hours == 1:
                return f'{str(hours)} hour ago'
            else:
                return f'{str(hours)} hours ago'

        if 1 <= time_difference.days < 30:

            days = time_difference.days

            if days == 1:
                return f'{str(days)} day ago'
            else:
                return f'{str(days)} days ago'

        if 30 <= time_difference.days < 365:

            months = math.floor(time_difference.days / 30)

            if months == 1:
                return f'{str(months)} month ago'
            else:
                return f'{str(months)} months ago'

        if time_difference.days >= 365:

            years = math.floor(time_difference.days / 365)

            if years == 1:
                return f'{str(years)} year ago'
            else:
                return f'{str(years)} years ago'
















