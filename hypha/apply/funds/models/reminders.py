from django.conf import settings
from django.db import models


class Reminder(models.Model):
    REVIEW = 'review'
    REMINDER_TYPES = {
        REVIEW: 'Remind to Review',
    }
    submission = models.ForeignKey(
        'funds.ApplicationSubmission',
        on_delete=models.CASCADE,
        related_name='reminders'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    time = models.DateTimeField()
    action = models.CharField(
        choices=REMINDER_TYPES.items(),
        default='review',
        max_length=15,
    )
    sent = models.BooleanField(default=False)
