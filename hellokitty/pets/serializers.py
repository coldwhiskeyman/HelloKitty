from rest_framework import serializers

from pets.models import Pet


class PetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    deleted = serializers.HiddenField(default=False)

    class Meta:
        model = Pet
        fields = ['name', 'age', 'adoption_date', 'weight', 'height', 'details', 'owner', 'deleted']
