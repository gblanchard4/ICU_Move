from django.contrib import admin
from .models import Air, Stool, Environment

# Admin Model views
class AirAdmin(admin.ModelAdmin):
	list_display = ('uid','sample_date','time','icu','pump','side', 'day')
	fieldsets = (
		('Date and Time',{
			'fields':['sample_date','time']
		}),
		('Collection Location',{
			'fields':['icu','pump','side']
		}),
		('Storage Location',{
			'fields':['tub','shelf','rack','box']
		})
	)

class StoolAdmin(admin.ModelAdmin):
	list_display = ('uid','sample_date','time','icu','room','pressure','emr','day')
	fieldsets = (
		('Date and Time',{
			'fields':['sample_date','time']
		}),
		('Collection Location',{
			'fields':['icu',('room','pressure')]
		}),
		('Patient',{
			'fields':['emr']
		}),
		('Storage Location',{
			'fields':['shelf','rack','box']
		})
	)

class EnvironmentAdmin(admin.ModelAdmin):
	list_display  = ('uid' , 'sample_date', 'time', 'icu', 'pump', 'temp', 'humidity', 'airflow', 'airdirection')
	fieldsets = (
		('Date and Time',{
			'fields':['sample_date','time']
		}),
		('Collection Location',{
			'fields':['icu', 'pump']
		}),
		('Readings',{
			'fields':['temp','humidity','airflow','airdirection']
		})
	)

# class FloorAdmin(admin.ModelAdmin):
	# list_display = ('uid','sample_date','time','icu','day')
	# fieldsets = (
		# ('Date and Time',{
			# 'fields':['sample_date','time']
		# }),
		# ('Collection Location',{
			# 'fields':['icu']
		# }),
		# ('Storage Location',{
			# 'fields':['shelf','rack','box']
		# })
	# )

# class DoorAdmin(admin.ModelAdmin):
	# list_display = ('uid','sample_date','time','icu','day')
	# fieldsets = (
		# ('Date and Time',{
			# 'fields':['sample_date','time']
		# }),
		# ('Collection Location',{
			# 'fields':['icu']
		# }),
		# ('Storage Location',{
			# 'fields':['shelf','rack','box']
		# })
	# )


# Register your models here.
admin.site.register(Air, AirAdmin)
admin.site.register(Stool, StoolAdmin)
admin.site.register(Environment, EnvironmentAdmin)
# admin.site.register(Door, DoorAdmin)
# admin.site.register(Floor, FloorAdmin)

