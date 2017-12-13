#!/usr/bin/python
# -*- coding: UTF-8 -*-
# created by dq

import os,sys

path = os.getcwd()


# 项目名称
project_name =  "xxx"
# 项目类型
project_type = "xcworkspace"

#蒲公英
api_key = "xx"
user_key = "xx"


# 项目目录
project_path = os.path.dirname(path) + "/" + project_name

# 打包模式
development_mode = "Release"

# archive 文件存放路径
archive_path = "~/Desktop/%s_build/%s" %(project_name,project_name)
archive_name = archive_path + ".xcarchive"
ipa_file_path = "~/Desktop/%s_build/ipa"% project_name


def archiveWorkspace():
	archive_project_type = "" #
	if project_type == "xcworkspace":
		archive_project_type = "workspace"
	else:
		archive_project_type = "project"
	archive_com = "xcodebuild archive -%s %s.%s -scheme %s -configuration %s -archivePath %s  clean archive" % (archive_project_type,project_path,project_type,project_name,development_mode,archive_path)
	os.system(archive_com)

	ipa_com = "xcodebuild -exportArchive -archivePath %s -exportPath %s -exportOptionsPlist info.plist -allowProvisioningUpdates" % (archive_name,ipa_file_path)
	os.system(ipa_com)

def upload_pgyer():
	ipa_path = os.path.expanduser('~') + "/Desktop/%s_build/ipa"% project_name  + "/" + project_name + ".ipa"
	upload_com = "curl -F 'file=@%s' -F 'uKey=%s' -F '_api_key=%s' https://qiniu-storage.pgyer.com/apiv1/app/upload" % (ipa_path,user_key,api_key)
	os.system(upload_com)

	print "上传成功"

		
if __name__ == "__main__":
	archiveWorkspace()
	upload_pgyer()





