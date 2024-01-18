from django.contrib import admin

from myapp.models import Currency, Rate, Holdings


# Register your models here.
class CurrencyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Currency, CurrencyAdmin)

class HoldingsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Holdings, HoldingsAdmin)

class RateAdmin(admin.ModelAdmin):
    pass
admin.site.register(Rate,RateAdmin)
