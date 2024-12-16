# BackEnd/HEXA_V1/Dockerfile
FROM python:3.10

WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# Docker CLI 설치
RUN apt-get update && apt-get install -y docker.io

# 소스 복사
COPY . .

# Django 서버의 기본 포트
EXPOSE 8000

# gunicorn을 사용하여 Django 애플리케이션을 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "hexa_core.wsgi:application"]