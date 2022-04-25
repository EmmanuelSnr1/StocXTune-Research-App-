from curses.ascii import US
from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta: 
        model = User
        fields = ['id','name','email','password']
        extra_kwargs = {
            'password':{'write_only': True}
        }


