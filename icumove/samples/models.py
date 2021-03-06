from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator


# Global values
DAY_1 = date(2015,07,28)

# Air sample model
class Air(models.Model):

	ICU_CHOICES = (
		('1', 'UMC Tower-1'),
		('2', 'UMC Tower-2'),
		('3', 'UMC Tower-3')
	)

	COLOR_CHOICES = (
		('R', 'Red'),
		('G', 'Green'),
		('P', 'Purple')
	)

	PUMP_CHOICES = (
		('A', 'ICS Station A'),
		('B', 'ICS Station B'),
		('C', 'ICS Station C'),
		('E', 'Exterior')
	)

	SIDE_CHOICES = (
		('1', 'Filter 1'),
		('2', 'Filter 2')
	)

	# DateTime
	sample_date = models.DateField(verbose_name="Sample Date: Date of Deployment")
	#time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="Hour of Sample: 24hr Clock")
	# Sample Information
	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name='ICU Location')
	color = models.CharField(max_length=1, choices=COLOR_CHOICES, verbose_name='Tape Color')
	pump = models.CharField(max_length=1, choices=PUMP_CHOICES, verbose_name='Pump Letter')
	side = models.CharField(max_length=1, choices=SIDE_CHOICES, verbose_name='Pump Side')
	# Storage Location
	rack = models.CharField(max_length=2, verbose_name='Freezer Rack', blank=True)
	box = models.CharField(max_length=2, verbose_name='Box', blank=True)
	# Calculated
	day = models.CharField(max_length=2, default='00')
	uid = models.CharField(primary_key=True, max_length=16, unique=True)
	# Notes
	notes = models.TextField(verbose_name="Notes", blank=True)


	def __str__(self):
		return str("A-{}-{}{}-{}".format(self.color, self.pump, self.side, self.sample_date.strftime('%m%d%y')))

	# Unique together
	class Meta:
		unique_together = ("sample_date", "icu", "pump", "side")
		unique_together = ("rack", "box")

	def clean(self):
		# Validate unique Freezer/Shelf/Rack/Box
		#Ehhh
		# Validate Tower to Color
		tower_to_color_dict = {'1':'R','2':'G','3':'P'}
		if not tower_to_color_dict[self.icu] == self.color:
			raise ValidationError("{} is not the right color for tower {}".format(self.color, self.icu))

	def save(self):
		# calculate day from DAY_1
		self.day = "%02d" % (self.sample_date - DAY_1).days
		# UID
		self.uid = str("A-{}-{}{}-{}".format(self.color, self.pump, self.side, self.sample_date.strftime('%m%d%y')))
		super(Air, self).save()


class Stool(models.Model):


	ICU_CHOICES = (
		('M', 'ILH M-ICU'),
		('T', 'ILH T-ICU'),
		('1', 'UMC Tower-1'),
		('2', 'UMC Tower-2'),
		('3', 'UMC Tower-3')
	)

	PRESSURE_CHOICES = (
		('NAN', 'Not Pressured'),
		('NEG', 'Negative Pressure'),
		('POS', 'Positive Pressure')
	)

	#DateTime
	sample_date = models.DateField(verbose_name="Date Collected")
	time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="Hour Sample Collected (24hr Clock)")
	# Sample Location
	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name="ICU Location")
	room = models.CharField(max_length=4, verbose_name="Room Number")
	# Metadata
	emr = models.CharField(max_length=10, verbose_name="Epic Medical Record Number")
	emr_check = models.CharField(max_length=10, verbose_name="Epic Medical Record Number")
	# Storage Location
	rack = models.CharField(max_length=2, verbose_name='Freezer Rack', blank=True)
	box = models.CharField(max_length=2, verbose_name='Box', blank=True)
	# Calculated
	day = models.CharField(max_length=2, default='00')
	uid = models.CharField(primary_key=True, max_length=27, unique=True)
	pressure = models.CharField(max_length=3, choices=PRESSURE_CHOICES, verbose_name="Room pressure")
	# Notes
	notes = models.TextField(verbose_name="Notes", blank=True)

	def __str__(self):
		return str("S-{}-{}-{}".format(self.room, self.sample_date.strftime('%m%d'), "%02d" % self.time))

	# Unique together
	class Meta:
		unique_together = ("sample_date", "time", "icu", "room", "emr")

	# Clean Overide for Validation
	def clean(self):
		if not self.emr == self.emr_check:
			raise ValidationError('EMR Does not match')

		# Validate Room numbers for POG
		valid_room_enders = ['15','16','17','18','19','20','32','33','34','35','36','37','41','42','43','44','45','46','61','62','63','64','65','66']
		if self.icu in ['1', '2,', '3']:
			if not self.icu == self.room[1]:
				raise ValidationError('Room %s can not be in tower %s' % (self.room, self.icu))
			if not self.room[2::] in valid_room_enders:
				raise ValidationError('Room %s is not a valid room, hint check %s' % (self.room, self.room[2::]))

	def save(self):
		# calculate day from DAY_1
		self.day = "%02d" % (self.sample_date - DAY_1).days
		# UID
		self.uid = str("S-{}-{}-{}".format(self.room, self.sample_date.strftime('%m%d%y'), "%02d" % self.time))
		# Pressure
		neg_pressure_rooms = ['4115','4116','4117','4141','4142','4143','4215','4241','4315','4341']
		if self.room in neg_pressure_rooms:
			self.pressure = "NEG"
		else:
			self.pressure = "NOR"
		super(Stool, self).save()


