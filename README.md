# iOS-自动打包脚本
iOS自动打包脚本
上传蒲公英

需要修改的地方
*****************************
project_name =  "xx"

project_type = "xcworkspace"

#蒲公英
api_key = "xx"
user_key = "xxx"
*************************
info.plist
************************
profiles
这边的key 为buildID
value 为配置文件的文件名
************************

# 默认设置
1 会在桌面生成 项目名_build 文件夹
2 文件夹中会有生成的 archive文件和打包好的ipa 文件
3 每次运行都会覆盖掉旧的ipa 文件

