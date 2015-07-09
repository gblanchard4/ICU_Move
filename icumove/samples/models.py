from django.db import models

# Create your models here.

ICU_CHOICES = (
	('M', 'ILH M-ICU'),
	('T', 'ILH T-ICU'),
	('P', 'UMC T/S-ICU Purple'),
	('O', 'UMC M-ICU Orange'), 
	('G', 'UMC Control ICU Green')
)

# Air sample model
class Air(models.Model):

	PUMP_CHOICES = zip(range(1,10), range(1,10))

	SIDE_CHOICES = (
		'A' = 'Outside of Reception, "Aft"', 
		'B' = 'Inside of Reception, "Bow"'
	)

	date = models.DateField(verbose_name="Sample Date"),
	time = models.TimeFields(verbose_name="Time of Sample"),
	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name='ICU Location'),
	pump = models.IntegerField(choices=PUMP_CHOICES, verbose_name='Pump Number'),
	side = models.CharField(max_length=1, choices=SIDE_CHOICES, verbose_name='Pump Side')

