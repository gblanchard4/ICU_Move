from django.db import models
from django.core.exceptions import ValidationError

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

	PUMP_CHOICES = (
		('A', 'ICS Station A'), 
		('B', 'ICS Station B'),
		('C', 'ICS Station C'),
		('W', 'Waiting Room')
	)

	SIDE_CHOICES = (
		('1', 'Filter 1'), 
		('2', 'Filter 2')
	)

	sample_date = models.DateField(verbose_name="Sample Date")
	time = models.TimeField(verbose_name="Time of Sample")
	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name='ICU Location')
	pump = models.CharField(max_length=1, choices=PUMP_CHOICES, verbose_name='Pump Number')
	side = models.CharField(max_length=1, choices=SIDE_CHOICES, verbose_name='Pump Side')
		
	def _get_day(self):
		return self.sample_date.day
	day = property(_get_day)
	
	def __str__(self):
		return str("A-{}-{}-{}-{}{}{}{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time.strftime('%H'), self.icu, self.pump, self.side, self.day))


class Door(models.Model):
	sample_date = models.DateField(verbose_name="Sample Date")
	time = models.TimeField(verbose_name="Time of Sample")
	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name='ICU Location')
	day = models.CharField(max_length=2, default='00')

	def _get_day(self):
		return self.sample_date.day
	day = property(_get_day)
	
	def __str__(self):
		return str("D-{}-{}-{}-{}DC{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time.strftime('%H'), self.icu, self.day))

class Floor(models.Model):
	sample_date = models.DateField(verbose_name="Sample Date")
	time = models.TimeField(verbose_name="Time of Sample")
	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name="ICU Location")
	day = models.CharField(max_length=2, default='00')

	def _get_day(self):
		return self.sample_date.day
	day = property(_get_day)
	
	def __str__(self):
		return str("F-{}-{}-{}-{}FC{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time.strftime('%H'), self.icu, self.day))

class Stool(models.Model):

	PRESSURE_CHOICES = (
		('NAN', 'Not Pressured'),
		('NEG', 'Negative Pressure'),
		('POS', 'Positive Pressure')
	)


	sample_date = models.DateField(verbose_name="Sample Date")
	time = models.TimeField(verbose_name="Time of Sample")
	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name="ICU Location")
	room = models.CharField(max_length=4, verbose_name="Room Number")
	pressure = models.CharField(max_length=3, choices=PRESSURE_CHOICES, verbose_name="Room pressure")
	emr = models.CharField(max_length=10, verbose_name="Epic Medical Record Number)")
	day = models.CharField(max_length=2, default='00')

	def _get_day(self):
		return self.sample_date.day
	day = property(_get_day)

	def __str__(self):
		return str("A-{}-{}-{}-{}-{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time.strftime('%H'), self.room, self.emr))

	# Custom Primary Key
	def keymaker(self):
		return str("A{}{}{}{}{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time.strftime('%H'), self.room, self.emr))
	custom_key = keymaker(self)
	key_field = models.CharField(primary_key=True, default=custom_key)

	## Clean Overide for Validation

	def clean(self):
		# Make sure only rooms that have preassure panels select and option
		pressure_rooms = ['4115','4116','4117','4141','4142','4143','4215','4241','4315','4341']
		if self.pressure == 'NEG' and not self.room in pressure_rooms:
			raise ValidationError('%s is not a valid negative pressure room' % self.room)
		if self.pressure == 'POS' and not self.room in pressure_rooms:
			raise ValidationError('%s is not a valid positive pressure room' % self.room)

		# Validate Room numbers

		tower_dict = {'O':'1', 'G':'2', 'P':'3'}
		if not tower_dict[self.icu] == self.room[1]:
			raise ValidationError('Room %s can not be in tower %s' % (self.room, self.icu))
		valid_room_enders = ['15','16','17','18','19','20','32','33','34','35','36','37','41','42','43','44','45','46','61','62','63','64','65','66']
		if not self.room[2::] in valid_room_enders:
			raise ValidationError('Room %s is not a valid room, hint check %s' % (self.room, self.room[2::]))
