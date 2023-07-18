-- create movies table
create table if not exists movies (
	id int primary key,
	name varchar(64),
	release_date date
);

-- create category table
create table if not exists category (
	category_id int primary key,
	category varchar(100)
);


-- insert into movies
insert into movies 
values
	(1, 'Deep blue sea 2', '2018-02-28'),
	(2, 'The Meg', '2018-07-10'),
	(3, 'The Meg 2', '2023-07-04');


-- select one item
select name, release_date from movies where id=2;


-- add column category_id to movies table
alter table movies 
add column
	category_id int;

-- add constraint foreign key to movies
alter table movies 
add constraint fk_moviecategory
foreign key (category_id) references category(category_id);

-- select all items
select * from category;

-- insert into category name values
insert into category 
values 
	(1, 'Action'),
	(2, 'Fantasy'),
	(3, 'Horror');

alter table movies 
add constraint unique_name unique (name);

-- update movies table
update movies 
set category_id = 1
where id = 2;

-- alter table add multiple columns
alter table movies 
add column 
	runtime time,
add column
	rating decimal(4,2),
add column
	box_office bigint,
add column
	created_at timestamp;


-- update film The meg
update movies 
set runtime = '1:50:00', rating = 8.7, box_office = 145443742, created_at = '2018-07-10 12:00:00'
where id = 2;

-- update film deep blue sea
update movies 
set runtime = '2:13:50', rating = 4.0, box_office = 109287365, created_at = '2018-02-28 14:19:10'
where id = 1;

-- update film The meg 2
update movies 
set runtime = '2:30:00', rating = 8.9, box_office = 189032932, created_at = '2018-07-04 18:40:00'
where id = 3;


select * from movies order by release_date;
