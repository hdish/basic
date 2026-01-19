


/*
条件查询，格式为：
    select..．from 数据表名 where 条件;
条件查询，几种写法，即：where后边可以跟什么：
    比较运算符：>，≥，<，≤，=，≠，
    范围查询：
        区间校验：between 起始值 and 结束值      包左包右
        固定值校验：列名 in（值1，值2...）
    模糊查询：   列名 like '_%'    _表示任意的1个字符，%表示多个任意的字符。
    非空查询：   is null 和 is not null
    逻辑运算符： and，or，not
*/

-- 建库，切库，查表
drop database if exists day2;
create database day2;
use day2;
show tables;

-- 建表
create table teacher(
    id int primary key auto_increment,  #id，主键约束（非空，唯一）
    name varchar(10) not null ,         #name，非空约束，必须传值，不能是null
    phone varchar(20) unique,           #手机号，唯一约束，不能重复
    address varchar(20) default '北京'   #地址，默认北京
);

-- 添加数据
insert into teacher values (null,'萧炎',123456789,'斗气大陆');
insert into teacher values (null,'海波东',123456); -- 报错，不写列名默认全列名，值的个数要和列数匹配
insert into teacher values (10,'时代',34567,'斗气大陆');

insert into teacher(name) values ('药尘');
-- 查看表结构，表数据
desc teacher;
select * from teacher;

create table product(
  pid int primary key auto_increment ,
  pname varchar(20),
  price double,
  cate_gory varchar(30)
);

insert into product values (null,'联想',5000,'c001');
insert into product values (null,'观点',356,'c002');
insert into product values (null,'是否',568,'null');
insert into product values (null,'单个',2000,'c003');
insert into product values (null,'改革',3000,'c004');
insert into product values (null,'回归热',4000,'c002');
insert into product values (null,'和',2000,'c005');
insert into product values (null,'说如果',3000,'null');
insert into product values (null,'然后',750,'c003');
insert into product values (null,'让国人',4500,'c004');
insert into product values (null,'俄国',2000,'c001');

-- 删除表数据
delete from product;  -- 不重置主键id   DML语句
truncate table product;  -- 重置主键id  DDL语句

desc product;
select * from product;   #  *在这里代表所有的列，不是通配符
select pid, pname, price, cate_gory from product;
# select  pname, price+10 as new_price from product;  -- 不改变原表
-- 价格等于2000
select * from product where price=2000;
-- 价格不等于2000
select * from product where price != 2000;
select * from product where price not in (2000);  -- in(值1，值2，值3);满足任一一个即可
-- 价格大于3000
select * from product where price >3000;
select * from product where not price <=3000;
-- 价格2000或3000
select * from product where price=2000 or price=3000;
select * from product where pname like '联%';-- %任意字符  _1个字符
-- 查询没有分类的商品
select * from product where cate_gory is null;
-- 查询有分类的商品
select * from product where cate_gory is not null;

select *from product order by price asc; -- 升序  不写默认升序
select *from product order by price desc ; -- 降序
-- 在price降序的基础上，cate升序
select *from product order by price desc ,cate_gory asc ; -- 降序

# 概述/作用:
#   聚合函数是用来操作某列数据的
# 分类:
# count()功能是:统计表的总行数(总条数)
# max()功能是:最大值，只针对于数字列有效
# min()功能是:最小值，只针对于数字列有效
# sum()功能是:求总和，只针对于数字列有效
# avg()功能是:平均值，只针对于数字列有效.
# 细节：
#     操作某列值用这种方法
# :count(*)，count(列)，count(1)的区别是什么
# 答案:
# 1.是否统计null值。
# count(列):只统计该列的非nuLl值。
# count(*)，count(1):都会统计null值.
# 2.效率问题。
# 从高到低，分别是:count(主键列)>count(1)>count(*)>count(列)

select max(price) as max_price from product;
-- 四舍五入，保留两位小数
select round(3.23444,2); -- 3.23

-- 统计每类商品总价格，只统计单价1000以上的商品，且只显示总价在2000以上的分组信息，
-- 然后按照总价升序排列，求价格最低的那个
select  -- select后面显示哪几列，只能是分组字段或聚合函数
    cate_gory,                  -- 分组字段
    sum(price) as sum_price     -- 该分类商品的总价，聚合函数
from
    product
where
    price>1000                  -- 组前筛选
group by
    cate_gory                   -- 分组
having
    sum_price>2000              -- 组后筛选
order by
    sum_price asc               -- 排序
limit
    0,1;  -- 数据表中每条数据都有自己的编号，编号从0开始

select * from product;

