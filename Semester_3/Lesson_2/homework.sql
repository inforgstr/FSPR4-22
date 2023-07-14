CREATE TABLE IF NOT EXISTS friends (
	id integer primary key,
	name text not NULL,
	birthday date not NULL
);

INSERT into friends 
	(name, birthday) 
VALUES 
	("James Monro", "1940-03-30"),
	("John", "2000-05-13"),
	("Emma Walter", "1889-10-18");


UPDATE friends SET name="Flash" where name="James Monro";

alter table friends add column email text;

DELETE FROM friends where name="James Monro";

UPDATE friends set email="example@email.com" where name="Flash";
UPDATE friends set email="root@root.com" where name="John";
UPDATE friends set email="emma@emma.com" where name="Emma Walter";

select * from friends;
