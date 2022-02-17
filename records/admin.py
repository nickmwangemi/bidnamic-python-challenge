from django.contrib import admin

from .models import AdGroup, Campaign, SearchTerm


# Register your models here.
class AdGroupAdmin(admin.ModelAdmin):
    pass


class CampaignAdmin(admin.ModelAdmin):
    pass


class SearchTermAdmin(admin.ModelAdmin):
    pass


admin.site.register(AdGroup, AdGroupAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(SearchTerm, SearchTermAdmin)
