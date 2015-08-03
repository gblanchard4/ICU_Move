from django.contrib import admin
from .models import Air, Stool, Environment, Toilet

# Admin Model views
class AirAdmin(admin.ModelAdmin):
	list_display = ('uid','sample_date','time','icu','pump','side', 'day')
	fieldsets = (
		('Date and Time',{
			'fields':['sample_date','time']
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
			'fields':['stool_number','emr']
		}),
		('Storage Location',{
			'fields':['rack','box']
		}),
		('Notes',{
			'fields':['notes']
		})
	)

class EnvironmentAdmin(admin.ModelAdmin):
	list_display  =('sample_date', 'time')
	fieldsets = (
		('Date',{
			'fields':['sample_date', 'time']
		}),
		('Tower 1',{
			'fields':['tower1_E_temp','tower1_E_humi','tower1_E_pres','tower1_A_temp','tower1_A_humi','tower1_A_pres','tower1_B_temp','tower1_B_humi','tower1_B_pres','tower1_C_temp','tower1_C_humi','tower1_C_pres']
		}),
		('Tower 2',{
			'fields':['tower2_E_temp','tower2_E_humi','tower2_E_pres','tower2_A_temp','tower2_A_humi','tower2_A_pres','tower2_B_temp','tower2_B_humi','tower2_B_pres','tower2_C_temp','tower2_C_humi','tower2_C_pres']
		}),
		('Tower 3',{
			'fields':['tower3_A_temp','tower3_A_humi','tower3_A_pres','tower3_B_temp','tower3_B_humi','tower3_B_pres']
		})
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
