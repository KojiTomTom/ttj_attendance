from django.shortcuts import render, redirect
from ..utils import get_target_month, get_all_sheets
from django.conf import settings
import openpyxl

def initialize(request):

    employeeId = request.session.get('employeeId')
    employeeName = request.session.get('employeeName')

    if request.session.get('selected_month') is not None:
        selected_month = request.session.get('selected_month')
        del request.session['selected_month']
    else:
        selected_month = get_target_month()

    errMessage = ''
    successMessage = ''
    if request.session.get('err') is not None:
        errMessage = request.session.get('err')
        del request.session['err']
    if request.session.get('success') is not None:
        successMessage = request.session.get('success')
        del request.session['success']

    return render(
        request,
        settings.TEMPLATE_SEAT,
         {
            "employeeId": employeeId,
            "employeeName": employeeName,
            "month_list": get_all_sheets(),
            "selected_month": selected_month,
            "errMessage": errMessage,
            "successMessage": successMessage
        },
    )