from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from rest_framework import status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from backend.account.serializers.auth import SignUpSerializer


class Signup(views.APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    @method_decorator(never_cache)
    def put(self, request, user_id):
        userdata = request.data
        user = User.objects.filter(id=user_id).first()
        if userdata.get("action") == 'is_active':
            user.is_active = userdata.get("is_active")
            user.save()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        user.username = userdata.get("username")
        user.email = userdata.get("email")
        user.first_name = userdata.get("first_name")
        user.last_name = userdata.get("last_name")
        user.save()

        return Response({'msg': 'account updated'}, status=status.HTTP_200_OK)

    @method_decorator(never_cache)
    def post(self, request):
        userdata = request.data
        serializer = SignUpSerializer(data=userdata)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response({'msg': 'account created'}, status=status.HTTP_201_CREATED)
