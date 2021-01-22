# PKU自动云战"疫"

PKU自动云战"疫"小工具，使用了python自带的`requests`库，结合Github Action与Server酱，辅导员再也不用担心我漏填了~

## 内容列表

- [说明](#说明)
- [安装](#安装)
- [使用说明](#使用说明)
- [相关仓库](#相关仓库)
- [使用许可](#使用许可)

## 说明

* 本工具采用 Python3 并使用了系统自带库`requests`进行。
* 本想采用`selenium`的方式进行模拟，但是觉得selenium速度太慢，占用资源大，且不够优雅。经过对网站的解析后得到了以下方法（没有反爬就很爽）。
* 支持所有系统（毕竟只用了`requests`）。
* 运行贼快，综合只需要2秒不到。
* 喜欢可以点个`Star`?

## 安装

这个项目使用 Python3，并未使用三方库。请确保你本地安装了 Python。

## 使用说明

### 获取FORM数据
* 使用前需手动进入云战役填写一次：
  1. 在云战"疫"页面，将需要填写的信息填写完成，点击保存。
  2. 输入`ctrl+shift+i`进入开发者工具。
  3. 在开发者工具的`Console`一栏中输入`copy(JSON.stringify({xh: app.basicInfoForm.xh,sfhx: app.dailyInfoForm.sfhx,hxsj: app.dailyInfoForm.hxsj,cfdssm: app.dailyInfoForm.cfdssm,cfddjsm: app.dailyInfoForm.cfddjsm,cfdxjsm: app.dailyInfoForm.cfdxjsm,dqszdxxdz: app.dailyInfoForm.dqszdxxdz,dqszdsm: app.dailyInfoForm.dqszdsm,dqszddjsm: app.dailyInfoForm.dqszddjsm,dqszdxjsm: app.dailyInfoForm.dqszdxjsm,dqszdgbm: app.dailyInfoForm.dqszdgbm,sflsss: app.dailyInfoForm.sflsss,jrtw: app.dailyInfoForm.jrtw,sfczzz: app.dailyInfoForm.sfczzz,jqxdgj: app.dailyInfoForm.jqxdgj,qtqksm: app.dailyInfoForm.qtqksm,tbrq: app.dailyInfoForm.tbrq,yqzd: app.dailyInfoForm.yqzd,sfcx: app.dailyInfoForm.sfcx,dwdzxx: app.locationInfo,dwjd: app.dwjd,dwwd: app.dwwd,sfdrfj: app.dailyInfoForm.sfdrfj,chdfj: app.dailyInfoForm.chdfj,jkm: '绿码',simstoken: simstoken,sfmjqzbl: app.dailyInfoForm.sfmjqzbl,sfmjmjz: app.dailyInfoForm.sfmjmjz,hsjcjg: app.dailyInfoForm.hsjcjg,jjgcsj: app.dailyInfoForm.jjgcsj,sfzgfxdq: app.dailyInfoForm.sfzgfxdq}).replaceAll("\"", "\"\"\""))`
  4. 此时云战"疫"的FORM数据便保存在了剪贴板中，保存下来，稍后要用。

### 本地使用

```
git clone https://github.com/Littlebus/PKU-auto-epidemic-fighter.git
cd PKU-auto-epidemic-fighter
python main.py -u [你的学号] -p [你的密码] -f [刚才得到的FORM数据] [--sckey server酱sckey]
```

### Github Actions

使用Github Actions可以免去繁琐的操作，需以下几步便可每日定时填报。
* 点击右上角 `Fork` 项目；
* `Settings` -> `Secrets` 中添加学号、密码、表单以及Server酱SCKEY(选填)；
	- `USERNAME`：学号
	- `PASSWORD`：密码
	- `FORM`：FORM数据
	- `SCKEY`：Server酱SCKEY(选填)
* 点击`Star`，任务会自动执行(默认早8点)，运行进度和结果可以在`Actions`页面查看；
* 或者在Actions页面中点击`Run WorkFlow`，运行进度和结果可以在`Actions`页面查看；
* 如果配置了Server酱，运行结果会推送到微信；

## 获取Server酱SCKEY

* github 授权登录[Server酱](http://sc.ftqq.com/3.version)官网；
* 菜单栏点击`微信推送`，并扫描绑定微信；
* 菜单栏点击`发送消息`，拷贝SCKEY；

## 相关仓库

- [PKUAutoSubmit](https://github.com/YOUSIKI/PKUAutoSubmit) — 从中受到启发。


## 责任须知

* 本项目仅供参考学习，造成的一切后果由使用者自行承担。
* 本项目仅在日常无发热情况时的默认填写，若出现发热症状，请自行进入系统填写。

## 使用许可

[GPL3](LICENSE) © Littlebus