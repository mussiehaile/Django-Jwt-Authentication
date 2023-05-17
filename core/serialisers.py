from djoser.serializers import UserSerializer as BaseSerialiser ,UserCreateSerializer as BaseUserSerializer


class UserCreateSerialiser(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','username','password','email','first_name','last_name']
        
        

class UserSerializer(BaseSerialiser):
    class Meta(BaseSerialiser.Meta):
        fields = ['id','username','email','first_name','last_name']