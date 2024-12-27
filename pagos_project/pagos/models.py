from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def obtener_monto_mes(self, mes):
        """Calcula el monto adeudado para un mes específico."""
        pagos_mes = Pago.objects.filter(empresa=self, fecha_pago__month=mes, fecha_pago__year=datetime.now().year)
        return sum(p.monto for p in pagos_mes)

    def __str__(self):
        return self.nombre

class Pago(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago de {self.monto} - {self.fecha_pago}"

