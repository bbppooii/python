import os
import sys
import subprocess

print("=" * 50)
print("Allure诊断工具")
print("=" * 50)

# 1. 检查Python版本和路径
print(f"\n1. Python信息:")
print(f"   Python版本: {sys.version}")
print(f"   可执行文件: {sys.executable}")

# 2. 打印PATH环境变量
print(f"\n2. PATH环境变量:")
paths = os.environ.get("PATH", "").split(";")
allure_in_path = False
for i, p in enumerate(paths):
    if p and "allure" in p.lower():
        print(f"   ✅ [{i}] {p}")
        allure_in_path = True
    elif p:
        print(f"   ❌ [{i}] {p[:50]}..." if len(p) > 50 else f"   ❌ [{i}] {p}")

if not allure_in_path:
    print("\n   ⚠️ PATH中未找到allure路径")

# 3. 尝试用where命令查找
print(f"\n3. 使用where命令查找allure:")
try:
    result = subprocess.run(
        ["where", "allure"],
        capture_output=True,
        text=True,
        shell=True
    )
    if result.returncode == 0:
        print(f"   找到: {result.stdout}")
    else:
        print(f"   where命令找不到allure")
        print(f"   错误: {result.stderr}")
except Exception as e:
    print(f"   执行where命令出错: {e}")

# 4. 检查常见安装位置
print(f"\n4. 检查常见安装位置:")
common_paths = [
    r"C:\allure\allure-2.30.0\bin\allure.bat",
    r"C:\allure\allure-2.30.0\bin\allure.cmd",
    r"C:\Program Files\allure\bin\allure.bat",
    r"C:\allure\bin\allure.bat",
    r"D:\allure-2.30.0\bin\allure.bat",  # 你之前显示的路径
    os.path.expanduser("~/allure/bin/allure.bat"),
]

for path in common_paths:
    if os.path.exists(path):
        print(f"   ✅ 存在: {path}")
    else:
        print(f"   ❌ 不存在: {path}")

# 5. 尝试直接调用
print(f"\n5. 尝试直接调用allure:")
try:
    # 方法1：直接调用
    result = subprocess.run(["allure", "--version"],
                            capture_output=True,
                            text=True,
                            shell=True)
    if result.returncode == 0:
        print(f"   ✅ 调用成功: {result.stdout}")
    else:
        print(f"   ❌ 调用失败")
        print(f"      错误码: {result.returncode}")
        print(f"      错误: {result.stderr}")
except Exception as e:
    print(f"   ❌ 调用异常: {e}")

# 6. 尝试用绝对路径
print(f"\n6. 尝试用绝对路径:")
found_allure = None
for path in common_paths:
    if os.path.exists(path):
        found_allure = path
        try:
            result = subprocess.run([path, "--version"],
                                    capture_output=True,
                                    text=True)
            if result.returncode == 0:
                print(f"   ✅ {path} 调用成功: {result.stdout.strip()}")
            else:
                print(f"   ❌ {path} 调用失败")
        except Exception as e:
            print(f"   ❌ {path} 调用异常: {e}")

if not found_allure:
    print("   未找到allure可执行文件")

# 7. 检查系统环境变量
print(f"\n7. 系统环境变量:")
try:
    # 读取系统环境变量
    result = subprocess.run(
        ['powershell', '-Command', '[Environment]::GetEnvironmentVariable("Path", "Machine")'],
        capture_output=True,
        text=True
    )
    if "allure" in result.stdout.lower():
        print("   ✅ 系统PATH中包含allure")
    else:
        print("   ❌ 系统PATH中不包含allure")

    result = subprocess.run(
        ['powershell', '-Command', '[Environment]::GetEnvironmentVariable("Path", "User")'],
        capture_output=True,
        text=True
    )
    if "allure" in result.stdout.lower():
        print("   ✅ 用户PATH中包含allure")
    else:
        print("   ❌ 用户PATH中不包含allure")
except Exception as e:
    print(f"   读取系统环境变量失败: {e}")

# 8. 检查allure-pytest
print(f"\n8. allure-pytest安装情况:")
try:
    import allure
    import pytest

    print(f"   ✅ allure模块可用")
    print(f"   ✅ pytest版本: {pytest.__version__}")
    print(f"   ✅ allure模块路径: {allure.__file__}")
except ImportError as e:
    print(f"   ❌ 导入失败: {e}")

print("\n" + "=" * 50)
print("诊断完成")
print("=" * 50)