/*
 * triggers creation
*/

create table customers_log (
	schema_name varchar(50),
	changed_by varchar(100),
	table_name varchar(150),
	action_name varchar(50),
	time_changed timestamp,
	operation varchar(50)
);


create or replace function on_customers_log() returns trigger as $$ 
	begin
		insert into customers_log 
			(schema_name, changed_by, table_name, action_name, time_changed, operation)
		values
			(
				TG_TABLE_SCHEMA,
				user,
				TG_TABLE_NAME, 
				TG_WHEN,
				date_trunc('minute', NOW()),
				TG_OP
			);
		return new;
	end;
$$ language PLPGSQL;
   
   

create or replace trigger customers_update_insert_delete_log
	after update or insert or delete on address 
	for each row
	execute procedure on_customers_log();

   
update address 
set state = 'MA'
where id = 1;


insert into address
values
	(
		2,
		219,
		'Street Houston',
		'ChinaTown',
		'MS',
		'https://maps.google.com/',
		null
	);
	
delete from address 
where id = 2;

   
create or replace trigger customers_update_insert_delete_log 
	after update or insert or delete on category 
	for each row
	execute procedure on_customers_log();
   
   
update category 
set description = 'unknown'
where id = 'C' or id = 'HS';

insert into category 
values 
	(
		'V',
		'Pick Up Special',
		'Order pick up special online from Skillman Wok - Garland for takeout. The best Chinese in Garland, TX.'
	);


delete from category 
where id = 'V';


create or replace trigger customers_update_insert_delete_log
	after update or insert or delete on dish 
	for each row
	execute procedure on_customers_log();


update dish
set spicy = false 
where id = 1;
   

insert into dish
values 
	(
		9,
		'Chicken fried',
		'Tender pea-pod sautéed with fresh shrimp in a light sauce',
		false
	);

update dish 
set spicy = true
where id = 9;


delete from dish 
where id = 9;


create or replace trigger customers_update_insert_delete_log
	after update or insert or delete on review 
	for each row 
	execute procedure on_customers_log();

update review 
set rating = 4.8
where id = 2;

insert into review 
values
	(
		4,
		5.7,
		'The food is ok, nothing special.',
		'2020-04-20',
		1,
		2
	);

delete from review 
where rating = 4.8 and id = 2;

