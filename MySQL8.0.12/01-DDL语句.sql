# --------------DDL语句 操作数据库--------------
-- 1.查看所有数据库
show databases;

-- 2.创建数据库，采用默认码表
-- 格式:create database if not exists 数据库名 charset '码表名'
create database day1;

-- 3.创建数据库采用指定码表：gbk
create database day2 charset 'gbk';

-- 4.创建数据库，如果数据库不存在 (掌握)
-- 如果不存在就创建，存在就什么也不做
create database if not exists day1;

-- 5.查看单个数据库（码表）
show create database day1;
show create database day2;

-- 6.修改数据库码表
alter database day2 charset 'utf8';

-- 7.删除指定数据库
# drop database day2;

-- 8.切库
use day1;

-- 9.查看当前使用的是哪个数据库
select database();

# --------------DDL语句 操作数据表--------------

-- 0.切库
use day1;

-- 1.查看（当前数据库）所有数据表
show tables;

-- 2.创建数据表
/*
格式：
	create table [if not exists] 数据表名(
		字段名数据类型[约束],
		字段名数据类型[约束],
		字段名数据类型[约束]
	);
细节：
    上述的中括号的内容是可选项，写不写都行。

 */
create table if not exists stu(
    id int not null,
    name varchar(20) ,
    gander varchar(10),
    age int

);

# 3.修改表名
alter table stu rename to student;
rename table stu to student;            # 效果同上

# 4.给表新增1列    格式：alter table 表名 add 新列名 数据类型 [约束];
alter table student add address varchar(10) not null;

# 5.修改字段：数据类型，约束.  address varchar(10) => address double
#格式：alter table 表名 modify 旧列名 数据类型［约束］;
alter table student modify address char(10);

# 6.修改字段：列名，数据类型，约束.    address double => desc char(10) 非空约束
#格式：alter table 表名change 旧列名 新列名 数据类型［约束];
alter table student change address `desc` char(10) not null;        #列名如果和关键字重名了，要用反引号``包裹.

# 7.删除某列． 例如：删除 desc 列
# 格式：alter table 表名 drop 旧列名;
alter table student drop `desc`;

-- 查看（单个）数据表中的详细信息（码表）
desc student;

select * from student;


# 删表
drop table student;

