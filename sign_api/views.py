from django.shortcuts import render
from django.http import JsonResponse
from sign_api.models import Event
from django.core.exceptions import  ValidationError

# Create your views here.
# 添加发布会接口
def add_event(request):
    eid = request.POST.get('eid', '')
    name = request.POST.get('name', '')
    limit = request.POST.get('limit', '')
    status = request.POST.get('status', '')
    address = request.POST.get('address', '')
    start_time = request.POST.get('start_time', '')

    if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error!'})
    result = Event.objects.filter(id = eid)

    if result:
        return JsonResponse({'status': 10022, 'message': 'event id already exists!'})
    result = Event.objects.filter(name = name)

    if result:
