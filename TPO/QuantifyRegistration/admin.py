from django.contrib import admin
from .models import Candidate

# Customize how Candidate is displayed in admin
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'father_name', 'email', 'mobile', 'age', 'job_role')
    search_fields = ('name', 'email', 'mobile', 'job_role')
    list_filter = ('job_role', 'age')
    ordering = ('name',)

# Register the model with the custom admin
admin.site.register(Candidate, CandidateAdmin)
