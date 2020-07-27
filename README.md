# 会战名次查询插件 for HoshinoBot

A [HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot) based [PCR](http://priconne-redive.jp/) plugin which can get the current clan rank or history clan rank from database.


## 简介

基于 [HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot) 和 [镜华-公会战排名查询](https://kengxxiao.github.io/Kyouka/) 制作的机器人插件。

机器人会查询指定公会当前或者历史能查到的全部会战名次并发送到QQ群中。



## 功能介绍

目前只有一条语句，输入“clanrank”进行查询。

- **clanrank <公会名>**：查询公会最新的会战名次。

- **clanrank <公会名> all**：查询公会全部的会战名次。


## 安装方式

1. clone或者下载此仓库的代码

2. 将`clanrank`文件夹放入`hoshino/modules/`文件夹中

3. 打开`hoshino/config/`文件夹中的`__bot__.py`文件，在`MODULES_ON`中加入一行`'clanrank',`