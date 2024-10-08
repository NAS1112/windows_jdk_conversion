# JDK 切换脚本

## 脚本功能

`jdk切换.py` 是一个用于在 Windows 系统上切换 JDK 版本的 Python 脚本。该脚本能够读取配置文件 `jdk_paths.txt`，并根据用户的选择更新系统的 JDK 环境变量和注册表设置。

## 脚本要求

- Python 3.x
- 管理员权限

## 文件结构

- `jdk切换.py` - 主脚本文件
- `jdk_paths.txt` - JDK 路径配置文件

## `jdk_paths.txt` 文件格式

配置文件 `jdk_paths.txt` 应包含 JDK 版本和路径的映射，每行的格式如下：

11=D:\java11 

1.8=D:\java8

17=D:\java17

- 以 `#` 开头的行是注释，脚本会跳过这些行。
- 每行应包含一个 JDK 版本和对应的路径，版本与路径之间用 `=` 分隔。

## 使用说明

1. 确保脚本文件和配置文件在同一目录下。
2. 以管理员权限运行脚本。可以通过以下命令在命令行中运行：

    ```shell
    python jdk切换.py
    ```

3. 选择 JDK 版本。脚本会显示一个菜单供您选择需要切换的 JDK 版本。输入相应的选项编号并按回车。

4. 脚本将更新系统环境变量和注册表设置。脚本会提示操作结果和当前 JDK 版本。

5. 如果配置文件不存在或内容无效，脚本会提示文件的正确格式，并要求检查 `jdk_paths.txt` 文件。



