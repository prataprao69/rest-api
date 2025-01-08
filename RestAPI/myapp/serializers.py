from myapp.models import Students
from rest_framework import serializers

class StudentsSerializer(serializers.ModelSerializer):
    # first_name=serializers.CharField(max_length=100)
    # last_name=serializers.CharField(max_length=100)
    # address=serializers.CharField(max_length=200)
    # roll_number=serializers.IntegerField()
    # mobiel=serializers.CharField(max_length=10)

    class Meta:
        model = Students
        fields = '__all__'
        # fields = ['first_name','last_name','address','roll_number','mobile']
    def create(self, validated_data):
        return Students.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.save()
        return instance
        
    