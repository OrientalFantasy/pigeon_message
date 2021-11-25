# 代码太乱了，时间匆忙请见谅



# 引入模块
# import os
import re
import datetime
# configparser 用于读取配置文件
import configparser
# 利用 flask 框架搭建 Web 服务
from flask import Flask
from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker




############################ 配置文件解析 ##################################

config = configparser.ConfigParser()
# 定义配置文件路径
file = "config/config.conf"
# 解析数据库配置文件
config.read(file, encoding='UTF-8')
items = config.items("DATABASE")
host = dict(items)["host"]
port = int(dict(items)["port"])
user = dict(items)["user"]
passwd = dict(items)["passwd"]
db_name = dict(items)["db_name"]

########################## 使用ORM来操作数据库 ##############################

# 拼接 sqlalchemy 数据库链接地址
mysql_info = "mysql+pymysql://" + user + ":" + passwd + "@" + host + ":"+ str(port) + "/" + db_name

# 初始化数据库连接:
engine = create_engine(mysql_info)
Base = declarative_base(engine)  # SQLORM基类
session = sessionmaker(engine)()  # 构建session对象


class Twitter(Base):
    __tablename__ = 'twitter'  # 表名
    nick = Column(String(16))
    twitter = Column(String(3200))
    time = Column(String(20), primary_key=True) # 设置主键

Base.metadata.create_all()  # 将模型映射到数据库中





# 利用 re.sub 对邮件模板关键位置字符进行替换
# 语法 re.sub(替换前的字符, 替换后的字符, 需要进行替换操作的字符串)
replace = re.sub


app = Flask(__name__)

# 解决ajax跨域问题 设置 Access-Control-Allow-Credentials: true
# CORS(app, supports_credentials = True)


# 主页 GET 回应
@app.route('/', methods=['GET'])

def home():
    return render_template('index.html')

# 关于页 GET 请求回应
@app.route('/about', methods=['GET'])

def about():
    return render_template('about.html')

# 留言页 GET 请求回应
@app.route('/twitter', methods=['GET'])

def twitter():

    twitter_template = """<div class="mdui-card" style="border-radius: 25px; margin-top: 0.5cm; margin-bottom: 0.5cm; background-color:rgba(240,248,255,0.5);">

    <!-- 卡片头部，包含头像、标题、副标题 -->
    <!--div class="mdui-card-header"-->
      <!-- 用户头像，来不及写了 -->
      <!-- <img class="mdui-card-header-avatar" src="/static/img/avatar-1.jpeg"/> -->
      <!-- <div class="mdui-card-header-title">东方幻梦</div> -->
      <!--div style="font-size: 135%;">ni_ck</div-->
      <!-- 用户个性签名，来不及写了 -->
      <!-- <div class="mdui-card-header-subtitle">只是当时已惘然。</div> -->
    <!--/div-->
    <div style="font-size: 135%; margin-top: 0.5cm; margin-left: 0.5cm;">ni_ck</div>
  
    <!-- 卡片的媒体内容，可以包含图片、视频等媒体内容，以及标题、副标题 -->
    <div class="mdui-card-media">
      <!-- 由于时间原因，图片上传写不完了，先实现功能吧 -->
      <!-- <img src="/static/img/card.jpg"/> -->
  
      <!-- 卡片中可以包含一个或多个菜单按钮 -->
      <div class="mdui-card-menu">
        <button class="mdui-btn mdui-btn-icon mdui-text-color-white"><i class="mdui-icon material-icons">share</i></button>
      </div>
    </div>
  
    <!-- 卡片的标题和副标题 -->
    <div class="mdui-card-primary">
      <!-- <div class="mdui-card-primary-title">「小仓百人一首」之一</div> -->
      <div class="mdui-card-content" style="font-size: 125%; margin-right: 15px; margin-left: 15px">twit_ter</div>
      <div class="mdui-card-primary-subtitle" style="text-align: right; margin-right: 15px;  margin-top: 15px;">ti_me</div>
    </div>
  
    <!-- 卡片的内容 -->
    <!-- <div class="mdui-card-content" style="margin-right: 15px; margin-left: 15px">玉の绪よ 绝えなば绝えね ながらへば 忍ぶることの よわりもぞする。</div> -->
  
    <!-- 卡片的按钮 -->
    <!-- <div class="mdui-card-actions" style="text-align: right;"> -->
      <!-- <button class="mdui-btn mdui-ripple"><i class="mdui-icon material-icons">sentiment_satisfied</i> 赞</button> -->
      <!-- <button class="mdui-btn mdui-ripple"><i class="mdui-icon material-icons">sentiment_dissatisfied</i> 踩</button> -->
      <!-- <button class="mdui-btn mdui-btn-icon mdui-float-right"><i class="mdui-icon material-icons">expand_more</i></button> -->
    <!-- </div> -->
  
    </div>
    """
    # 查询数据库
    # 对 time 字段进行降序排序后获取表内所有数据 DESC表示降序，ASC表示升序
    item_list = session.query(Twitter).order_by(Twitter.time.desc()).all() 
    # 计算留言数量
    # count = session.query(Twitter).count()

    body = ""
    body_data = ""

    for item in item_list:
        nick = item.nick
        twitter = item.twitter
        time = str(item.time)
        body_data = replace('ni_ck', nick, twitter_template)
        body_data = replace('twit_ter', twitter, body_data)
        body_data = replace('ti_me', time, body_data)
        body += body_data
    
    # 这是一个十分怪异的页面渲染方式（由于我不会写js不然早用ajax了
    return render_template('twitter.html', body = body)

# 写留言 GET 请求回应
@app.route('/new_twitter', methods=['GET'])

def new_twitter():
    return render_template('new_twitter.html')


# 写留言 POST 请求回应
@app.route('/new_twitter', methods=['POST'])

def post_twitter():
    
    nick = request.form['nick']
    twitter = request.form['twitter']
    if nick == "" and twitter == "":
        print("昵称或者留言为空！")
        
    else:
        # 格式化时间
        timestr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("留言成功 时间：" + timestr)
        twitter_info = Twitter(nick=nick, twitter=twitter,time = timestr)  # 创建一个student对象
        session.add(twitter_info)  # 添加到session
        session.commit()  # 提交到数据库

    return redirect(url_for('twitter'),code = 302)



if __name__ == '__main__':
    app.run()