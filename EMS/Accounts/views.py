from django.shortcuts import render
from django.views import View
from django.contrib import auth
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


# Create your views here.
class login_api(View):
    def post(self, request, *args, **kwargs):
        __account = request.POST.get('account')
        __password = request.POST.get('password')
        print(__account, __password)
        user = auth.authenticate(username=__account, password=__password)
        if user is not None and user.is_active:
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({"log_in_resp": "pass", 'token': token.key}, status=200)
        else:
            if(self.check_account_exist(__account)==False):
                #return Response({"sign_in_resp": "account fail", "account":__account})
                return JsonResponse({"log_in_resp": "account fail"}, status=401)
            #return Response({"sign_in_resp": "password fail"})
            return JsonResponse({"log_in_resp": "password fail"}, status=401)

    def check_account_exist(self, __account):
        """
        Check if a user with the given username exists in the database.
        Returns True if the user exists, False otherwise.
        """
        print(__account)
        User = get_user_model()
        try:
            User.objects.get(username=__account)
            return True
        except:
            return False
    