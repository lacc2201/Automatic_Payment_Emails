from celery import shared_task
from .views import verificar_pagos

@shared_task
def verificar_pagos_task():
    verificar_pagos()
