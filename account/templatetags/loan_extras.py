from django import template
from django.template.defaultfilters import stringfilter
from datetime import date,datetime, timedelta
register=template.Library()
@register.filter
def check_loan(obj):
    if obj.department=="NTD":
        if obj.loan_balance==50000:
            return 1
        if obj.emi>0:
            return 2
        return 3
    else:
        if obj.loan_balance==100000:
            return 1
        if obj.emi>0:
            return 2
        return 3
