from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from app1.models import User_registration


@method_decorator(csrf_exempt,name='dispatch')
def Check_User_Name_Ajax(request):
    name = request.POST.get('userna')
    try:
        User_registration.objects.get(Name=name)
        res = {'error':'username is exists'}
    except User_registration.DoesNotExist:
        res = {'message':'username available'}
        return JsonResponse(res)


def save_user(request):
    return None