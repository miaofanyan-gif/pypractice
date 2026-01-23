import os

from dotenv import load_dotenv
from flask import Flask, render_template

# 加载环境变量
# 第一步：加载 .env（必须在导入其他模块之前）
current_file = os.path.abspath(__file__)
project_root = os.path.dirname(current_file)
env_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path=env_path)





from app import create_app


print(os.getenv('DB_USER'))

app_env = os.getenv('FLASK_ENV', 'development')

app = create_app(app_env)


@app.route('/')
def helo_world():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
