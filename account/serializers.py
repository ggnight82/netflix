from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username','rating','first_name','last_name',
        'password', 'password2',]
        extra_kwargs = {
            'password': {
                'write_only':True
            }
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            rating=self.validated_data['rating'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            is_tutor=self.validated_data['is_tutor'],
            is_student=self.validated_data['is_student'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user