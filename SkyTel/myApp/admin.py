from django.contrib import admin
from myApp.models import cc_monthly_st




class cc_monthly_stAdmin(admin.ModelAdmin):
    list_display = ('id', 'month', 'year', 'total_calls', 'answered_calls')
    list_display_links = ('id', 'month')



admin.site.register(cc_monthly_st, cc_monthly_stAdmin)