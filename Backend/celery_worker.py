from celery import Celery

celery_app = Celery(
    'expense_tracker',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@celery_app.task
def send_reminder():
    return "Reminder sent"
