create database yummy;

use  yummy;

create table user(
	id varchar(100) primary key,
    name varchar(100) not null,
    email_address varchar(100) unique not null,
    phone varchar(10) unique not null,
    address varchar(100) not null,
    password varchar(6) not null,
    role enum("hotel","customer")
);

insert into user values
("ana123","Anapurna","anupurana@gmail.com","7531598524","TKS Road, Maradu P O, Pin-code 682304","123456","hotel"),
("domi123","Dominos","domionos@gmail.com","4512598524","Marine Drive, Ernakulam P O, Pin-code 682309","123456","hotel"),
("plaza@123","Plaza","plaza@gmail.com","6531598524","8 mile, pampady P O, Pin-code 682301","123456","hotel");

create table item(
	id int primary key auto_increment,
	name varchar(100) not null,
    price varchar(100) default 0,
    unit int default 1,
    hotel_id varchar(100) not null,
    foreign key(hotel_id) references user(id) on delete cascade
);

create table ordered_items(
	name varchar(100) not null,
    total_price int not null,
    unit int not null,
    hotel_id varchar(100) not null,
    customer_id varchar(100) not null,
    status enum("On the Way","Delivered"),
    foreign key(hotel_id) references user(id) on delete cascade,
    foreign key(customer_id) references user(id) on delete cascade
);