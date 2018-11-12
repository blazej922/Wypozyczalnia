from django.contrib import admin
from models import Manufacturer, Car, Engine, Comment, PositionInOrder, Order

# Register your models here.


class ManufacturerAdmin(admin.ModelAdmin):
	pass
admin.site.register(Manufacturer, ManufacturerAdmin)

class CarAdmin(admin.ModelAdmin):
	pass
admin.site.register(Car, CarAdmin)

class EngineAdmin(admin.ModelAdmin):
	pass
admin.site.register(Engine, EngineAdmin)

class CommentAdmin(admin.ModelAdmin):
	pass
admin.site.register(Comment, CommentAdmin)

class PositionInOrderAdmin(admin.ModelAdmin):
	pass
admin.site.register(PositionInOrder, PositionInOrderAdmin)

class OrderAdmin(admin.ModelAdmin):
	pass
admin.site.register(Order, OrderAdmin)


