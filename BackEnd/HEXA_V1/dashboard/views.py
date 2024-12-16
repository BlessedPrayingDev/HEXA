from django.shortcuts import render
from .models import hexaOrder, hexaUser, hexaSessionUsers, hexaModelWeight, hexaServer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from dashboard.serializers import CreateHexaUserSerializer, CreateHexaOrderSerializer, CreateHexaSessionUserSerializer
import subprocess

# Create your views here.
# 헥사 유저들 정보 가져오기
class GetHexaUsers(APIView) :
    def get(self, request) : 
        users = hexaUser.objects.all()
        serializer = CreateHexaUserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

# 헥사 Order 정보 가져오기
class GetHexaOrders(APIView):
    def get(self, request):
        # request.data에서 username을 가져옵니다. 없으면 None으로 설정
        username = request.query_params.get('username', None)
        
        # username이 있으면 해당 username으로 필터, 없으면 전체 조회
        if username:
            orders = hexaOrder.objects.filter(username=username)
        else:
            orders = hexaOrder.objects.all()
        
        serializer = CreateHexaOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# 헥사 세션 유저 정보 가져오기
class GetHexaSessionUsers(APIView) :
    def get(self, request) : 
        users = hexaSessionUsers.objects.all()
        serializer = CreateHexaSessionUserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

# 헥사 유저 등록
class RegisterHexaUser(APIView) : # 목적: 사용자가 보낸 데이터를 저장하는 것
    def post(self, request):
        serializer = CreateHexaUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
# 유저 정보 추가
class HexaUserInfoUpdate(APIView):
    def patch(self, request): # 보통 put 보다 patch를 자주 사용
        # 전체 request 정보를 콘솔에 출력
        print("Request Data:", request.data)           # 요청 본문 (body)
        print("Request Headers:", request.headers)     # 요청 헤더
        print("Request User:", request.user)           # 인증된 사용자 정보
        print("Request Auth:", request.auth)           # 인증 정보 (토큰 등)

        user_id = request.data.get("user")
        user = hexaUser.objects.get(user=user_id)

        new_username = request.data['user']
        new_level = request.data['level']
        new_serialNumber = request.data['serial_number']
        new_expiredDate = request.data['expired_date']

        user.user = new_username
        user.level = new_level
        user.serial_number = new_serialNumber
        user.expired_date = new_expiredDate

        user.save() # DB 저장 

        return Response({
                "message": "User info update success!!!!!!",
                "data": {
                    "Username": user.user,
                    "Level": user.level,
                    "Serial Number": user.serial_number,
                    "Expired Date": user.expired_date
                }
            }, status=status.HTTP_200_OK)

# 헥사 유저 삭제
class DeleteHexaUser(APIView):
    # permission_classes = [AllowAny]  # 인증(액세스 토큰) 없이 접근 허용

    def delete(self, request):
        username = request.data.get("user")  # 요청 데이터에서 유저 이름을 받아옴

        if not username:
            return Response({"Message": "Username is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = hexaUser.objects.get(user=username)  # 유저 검색
            user_info = user.user  # 삭제 전에 유저 정보를 저장
            user.delete()  # 유저 삭제

            return Response({
                "Message": "User info delete success!!!!",
                "data": {
                    "user": user_info
                }
            }, status=status.HTTP_200_OK)

        except hexaUser.DoesNotExist:
            return Response({"Message": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)

# 현재 실행 중인 Docker 컨테이너 목록을 가져오는 뷰
class GetDockerContainers(APIView):
    def get(self, request):
        try:
            # 'docker container ls' 명령어 실행, 포맷을 지정해 깔끔하게 데이터 분리
            result = subprocess.run(
                ["docker", "container", "ls", "--format", "{{.ID}}|{{.Image}}|{{.Command}}|{{.CreatedAt}}|{{.Status}}|{{.Ports}}|{{.Names}}"],
                capture_output=True,
                text=True,
                check=True
            )
            output = result.stdout.strip()  # 명령어의 출력 결과

            # 출력 데이터를 JSON 형식으로 정리
            containers = []
            for line in output.splitlines():
                columns = line.split('|')  # | 구분자로 분리
                container_info = {
                    "Container ID": columns[0],
                    "Image": columns[1],
                    "Command": columns[2],
                    "Created": columns[3],
                    "Status": columns[4],
                    "Ports": columns[5] if columns[5] else "None",
                    "Names": columns[6]
                }
                containers.append(container_info)

            return Response({"containers": containers}, status=status.HTTP_200_OK)

        except subprocess.CalledProcessError as e:
            # 에러 발생 시 예외 처리
            return Response({"error": "Failed to retrieve Docker containers", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
