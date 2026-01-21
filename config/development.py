import os


class DevelopmentConfig():

    """开发环境配置"""
    DEBUG = True
    # 本地数据库配置
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME_DEV')}?charset=utf8mb4"
    SQLALCHEMY_ECHO = False  # 打印生成的 SQL 语句，便于调试
