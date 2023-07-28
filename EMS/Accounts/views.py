from django.shortcuts import render
from django.views import View
from django.contrib import auth
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from models import Stuff


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
        
class stuff_op_api(View):

    def get(self, request, *args, **kwargs):
        name = request.GET.get('name', None)
        id = request.GET.get('id', None)

        if name:
            # 根據姓名進行查詢
            stuff_queryset = Stuff.objects.filter(name=name)
        elif id:
            # 根據ID進行查詢
            stuff_queryset = Stuff.objects.filter(id=id)
        else:
            # 若沒有提供name或id參數，回傳全部資料
            stuff_queryset = Stuff.objects.all()

        # 檢查是否有符合條件的資料
        if not stuff_queryset.exists():
            return JsonResponse({'error': 'Stuff not found.'}, status=404)

        # 將QuerySet轉換成JSON格式
        data = []
        for stuff in stuff_queryset:
            data.append({
                'id': stuff.id,
                'name': stuff.name,
                'account': stuff.account,
                'title': stuff.title,
                'unit': stuff.unit,
                'email': stuff.email,
                'permission': stuff.permission,
                'activation': stuff.activation
            })

        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
    