# --------------DML语句 操作数据 增--------------
/*
添加表数据，格式如下：
    一次添加1条数据：
        insert into 数据表名（列名1，列名2...）values（值1，值2...）;
        上述格式的语法糖，如果是操作全列，则：可以简写成如下的写法。
        insert into 数据表名 values（值1，值2...）;
    一次性添加多条数据：
        insert into 数据表名（列名1，列名2...) values
            （值1，值2...），
            （值1，值2...），
            （值1，值2...）;
    细节：
    1．列名和值，个数，对应类型等均要匹配.
    2.如果不写列名，默认是：全列名

 */
use day1;

desc student;

-- 1.添加单条数据
insert into student(id,name,gander,age) values (1,'乔峰','男',33);
insert into student(name,age) values ('虚竹',26); #   姓名的约束条件为非空，所有必须要有姓名

-- 2.同时添加多条数据
insert into student values
                        (1,'阿朱','女',26),
                        (3,'道君','男',28),
                        (2,'紫嫣','女',22);

# --------------DML语句 操作数据 改--------------
#格式：update 表名 set 列名1=新值，列名2=新值，列名3=新值...where 条件;
#细节：1．改值的时候，数据类型，个数要匹配。
#     2.进行修改，删除操作时，一定一定一定要加where条件，不然就是针对于全表数据做操作。
update student set id=10,name='迪迦' where id=2;


# --------------DML语句 操作数据 删--------------
/*
格式：
    delete from 表名where 条件;
细节：
    1。删除数据时，一定一定一定要加where条件.
    2.delete from 和 truncate table 都可以一次性清空表数据，那么它们之间有什么区别?
        delete from:
            属于DML语句，用于删除表数据的，不会重置：主键id.
            可以结合事务一起使用.
        truncate table:
            属于DDL语句，用于"清空"表数据的，它相当于把表摧毁了，然后创建1张和该表一模一样的新表。即：会重置之间id，一般不结合事务一起使用。
*/

delete from student where name='阿朱';

-- 简单查询表中的所有数据
select * from student;  -- 默认当前库中的表
select * from day1.student; -- 数据库名.数据表名


/*
约束 介绍：
    概述：
    约束就使用来保证数据的完整性，安全性 和一致性的.分类：
        单表约束：
            主键约束：primary key   特点：非空，唯一，且一般结合自增（自动增长 auto_increment）一起使用.
            非空约束：not null       特点：不能为null，可以重复.
            唯一约束：unique         特点：可以为空，不能重复.
            默认约束：default        特点：如果添加数据时没有给该列指定值，则用默认值。
    多表约束：
        外键约束：foreign key
            特点：外表的外键列不能出现主表的主键列没有的数据。
*/

# 1．建表，英雄表hero(id，name，age，phone，address)
create table hero(
    id int primary key auto_increment,      # id，主键约束(非空，唯一)，自增
    name varchar(20) not null,              #名字，非空约束.
    age int,                                #年龄
    phone varchar(11) unique,               #手机号，唯一约束。
    address varchar(10) default '北京'         # 住址，默认约束
);
#2.查看表数据.
select * from hero;
#3.添加表数据

insert into hero values(null,'乔峰',39,'111','上海');     # 对
insert into hero values(null,'乔峰',39,'222','广州');     # 对
insert into hero values(null, '虚竹', 31, null, '广州');  # 对
insert into hero values(null,'段誉',29,null,'大理');     # 对
insert into hero(id, name) values(null, '小龙女');      # 对

insert into hero values(null, null, 23, '111', '上海');  #报错，姓名不能为空
insert into hero values(null,'乔峰', 39,'111','广州');   #报错，手机号具有唯一性。
insert into hero values(null, '杨过', 26, null);       #报错，值的个数和列的个数不匹配

