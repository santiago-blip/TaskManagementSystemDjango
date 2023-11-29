from rest_framework import serializers

class ValidatePassword(serializers.Serializer):
    password = serializers.CharField(max_length=30)
    confirmPassword = serializers.CharField(max_length=30)

    def validate(self, data):

        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError({'error':'Passwords must be the same.'})
        return data