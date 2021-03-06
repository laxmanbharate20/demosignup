from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer

class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        print(email,password)
        if email and password:
            user_obj = User.objects.filter(email=email)
            if user_obj.exists() and user_obj.first().check_password(password):
                user = LoginSerializer(user_obj)
                data_list = {}
                data_list.update(user.data)
                return Response({"message": "Login Successfully", "data":data_list, "code": 200})
            else:
                message = "Unable to login with given credentials"
                return Response({"message": message , "code": 500, 'data': {}} )
        else:
            message = "Invalid login details."
            return Response({"message": message , "code": 500, 'data': {}})