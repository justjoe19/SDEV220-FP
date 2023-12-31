from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import DateRangeField

class Employee(models.Model):
    employed = models.BooleanField(default=True)
    employee_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, default='')

    def is_clocked_in(self):
        latest_punch = self.punches.order_by('-punch_time').first()
        return latest_punch and latest_punch.punch_type == 'Clock In'

    def punch(self):
        if self.is_clocked_in():
            punch_type = 'Clock Out'
            print('Clock out recorded!')
        else:
            punch_type = 'Clock In'
            print('Clock in recorded!')

        current_time = timezone.now()
        Punch.objects.create(employee=self, punch_time=current_time, punch_type=punch_type)


class Punch(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='punches')
    punch_time = models.DateTimeField()
    punch_type = models.CharField(max_length=20)

class LOA(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_requests')
    requestStart = models.DateField()
    requestEnd = models.DateField()
    date_submitted = models.DateField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"LOA Request #{self.id} for {self.employee.name}"
