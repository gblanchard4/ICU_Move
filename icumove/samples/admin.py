from django.contrib import admin
from .models import Air, Stool, Environment, Toilet

# Admin Model views
class AirAdmin(admin.ModelAdmin):
	list_display = ('uid','sample_date','icu','pump','side', 'day')
	fieldsets = (
		('Date and Time',{
			'fields':['sample_date']
		}),
		('Collection Location',{
			'fields':['color','icu','pump','side']
		}),
		('Storage Location',{
			'fields':['rack','box']
		}),
		('Notes',{
			'fields':['notes']
		})
	)

class StoolAdmin(admin.ModelAdmin):
	list_display = ('uid','sample_date','time','icu','room','pressure','emr','day')
	fieldsets = (
		('Date and Time',{
			'fields':['sample_date','time']
		}),
		('Collection Location',{
			'fields':['icu','room']
		}),
		('Patient',{
			'fields':['emr']
		}),
		('Storage Location',{
			'fields':['rack','box']
		}),
		('Notes',{
			'fields':['notes']
		}),
		('EMR Check',{
			'fields':['emr_check']
		})
	)

class EnvironmentAdmin(admin.ModelAdmin):
	fieldsets = (
		('Date',{
			'fields':['sample_date',]
		}),
		('Tower 1:',{
			'fields':[('tower1_B_temp','tower1_B_humi','tower1_B_pres')]
		}),
		('Tower 2',{
			'fields':[('tower2_B_temp','tower2_B_humi','tower2_B_pres')]
		}),
		('Tower 3',{
			'fields':[('tower3_A_temp','tower3_A_humi','tower3_A_pres')]
		}),
		('Exterior:',{
			'fields':[('exterior_temp','exterior_humi','exterior_pres')]
		}),
	)

class ToiletAdmin(admin.ModelAdmin):
	list_display = ('uid', 'sample_date', 'icu', 'room')
	fieldsets = (
		('Date',{
			'fields':['sample_date']
		}),
		('Collection Location',{
			'fields':['icu', 'room']
		}),
		('Storage Location',{
			'fields':['rack','box']
		}),
		('Notes',{
			'fields':['notes']
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
admin.site.register(Toilet, ToiletAdmin)
# admin.site.register(Door, DoorAdmin)
# admin.site.register(Floor, FloorAdmin)
