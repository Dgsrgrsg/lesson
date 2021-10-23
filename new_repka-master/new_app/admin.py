from django.contrib import admin

from new_app.models import Stock, Currency


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass
