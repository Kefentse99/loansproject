from django.contrib import admin

from .models import Branch, Customer, LoanAgent, Loaninfo

admin.site.register(Customer)
admin.site.register(Branch)
admin.site.register(LoanAgent)
admin.site.register(Loaninfo)
