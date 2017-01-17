from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
import json
from . import dummy


def post_request_check(request, header_list, body_list):
    for param in header_list:
        if 'HTTP_' + str(param.upper()) not in request.META.keys():
            return False
    for param in body_list:
        if param not in json.loads(request.body).keys():
            return False
    return True


def get_request_check(request, header_list, body_list):
    for param in header_list:
        if 'HTTP_' + str(param.upper()) not in request.META.keys():
            return False
    for param in body_list:
        if param not in json.loads(request.GET).keys():
            return False
    return True


@csrf_exempt
def social_login(request):
    if request.method == 'POST':
        if post_request_check(request, [], dummy.social_login['request']):
            response = JsonResponse(dummy.social_login['response'])
        else:
            response = JsonResponse({
                "meta": {},
                "data": {}
            }, status=400)

    else:
        response = JsonResponse({
            "meta": {},
            "data": {}
        }, status=405)
    return response


@csrf_exempt
def homepage(request, customer_id):
    if request.method == 'GET':
        if get_request_check(request, ['token'], dummy.homepage['request']):
            response = JsonResponse(dummy.homepage['response'])
        else:
            response = JsonResponse({
                "meta": {},
                "data": {}
            }, status=400)

    else:
        response = JsonResponse({
            "meta": {},
            "data": {}
        }, status=405)
    return response
