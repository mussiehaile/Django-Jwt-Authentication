from djoser.serializers import UserCreateSerializer as BaseUserSerializer


class UserCreateSerialiser(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','username','password','email','first_name','last_name']