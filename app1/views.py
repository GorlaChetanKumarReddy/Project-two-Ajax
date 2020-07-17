from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
def save_user(request):
    name = request.POST.get('name')
    print(name)
    ids = {'idno':100,"name":"Django"}
    print(ids)
    return JsonResponse(ids)