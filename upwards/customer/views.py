from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
import json
from . import dummy
import requests


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
            print request.body
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


@csrf_exempt
def linkedin(request):
    if request.method == 'POST':
        print 11010
        authcode = request.body.get('code')
        state = request.body.get('state')
        url = 'https://www.linkedin.com/oauth/v2/accessToken'
        header = {'Content-Type': 'application/x-www-form-urlencoded', 'grant_type': 'authorization_code',
                  'code': authcode, 'redirect_uri': "http://8c732110.ngrok.io/customer/linkedin", 'client_id': "81ddg94yp82qla", 'client_secret': "AZT3lJfWhFk0j8W4"}
        print 11010
        r = requests.post(url, data=header)
        r = json.loads(r.text)
        auth_code = r[r.keys()[0]]
        print r, 101
        print authcode
    else:
        print 11010
        authcode = request.GET.get('code')
        state = request.GET.get('state')
        url = 'https://www.linkedin.com/oauth/v2/accessToken'
        header = {'Content-Type': 'application/x-www-form-urlencoded', 'grant_type': 'authorization_code',
                  'code': authcode, 'redirect_uri': "http://8c732110.ngrok.io/customer/linkedin", 'client_id': "81ddg94yp82qla", 'client_secret': "AZT3lJfWhFk0j8W4"}
        print 11010
        r = requests.post(url, data=header)
        r = json.loads(r.text)
        auth_code = r[r.keys()[0]]
        print r, 101
        print authcode
    return JsonResponse({
        "meta": {},
        "data": {}
    }, 400)


@csrf_exempt
def linkedin2(request):
    return JsonResponse({
        "meta": {},
        "data": {"linkedin2": "linkedin2"}
    })


@csrf_exempt
def config(request):
    if request.method == 'GET':
        return JsonResponse(
            {
                "USER_STATE": {
                    "eligiblity": {
                        "not_started": 0,
                        "PAN": 25,
                        "professional": 50,
                        "education": 75,
                        "miscellaneous": 100
                    },
                    "KYC": {
                        "not_started": 0,
                        "AADHAR": 25,
                        "AADHAR_details": 50,
                        "personal": 75,
                        "uploads": 100
                    }

                },
                "BASE_URL": "http://40237ad1.ngrok.io",
            })
    else:
        return JsonResponse({
            "meta": {},
            "data": {}
        }, status=405)
