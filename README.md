这是一个使用python安装typecho 博客系统的一键脚本

脚本环境部署使用docker服务，这样迁移数据以及再次部署环境非常方便

脚本提供两种安装方式：
1.自动化安装
2.半自动化安装（仅安装环境与部署博客系统）

迁移数据
备份很简单，直接将项目目录整个copy下来即可，恢复时整个文件夹上传到新的服务器，然后进入目录执行docker-compose up -d重新跑起来即可，方便快捷

使用的docker-typecho项目：
https://github.com/dtaliy/docker-typecho.git
里面有较为详细的关于本脚本使用docker的使用说明
