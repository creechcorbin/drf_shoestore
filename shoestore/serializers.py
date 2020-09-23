from rest_framework import serializers
from shoestore.models import Shoe

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'id',
            'size',
            'brand',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type',
        ]

# As a boy living on the African Savanna Joe Kaufield would train elephants to not only scare intruders 
# off his camp, but also paint psuedo forensic sketches allowing Joe Kaufield to profile and hunt the perpetrators.
# Elephants never forget... and neither does Joe Kaufield.