class Environment(models.Model):

	# DateTime
	sample_date = models.DateField(verbose_name="Sample Date")
	#time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="Hour of Sample (24-hour Clock")

	exterior_temp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)],  verbose_name="Exterior: Temperature in C", blank=True, null=True)
	exterior_humi = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Exterior: Percent Relative Humidity", blank=True, null=True)
	exterior_pres = models.IntegerField(validators=[MinValueValidator(740), MaxValueValidator(780)], verbose_name="Exterior: Barometric Pressure", blank=True, null=True)
	# Tower-1
	tower1_B_temp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)],  verbose_name="ICS-B: Temperature in C", blank=True, null=True)
	tower1_B_humi = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="ICS-B: Percent Relative Humidity", blank=True, null=True)
	tower1_B_pres = models.IntegerField(validators=[MinValueValidator(740), MaxValueValidator(780)], verbose_name="ICS-B: Barometric Pressure", blank=True, null=True)
	# Tower-2
	tower2_B_temp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)],  verbose_name="ICS-B: Temperature in C", blank=True, null=True)
	tower2_B_humi = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="ICS-B: Percent Relative Humidity", blank=True, null=True)
	tower2_B_pres = models.IntegerField(validators=[MinValueValidator(740), MaxValueValidator(780)], verbose_name="ICS-B: Barometric Pressure", blank=True, null=True)
	# Tower-3
	tower3_A_temp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)],  verbose_name="ICS-A: Temperature in C", blank=True, null=True)
	tower3_A_humi = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="ICS-A: Percent Relative Humidity", blank=True, null=True)
	tower3_A_pres = models.IntegerField(validators=[MinValueValidator(740), MaxValueValidator(780)], verbose_name="ICS-A: Barometric Pressure", blank=True, null=True)

	# Calculated
	day = models.CharField(max_length=2, default='00')
	# Notes
	notes = models.TextField(verbose_name="Notes", blank=True)


	def __str__(self):
		return str("E-{}".format(self.sample_date.strftime('%m%d%y')))

	def save(self):
		# calculate day from DAY_1
		self.day = "%02d" % (self.sample_date - DAY_1).days
		super(Environment, self).save()

class Toilet(models.Model):

	ICU_CHOICES = (
		('1', 'UMC Tower-1'),
		('2', 'UMC Tower-2'),
		('3', 'UMC Tower-3')
	)

	# DateTime
	sample_date = models.DateField(verbose_name="Sample Date")
	# Sample Location
	icu = models.CharField(max_length=1, choices=ICU_CHOICES, verbose_name='ICU Location')
	room = models.CharField(max_length=4, verbose_name="Room Number")
	# Storage Location
	rack = models.CharField(max_length=2, verbose_name='Freezer Rack', blank=True)
	box = models.CharField(max_length=2, verbose_name='Box', blank=True)
	# Calculated
	day = models.CharField(max_length=2, default='00')
	uid = models.CharField(primary_key=True, max_length=16, unique=True)
	# Notes
	notes = models.TextField(verbose_name="Notes", blank=True)


	def __str__(self):
		return str("T-{}-{}".format(self.room, self.sample_date.strftime('%m%d%y')))

	# Unique together
	class Meta:
		unique_together = ("icu", "room", "sample_date")

	def clean(self):
		# Validate unique Freezer/Shelf/Rack/Box

		# Validate Room numbers for POG
		if not self.icu == self.room[1]:
			raise ValidationError('Room %s can not be in tower %s' % (self.room, self.icu))
		valid_room_enders = ['15','16','17','18','19','20','32','33','34','35','36','37','41','42','43','44','45','46','61','62','63','64','65','66']
		if not self.room[2::] in valid_room_enders:
			raise ValidationError('Room %s is not a valid room, hint check %s' % (self.room, self.room[2::]))

	def save(self):
		# calculate day from DAY_1
		self.day = "%02d" % (self.sample_date - DAY_1).days
		# UID
		self.uid = str("T-{}-{}".format(self.room, self.sample_date.strftime('%m%d%y')))
		super(Toilet, self).save()

# class Door(models.Model):
# 	sample_date = models.DateField(verbose_name="Sample Date")
# 	time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="Hour of Sample (24-hour Clock")
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
# 	time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="Hour of Sample (24-hour Clock")
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
