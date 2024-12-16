from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Create your models here.
class hexaOrder(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    username = models.CharField(db_column='UserName', max_length=50)
    project_name = models.CharField(db_column='ProjectName', max_length=50)
    datetime = models.DateTimeField(db_column='DateTime', auto_now_add=True)
    algorithms = models.IntegerField(db_column='Algorithms', default=0)
    success = models.IntegerField(db_column='Success', default=0)

    class Meta:
        managed = False  # Django가 이 테이블을 관리하지 않음
        db_table = 'orders'  # MariaDB에 있는 테이블 이름을 명시
    
    def __str__(self):
        return f"Order {self.id}: {self.username} - {self.project_name}"  # 문자열 반환

class hexaUser(models.Model):
    user = models.CharField(db_column='User', max_length=50, unique=True, primary_key=True, default='NULL')
    password = models.CharField(db_column='Password', max_length=256, default='NULL')
    level = models.IntegerField(db_column='Level', default=0)
    serial_number = models.CharField(db_column='SerialNumber', max_length=50, default='HCYYYYMMDD-NNNN')
    # expired_date = models.DateTimeField(db_column='ExpiredDate', default='9999-12-31 23:59:59')   
    expired_date = models.CharField(db_column='ExpiredDate', max_length=19, default='9999-12-31 23:59:59')
    # expired_date = models.DateTimeField(db_column='ExpiredDate', default=datetime(2099, 12, 31, 23, 59, 59))

    class Meta:
        managed = False  # Django가 테이블을 관리하지 않음
        db_table = 'users'  # MariaDB에 있는 테이블 이름을 명시
    
    def __str__(self) :
        return self.user
    
class hexaModelWeight(models.Model):
    user_name = models.CharField(max_length=50, primary_key=True, db_column='UserName')
    heart_seg = models.CharField(max_length=50, default='heartseg.pth', db_column='HeartSeg')
    lung_seg = models.CharField(max_length=50, default='lungseg.pth', db_column='LungSeg')
    liver_seg = models.CharField(max_length=50, default='liverseg.pth', db_column='LiverSeg')
    spine_seg = models.CharField(max_length=50, default='spineseg.pth', db_column='SpineSeg')
    breast_seg = models.CharField(max_length=50, default='breastseg.pth', db_column='BreastSeg')
    thyroid_seg = models.CharField(max_length=50, default='thyroidseg.pth', db_column='ThyroidSeg')

    class Meta:
        managed = False  # Django가 테이블을 관리하지 않음
        db_table = 'model_weight'  # MariaDB에 있는 테이블 이름을 명시

    def __str__(self):
        return self.user_name

class hexaSessionUsers(models.Model):
    peer = models.CharField(db_column='Peer', max_length=50, primary_key=True)
    user_name = models.CharField(db_column='UserName', max_length=50, default='NULL')
    session_time = models.DateTimeField(db_column='SessionTime', auto_now_add=True)
    duplicated = models.BooleanField(db_column='Duplicated', default=False)

    class Meta:
        managed = False  # Django가 테이블을 관리하지 않음
        db_table = 'session_users'  # MariaDB에 있는 테이블 이름을 명시
        unique_together = (('peer', 'user_name'),)  # 복합 기본 키 설정

    def __str__(self):
        return f"{self.peer} - {self.user_name}"

class hexaServer(models.Model):
    host = models.CharField(max_length=20, db_column='Host')
    port = models.IntegerField(db_column='Port')

    class Meta:
        managed = False  # Django가 테이블을 관리하지 않음
        db_table = 'servers'  # MariaDB에 있는 테이블 이름을 명시
        unique_together = (('host', 'port'),)  # 복합 키 설정

    def __str__(self):
        return f"{self.host}:{self.port}"