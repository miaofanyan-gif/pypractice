# 新建文件 test_port.py，替换目标 IP 后运行
import socket


def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)  # 超时时间 5 秒
    try:
        s.connect((ip, port))
        print(f"端口 {port} 连通！")
        return True
    except:
        print(f"端口 {port} 不通！")
        return False
    finally:
        s.close()


# 调用示例：替换成你的服务器 IP
check_port("127.0.0.1SSSS", 3306)
