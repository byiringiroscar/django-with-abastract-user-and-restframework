from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    phone_number = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'phone_number', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            name=self.validated_data['name'],
            phone_number=self.validated_data['phone_number'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        user.set_password(password)
        user.save()
        return user

        # def create(self, validated_data):
        #     password = validated_data.pop('password', None)
        #     instance = self.Meta.model(**validated_data)
        #     if password is not None:
        #         instance.set_password(password)
        #     instance.save()
        #     return instance
