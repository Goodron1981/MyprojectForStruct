from django.contrib import admin

from runapp.models import Excludespage, ExcludespageAdmin, Excludestate, ExcludestateAdmin

admin.site.register(Excludespage, ExcludespageAdmin)
admin.site.register(Excludestate, ExcludestateAdmin)
