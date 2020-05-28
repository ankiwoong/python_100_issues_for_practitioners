import flask
import sys
import os

# 가상환경 확인
print(sys.executable)
print("\n")

# 애플리케이션 디렉터리 구조 정의
cwd = os.getcwd()

app_root = os.path.join(cwd, 'my_flask_app')
app_static = os.path.join(app_root, 'static')
app_templates = os.path.join(app_root, 'templates')

os.makedirs(app_root)
os.makedirs(app_static)
os.makedirs(app_templates)

folder_list = os.listdir(app_root)
print(folder_list)
