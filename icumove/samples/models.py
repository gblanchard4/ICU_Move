from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator


# Global values

DAY_1 = date(2015,07,04)

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
		('E', 'Outdoor')
	)

	SIDE_CHOICES = (
		('1', 'Filter 1'), 
		('2', 'Filter 2')
	)

	TUB_CHOICES = (
		('1', 'Tub 1'),
		('2', 'Tub 2')
	)

	sample_date = models.DateField(verbose_name="Sample Date")
	time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="Time of Sample")
	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name='ICU Location')
	pump = models.CharField(max_length=1, choices=PUMP_CHOICES, verbose_name='Pump Number')
	side = models.CharField(max_length=1, choices=SIDE_CHOICES, verbose_name='Pump Side')
	# Storage Location
	tub = models.CharField(max_length=1, choices=TUB_CHOICES, verbose_name='Storage Tub')
	rack = models.CharField(max_length=2, verbose_name='Freezer Rack', blank=True)
	shelf = models.CharField(max_length=2, verbose_name='Shelf', blank=True)
	box = models.CharField(max_length=2, verbose_name='Box', blank=True)

	# Calculated
	day = models.CharField(max_length=2, default='00')
	uid = models.CharField(primary_key=True, max_length=16, unique=True)

	
	def __str__(self):
		return str("A-{}-{}-{}-{}{}{}{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time, self.icu, self.pump, self.side, self.day))

	# Unique together
	class Meta:
		unique_together = ("sample_date", "icu", "pump", "side")
		unique_together = ("rack", "shelf", "box")

	def save(self):
		# calculate day from DAY_1
		self.day = "%02d" % (self.sample_date - DAY_1).days
		# UID
		self.uid = str("A-{}-{}-{}-{}{}{}{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time, self.icu, self.pump, self.side, self.day))
		super(Air, self).save()
	

class Stool(models.Model):

	PRESSURE_CHOICES = (
		('NAN', 'Not Pressured'),
		('NEG', 'Negative Pressure'),
		('POS', 'Positive Pressure')
	)

	sample_date = models.DateField(verbose_name="Sample Date")
	time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="Time of Sample")
	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name="ICU Location")
	room = models.CharField(max_length=4, verbose_name="Room Number")
	pressure = models.CharField(max_length=3, choices=PRESSURE_CHOICES, verbose_name="Room pressure")
	emr = models.CharField(max_length=10, verbose_name="Epic Medical Record Number")
	day = models.CharField(max_length=2, default='00')
	uid = models.CharField(primary_key=True, max_length=27, unique=True)
	# Storage Location
	rack = models.CharField(max_length=2, verbose_name='Freezer Rack', blank=True)
	shelf = models.CharField(max_length=2, verbose_name='Shelf', blank=True)
	box = models.CharField(max_length=2, verbose_name='Box', blank=True)

	def __str__(self):
		return str("S-{}-{}-{}-{}-{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time, self.room, self.emr))

	# Unique together
	class Meta:
		unique_together = ("sample_date", "time", "icu", "room", "emr")

	# Clean Overide for Validation
	def clean(self):
		# Validate unique Freezer/Shelf/Rack/Box

		# Make sure only rooms that have preassure panels select and option
		pressure_rooms = ['4115','4116','4117','4141','4142','4143','4215','4241','4315','4341']
		if self.pressure == 'NEG' and not self.room in pressure_rooms:
			raise ValidationError('%s is not a valid negative pressure room' % self.room)
		if self.pressure == 'POS' and not self.room in pressure_rooms:
			raise ValidationError('%s is not a valid positive pressure room' % self.room)

		# Validate Room numbers for POG
		tower_dict = {'O':'1', 'G':'2', 'P':'3'}
		if self.icu in tower_dict:
			if not tower_dict[self.icu] == self.room[1]:
				raise ValidationError('Room %s can not be in tower %s' % (self.room, self.icu))
			valid_room_enders = ['15','16','17','18','19','20','32','33','34','35','36','37','41','42','43','44','45','46','61','62','63','64','65','66']
			if not self.room[2::] in valid_room_enders:
				raise ValidationError('Room %s is not a valid room, hint check %s' % (self.room, self.room[2::]))

	def save(self):
		# calculate day from DAY_1
		self.day = "%02d" % (self.sample_date - DAY_1).days
		# UID
		self.uid = str("S-{}-{}-{}-{}-{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time.strftime('%H'), self.room, self.emr))
		super(Stool, self).save()


class Environment(models.Model):

	PUMP_CHOICES = (
		('A', 'ICS Station A'), 
		('B', 'ICS Station B'),
		('C', 'ICS Station C'),
		('E', 'Outdoor')
	)

	SIDE_CHOICES = (
		('1', 'Filter 1'), 
		('2', 'Filter 2')
	)


	sample_date = models.DateField(verbose_name="Sample Date")
	time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="Time of Sample")
	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name='ICU Location')
	pump = models.CharField(max_length=1, choices=PUMP_CHOICES, verbose_name='Pump Number')
	side = models.CharField(max_length=1, choices=SIDE_CHOICES, verbose_name='Pump Side')
	
	humidity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Percent Relative Humidity")
	temp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Temperature in °F???")
	airflow = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Airflow")
	airdirection = models.CharField(max_length=2, verbose_name="Air Direction")
	

	# Calculated
	day = models.CharField(max_length=2, default='00')
	uid = models.CharField(primary_key=True, max_length=16, unique=True)

	
	def __str__(self):
		return str("A-{}-{}-{}-{}{}{}{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time, self.icu, self.pump, self.side, self.day))

	# Unique together
	class Meta:
		unique_together = ("sample_date", "icu", "pump", "side")

	def save(self):
		# calculate day from DAY_1
		self.day = "%02d" % (self.sample_date - DAY_1).days
		# UID
		self.uid = str("A-{}-{}-{}-{}{}{}{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time, self.icu, self.pump, self.side, self.day))
		super(Air, self).save()
	
# class Door(models.Model):
# 	sample_date = models.DateField(verbose_name="Sample Date")
# 	time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="Time of Sample")
# 	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name='ICU Location')
# 	day = models.CharField(max_length=2, default='00')
# 	uid = models.CharField(primary_key=True, max_length=16, unique=True)
# 	# Storage Location
# 	rack = models.CharField(max_length=2, verbose_name='Freezer Rack', blank=True)
# 	shelf = models.CharField(max_length=2, verbose_name='Shelf', blank=True)
# 	box = models.CharField(max_length=2, verbose_name='Box', blank=True)
	
# 	def __str__(self):
# 		return str("D-{}-{}-{}-{}DC{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time, self.icu, self.day))

# 	# Unique together
# 	class Meta:
# 		unique_together = ("sample_date", "icu", "day")
		
# 	def save(self):
# 		# calculate day from DAY_1
# 		self.day = "%02d" % (self.sample_date - DAY_1).days
# 		# UID
# 		self.uid = str("D-{}-{}-{}-{}DC{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time, self.icu, self.day))
# 		super(Door, self).save()

# class Floor(models.Model):
# 	sample_date = models.DateField(verbose_name="Sample Date")
# 	time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="Time of Sample")
# 	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name="ICU Location")
# 	day = models.CharField(max_length=2, default='00')
# 	uid = models.CharField(primary_key=True, max_length=16, unique=True)
# 	# Storage Location
# 	rack = models.CharField(max_length=2, verbose_name='Freezer Rack', blank=True)
# 	shelf = models.CharField(max_length=2, verbose_name='Shelf', blank=True)
# 	box = models.CharField(max_length=2, verbose_name='Box', blank=True)

# 	def __str__(self):
# 		return str("F-{}-{}-{}-{}FC{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time, self.icu, self.day))

# 	# Unique together
# 	class Meta:
# 		unique_together = ("sample_date", "icu", "day")



# 	def save(self):
# 		# calculate day from DAY_1
# 		self.day = "%02d" % (self.sample_date - DAY_1).days
# 		# UID
# 		self.uid = str("F-{}-{}-{}-{}FC{}".format(self.icu, self.sample_date.strftime('%m%d'), self.time, self.icu, self.day))
# 		super(Floor, self).save()