# jdk_conversion
JDK 切换脚本
脚本功能
jdk切换.py 是一个用于在 Windows 系统上切换 JDK 版本的 Python 脚本。该脚本能够读取配置文件 jdk_paths.txt，并根据用户的选择更新系统的 JDK 环境变量和注册表设置。

脚本要求
Python 3.x
管理员权限
文件结构
jdk切换.py - 主脚本文件
jdk_paths.txt - JDK 路径配置文件
jdk_paths.txt 文件格式
配置文件 jdk_paths.txt 应包含 JDK 版本和路径的映射，每行的格式如下：

# 这是注释
11=D:\java11
1.8=D:\java8
17=D:\java17
以 # 开头的行是注释，脚本会跳过这些行。
每行应包含一个 JDK 版本和对应的路径，版本与路径之间用 = 分隔。
使用说明
确保脚本文件和配置文件在同一目录下。

以管理员权限运行脚本。可以通过以下命令在命令行中运行：


python jdk切换.py
选择 JDK 版本。脚本会显示一个菜单供您选择需要切换的 JDK 版本。输入相应的选项编号并按回车。

脚本将更新系统环境变量和注册表设置。脚本会提示操作结果和当前 JDK 版本。

如果配置文件不存在或内容无效，脚本会提示文件的正确格式，并要求检查 jdk_paths.txt 文件。

示例
正确的 jdk_paths.txt 文件内容

# 这是注释
11=D:\java11
1.8=D:\java8
17=D:\java17
脚本运行结果示例
plaintext
复制代码
已获得管理员权限
=============================================
请选择要切换的JDK版本
1: Java JDK 11
2: Java JDK 1.8
3: Java JDK 17
4: 取消
=============================================
请选择：1
正在清理旧的JDK路径...
更新注册表中的Java版本信息
更新用户环境变量
已切换到JDK 11
当前Java版本：
java version "11.0.1"
...
错误提示示例
plaintext
复制代码
未找到文件: jdk_paths.txt
没有可用的JDK路径，请检查 jdk_paths.txt 文件是否存在并包含有效的路径。
示例 jdk_paths.txt 内容：
# 这是注释
11=D:\java11
1.8=D:\java8
17=D:\java17
按任意键退出...
通过以上说明，您可以配置和运行 JDK 切换脚本，并根据需求调整 JDK 路径和版本。
