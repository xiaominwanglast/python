from rest_framework import serializers
from share.models import Share


class Shareserializers(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields= ("team","shareperson","sharetime","sharetitle","shareaddress")