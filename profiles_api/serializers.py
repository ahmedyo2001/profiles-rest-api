from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """test api view"""
    name = serializers.CharField(max_length=10)
    