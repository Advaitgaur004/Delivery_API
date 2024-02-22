from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.core.validators import EmailValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(
        max_length=35,
        required=False,
        help_text="Add your Email which contain '@'",
        validators=[EmailValidator(message="Invalid email address.")]
    )

    phone_number = PhoneNumberField(help_text="Write Phone Number")
    
    password = serializers.CharField(
        min_length=8,
        validators=[validate_password],
        help_text="Enter your password (at least 8 characters).",
    )

    class Meta:
        model = User
        fields = ['username','email','phone_number','password']

    def validate(self, attrs):
        return super().validate(attrs)