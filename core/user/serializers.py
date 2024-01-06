from rest_framework import serializers
from core.user.models import User
from core.abstract.serializers import AbstractSerializer

class UserSerializer(AbstractSerializer):
	# Re-writing some fields like the 'public_id' to be represented as the id of the object
	
	# id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
	# created = serializers.DateTimeField(read_only=True)
	# updated = serializers.DateTimeField(read_only=True)

	class Meta:
		model = User
		# list all the fields that can be included or listed in a request or a response
		fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'avatar', 'email', 'is_active', 'created', 'updated']
		
		# List of all the fields that can only be read_only
		read_only_field = ['is_active']