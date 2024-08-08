import os
import subprocess
import sys
import ctypes
import winreg

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

def run_as_admin():
    if not is_admin():
        print("请求管理员权限...")
        try:
            script = os.path.abspath(sys.argv[0])
            params = ' '.join([script] + sys.argv[1:])
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        except Exception as e:
            print(f"无法提升权限: {e}")
            sys.exit(1)
        sys.exit(0)
    else:
        print("已获得管理员权限")

def clean_path():
    print("正在清理旧的JDK路径...")
    path = os.environ['PATH']
    new_path = ';'.join([p for p in path.split(';') if not p.startswith("D:\\java")])
    os.environ['PATH'] = new_path

def set_java(version, java_home):
    os.environ['JAVA_HOME'] = java_home
    os.environ['JRE_HOME'] = java_home
    os.environ['PATH'] = f"{java_home}\\bin;" + os.environ['PATH']
    update_registry(version)
    update_user_env(java_home)
    show_java_version(version)

def update_registry(version):
    print("更新注册表中的Java版本信息")
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\JavaSoft\Java Development Kit", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "CurrentVersion", 0, winreg.REG_SZ, version)
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\JavaSoft\Java Runtime Environment", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "CurrentVersion", 0, winreg.REG_SZ, version)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"更新注册表时出现错误：{e}")

def update_user_env(java_home):
    print("更新用户环境变量")
    subprocess.run(['setx', 'JAVA_HOME', java_home, '/m'], shell=True)
    subprocess.run(['setx', 'JRE_HOME', java_home, '/m'], shell=True)
    subprocess.run(['setx', 'PATH', f"{java_home}\\bin;{os.environ['PATH']}", '/m'], shell=True)

def show_java_version(version):
    print(f"已切换到JDK {version}")
    print("当前Java版本：")
    try:
        subprocess.run(["java", "-version"], shell=True)
    except Exception as e:
        print(f"执行 java -version 时出现错误：{e}")

def read_jdk_paths(file_path):
    jdk_paths = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    version, path = line.split('=', 1)
                    jdk_paths[version.strip()] = path.strip()
    except FileNotFoundError:
        print(f"未找到文件: {file_path}")
    except Exception as e:
        print(f"读取文件时出错: {e}")
    return jdk_paths

def show_menu(jdk_paths):
    print("=============================================")
    print("请选择要切换的JDK版本")
    for i, version in enumerate(jdk_paths.keys(), 1):
        print(f"{i}: Java JDK {version}")
    print(f"{len(jdk_paths) + 1}: 取消")
    print("=============================================")
    try:
        choice = int(input("请选择："))
        if 1 <= choice <= len(jdk_paths):
            version = list(jdk_paths.keys())[choice - 1]
            clean_path()
            set_java(version, jdk_paths[version])
        elif choice == len(jdk_paths) + 1:
            sys.exit(0)
        else:
            print("无效选择，请重新选择。")
            show_menu(jdk_paths)
    except ValueError:
        print("无效选择，请输入数字。")
        show_menu(jdk_paths)

def main():
    run_as_admin()
    jdk_paths = read_jdk_paths("jdk_paths.txt")
    if jdk_paths:
        show_menu(jdk_paths)
    else:
        print("没有可用的JDK路径，请检查 jdk_paths.txt 文件是否存在并包含有效的路径。")
        print("示例 jdk_paths.txt 内容：")
        print("# 这是注释")
        print("版本号=jdk路径")
        print("例:")
        print("17=D:\\java17")
        input("按任意键退出...")
        sys.exit(1)

if __name__ == "__main__":
    main()
