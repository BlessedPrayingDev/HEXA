from rest_framework import serializers
from django.contrib.auth.hashers import make_password
import hashlib
from dashboard.models import hexaUser, hexaOrder, hexaServer, hexaModelWeight, hexaSessionUsers

class CreateHexaUserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = hexaUser # User 모델 사용
        fields = ['user', 'password', 'level', 'serial_number', 'expired_date'] # hexaUser 모델 내 필드

    def create(self, validated_data):
        # password 필드를 가져와서 sha256으로 해싱
        password = validated_data.pop('password', None)
        
        # 나머지 필드를 이용해 인스턴스 생성
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            # hashlib을 사용하여 비밀번호를 SHA256으로 해싱
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            instance.password = hashed_password
        
        # 새 인스턴스를 저장
        instance.save()
        
        return instance

class CreateHexaOrderSerializer(serializers.ModelSerializer) :
    class Meta :
        model = hexaOrder # User 모델 사용
        fields = ['id', 'username', 'project_name', 'datetime', 'algorithms', 'success'] # hexaOrder 모델 내 필드

class CreateHexaSessionUserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = hexaSessionUsers # User 모델 사용
        fields = ['peer', 'user_name', 'session_time', 'duplicated'] # hexaSessionUsers 모델 내 필드