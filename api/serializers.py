from rest_framework import serializers

from todo.models import Todo
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'first_name', 'last_name', 'bio')


class TodoSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)

    class Meta:
        model = Todo
        fields = ('profile', 'id', 'title', 'description', 'completed')
