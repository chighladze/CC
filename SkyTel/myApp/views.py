from django.shortcuts import render
from django.http import HttpResponse
# from .models import Cdr
from asterisk.models import Cdr
from myApp.models import cc_monthly_st
import datetime


def index(request):
    return render(request, 'myApp/index.html')


def monthly_st_desk(request):
    year_now = f"{datetime.datetime.now():%Y}"
    if request.GET.get('year', None):
        tt_calls = cc_monthly_st.objects.filter(year=request.GET.get('year'))
    else:
        tt_calls = cc_monthly_st.objects.filter(year=year_now)
    context = {
        'tt_calls': tt_calls,
        'year_filter': cc_monthly_st.objects.order_by().values_list('year', flat=True).distinct(),
        'year_now': year_now,
        'year': request.GET.get('year', year_now)
    }

    return render(request, 'myApp/monthly_stat.html', context=context)


# def monthly_st_desk_filter(request):
#     year_now = f"{datetime.datetime.now():%Y}"
#     year = request.GET.get('year', year_now)
#     tt_calls = cc_monthly_st.objects.filter(year=year)
#     year_filter = cc_monthly_st.objects.order_by().values_list('year', flat=True).distinct()
#     context = {
#         'tt_calls': tt_calls,
#         'year_filter': year_filter,
#         'year_now': year_now,
#         'year': year
#     }
#
#     return render(request, 'myApp/monthly_stat.html', context=context)

