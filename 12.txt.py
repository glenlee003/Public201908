练习：
    创建数据库books，默认编码utf8
    数据库中创建表book
    表的字段如下： id title(书名) author(作者) pulication(出版社)
                 price(定价) comment(备注)
(id int primary key auto_increment, titel varchar(64) not null, author varchar(32) not null, publication enum("中国教育", "机械工业","中国邮电","人民教育","中国文学"), price float unsigned, comment text default 0.0);
    插入若干数据
    规定：定价区间 30～～75
    出版社：中国教育
           机械工业
           中国邮电
           人民教育
           中国文学
    作者：老舍
         钱钟书
         鲁迅
         张爱玲
         金庸
         三毛
    查找：
        所有40多元的书，只看书名、作者、价格
        查找老舍写的，同时是中国教育出版的书
        查找备注不是空的记录
        查找价格大于60元或者作者是鲁迅的书，只看作者、书名和价格
