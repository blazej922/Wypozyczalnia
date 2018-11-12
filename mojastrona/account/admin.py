from django.contrib import admin
from models import Fault, FaultComment, Service

# Register your models here.

class FaultAdmin(admin.ModelAdmin):
	pass
admin.site.register(Fault, FaultAdmin)

class FaultCommentAdmin(admin.ModelAdmin):
	pass
admin.site.register(FaultComment, FaultCommentAdmin)

class ServiceAdmin(admin.ModelAdmin):
	pass
admin.site.register(Service, ServiceAdmin)