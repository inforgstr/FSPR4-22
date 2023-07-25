create table customers (
	customer_id integer generated always as identity primary key,
	first_name varchar(100) not null,
	last_name varchar(100) not null,
	email_adress varchar(300) null,
	home_phone varchar(100) null,
	city varchar(50) null,
	state_name varchar(50) null,
	years_old integer null
);

create table customers_log (
	changed_by varchar(100) not null,
	time_changed timestamp not null
);

create table clients (
	client_id integer generated always as identity primary key,
	high_spender integer null,
	first_name varchar(100) not null,
	last_name varchar(100) not null,
	total_spent integer null
);

COPY customers(
    first_name,
    last_name,
    email_address,
    home_phone,
    city,
    state_name,
    years_old
)
FROM
    'data.csv' DELIMITER ',' CSV HEADER;

   
create or replace function insert_function() returns trigger as $$ begin 
	new.last_name := 'UNKNOWN';
	return new;
end; $$ language PLPGSQL;

create trigger insert_trigger
	before update on customers 
	for each row 
	execute procedure insert_function();

select * from customers;

update customers 
set years_old = 42
where last_name = 'Hall';


create or replace function log_customers_change() returns trigger as $$ begin 
	insert into 
		customers_log (changed_by, time_changed)
	values 
		(user, date_trunc('minute', NOW()));
	return new;
end;
$$ language PLPGSQL;


create or replace trigger trigger_customer_change
	before update on customers 
	for each row 
	execute procedure log_customers_change();


update customers 
set years_old = 10
where customer_id = 1;