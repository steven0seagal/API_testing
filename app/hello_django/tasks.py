from celery import shared_task
from celery.utils.log import get_task_logger
from .celery import app
from datetime import datetime

logger = get_task_logger(__name__)


@shared_task
def check_time():
    print("Checking time {}".format(datetime.now()))
