# Create your tasks here
from celery import shared_task

from main.models import Upvote


@shared_task
def upvote_clean():
    upvotes = Upvote.objects.all()
    upvotes.delete()
