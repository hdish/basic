# 场景1：建表时创建，和以前写字段的方式一样。
#     [constraint 外键约束名] foreign key (外键列名) references 主表名 (主键列名)
# 场景2：建表后创建。
#     alter table 表名 add [constraint 外键约束名] foreign key (外键列名) references 主表名 (主键列名)
# 场景3：删除外键约束。
#     alter table 表名 drop foreign key 外键约束名

/*
外键约束详解：
    概述：
        它属于多表约束，用于保证数据的完整性和一致性。
    格式：
        添加外键约束：
            alter table 外表名 add constraint 外键约束名 foreign key(外键列名) references 主表名 (主键列名);
        删除外键约束：
            alter table 外表名 drop foreign key 外键约束名;

 */
-- 1.建库，切库，查库
drop database if exists day3;
create database if not exists day3;
use day3;
show tables ;
-- 2.建表部门表
create table dept(
    id int primary key auto_increment,
    name varchar(10)
);
-- 3.建员工表，
create table employee(
    id int primary key auto_increment,
    name varchar(10),
    salary int,
    dep_id int,
    constraint fk_dept_em foreign key (dep_id) references dept(id)
                     #设置员工表和部门表的外键约束
);
-- 4.给部门添加数据
insert into dept values (null,'人事部'),(null,'财务部'),(null,'研发部');
delete from dept where id>3;

-- 5.给员工添加数据，
insert into employee values (null,'刘备',500,1);
insert into employee values (null,'关于',1000,2);
insert into employee values (null,'张飞',2000,6);
delete from employee where id>3;

-- 6.删表，重新建表，建表时添加外键约束
drop table dept;
drop table employee;
-- 7.手动删除外键约束
alter table employee drop foreign key fk_dept_em;
# alter table employee drop foreign key employee_ibfk_1;
-- 8.手动添加外键约束
alter table employee add foreign key (dep_id) references dept(id);

select * from dept;
select * from employee;


#------------------：多表建表-多对多----------------
#原则：新建中间表，该表至少有2列，充当外键列，分别去关联多的两方的主键列.

#学生表
create table student(
    sid  int primary key auto_increment, # 学生id
    name varchar(10)                     #学生姓名
);
#选修课表
create table course(
    cid    int primary key auto_increment, # 课程
    idname varchar(10)                  #课程名
);

#学生-选修课关系表，即：中间表.
create table stu_cur(
    id  int unique not nuLl auto_increment, # 自身id，伪主键(非空，唯一)，自增
    sid int,                                #学生id
    cid int                                 #选修课id
);

#2．添加外键约束.
#2.1学生表和中间表
alter table stu_cur add constraint fk_stu_mid foreign key (sid) references student(sid);
#2.2课程表和中间表，这个我们不给外键约束起名字了，让程序自动生成.
alter table stu_cur add foreign key (cid) references course(cid);

#3．设置中间表的 学生id（sid）和 选修课id（cid）为：联合主键.
alter table stu_cur add primary key(sid, cid);
#4.添加表数据.
#4.1学生表.
insert into student values(null,'乔峰'),(null,'虚竹'),(null,'段誉');
#4.2选修课表
insert into course values(nuLl,'AI人工智能'),(null,'Py大数据'),(nuLl,'鸿蒙');

#4.3中间表.
insert into stu_cur values(null, 1, 1);     # 乔峰，AI
insert into stu_cur values(null, 1, 2);     # 乔峰，大数据
insert into stu_cur values(null, 2, 1);     # 虚竹，AI
insert into stu_cur values(null, 2, 1);     # 虚竹，AI，报错。

select * from student;
select * from course;




# 创建hero表
create table hero(
    hid int primary key ,
    hname varchar(10),
    kongfu_id int
);
# 创建kongfu表
create table kongfu(
    kid int primary key ,
    kname varchar(10)
);

# 2.添加表数据
# 插入hero数据
insert into hero values (1,'鸠摩智',9),(3,'乔峰',1),(4,'虚竹',4),(5,'段誉',12);
#插入kongfu数据
insert into kongfu values (1,'降龙十八掌'),(2,'乾坤大挪移'),(3,'猴子偷桃'),(4,'天山折梅手');
#3.查看表数据.
select * from hero;     # 英雄表.

select * from kongfu;   # 功夫表


#------------连接查询-------------
# 场景1：内连接，查询结果是：表的交集。
# 显式内连接，select * from A inner join B on 关联条件.
select * from hero h inner join kongfu kf on h.kongfu_id = kf.kid;
select * from hero h join kongfu kf on h.kongfu_id = kf.kid;    # 语法糖，inner可以省略不写.

# 隐式内连接，Select * from A，B where 关联条件.
select * from hero h, kongfu kf where h.kongfu_id = kf.kid;

# 场景2：外连接.
# 左外连接：查询结果是左表全集+交集.
# 格式： select * from A Left outer join B on 关联条件.
select * from hero h left outer join kongfu kf on h.kongfu_id = kf.kid;
select * from hero h left join kongfu kf on h.kongfu_id = kf.kid;   # 语法糖，outer可以省略不写.

# 右外连接：查询结果是右表全集+交集.
# 格式： select * from A right outer join B on 关联条件.
select * from hero h right outer join kongfu kf on h.kongfu_id = kf.kid;
select * from hero h right join kongfu kf on h.kongfu_id = kf.kid;# 语法糖，outer可以省略不写.


# ：-----------------窗口函数-------------
/*
窗口函数介绍：
    概述：
        它是MySQL8.O的特性，窗口函数有很多，常用的有：
        row_number():   可以理解为：行号，即：1，2，3，4..
        rank():         （稀疏)排名，会跳跃．1，2，2，2，5..
        dense_rank()    （密集)排名，不会跳跃．1，2，2，2，3.．
    精髓：窗口函数=给表新增1列，至于新增的是什么，取决于用哪个窗口函数.
    格式：
        窗口函数 over(partition by 分组字段 order by 排序字段 asc | desc)
    细节：
        1．学窗口函数，首先要掌握两个知识点.
            A．分组排名.
            B．分组排名求TopN
       2.where后边写的字段，必须是表中已有的字段。

*/











