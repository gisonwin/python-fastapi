# 短链项目

#### 背景：

商家为了吸引客户制作的营销页面需要通过短信的形式进行推文。而为了节省短信费用，所以将页面链接改为简短的url。

#### 特点：

- 基于SQLite3数据库来存储短链信息
- 使用SQLAlchemy异步方式处理数据交互
- 可对短链重定向及短链统计
- 可据不同渠道批量生成营销特定短链内容或单一类型短链内容

#### 短链类型：

- 常量短链：一个短链地址对应一个固定长链地址，长链地址是不可变的。
- 变量短链：一个短链地址对应不同的长链地址，长链地址中存在可变的参数



#### 需求描述：

应用程序包括两部分：

- 用户使用侧：用户通过浏览器可以访问短链地址，并可以重定向到对应的长链地址
- 内部管理侧：通过浏览器访问用户登录接口，登录成功后返回对应token；浏览器访问后端批量生产短链接口或创建单一短链API，需要携带对应的token信息。

#### 数据库：

user:

| column     | column_type | description |
| ---------- | ----------- | ----------- |
| id         | integer     |             |
| username   | varchar(20) |             |
| password   | varchar(20) |             |
| created_at | Datetime    |             |

short_url:保存短链映射的长链信息。

| column       | type        | desciption             |
| ------------ | ----------- | ---------------------- |
| id           | integer     | 唯一标识               |
| short_tag    | varchar(20) | 短链标签               |
| short_url    | varchar(20) | 完整短链地址           |
| long_url     | varchar     | 短链对应的完整长链地址 |
| visits_count | integer     | 短链访问次数           |
| created_at   | DATETIME    | 生成时间               |
| created_by   | varchar(20) | 由哪个用户生成         |
| msg_context  | varchar     | 短链包含的群发信息     |

#### 项目结构

- short-chain:项目名称
- api：主要存放编写好的API，包括用户登录和短链访问跳转等路由信息
- config：存放配置信息，包括数据库连接配置等
- db包存放定义连接数据库相关的配置信息及连接数据库相关的实例化对象
- dependencies主要存放相关依赖注入的依赖项
- models包主要存放数据库表中映射的ORM映射类
- schemas：存放各个接口的入参、出参的各个字段的类型定义
- services：存放数据库表中ORM模型类封装好的CRUD操作
- utils：存放项目中使用的工具类
- app.py 定义FastAPI对象以及初始化相关的路由注册操作
- main.py 表示应用程序启动入口文件
- short.db表示当前项目使用的数据库文件。



需要编写的api

- 访问短连后重定向长链的接口
- 单一短链生成接口
- 用户登录接口
- 批量短链生成接口



