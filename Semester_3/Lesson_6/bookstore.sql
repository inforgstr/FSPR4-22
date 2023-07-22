create table book (
    title varchar(100),
    isbn varchar(50) primary key,
    pages integer,
    price money,
    description varchar(256),
    publisher varchar(100)
);


alter table book
add constraint fk_book_page foreign key (pages) references page(id);


create table chapter (
    id integer,
    number integer,
    title varchar(50),
    content varchar(50),
    book_isbn varchar(50) references book(isbn)
);


create table author (
    name varchar(50),
    bio varchar(50),
    email varchar(20) primary key
);


--select 
--	constraint_name, table_name, column_name
--from 
--	information_schema.key_column_usage
--where table_name = 'author';


create table popular_books (
    book_title varchar(50),
    author_name varchar(20),
    number_sold integer,
    number_previewed integer
);


--select 
--	constraint_name, table_name, column_name
--from
--	information_schema.key_column_usage
--where 
--	table_name = 'popular_books';


create table book_details (
    id integer primary key,
    book_isbn varchar(50) references book(isbn) unique,
    rating decimal(3, 1),
    language varchar(10),
    keywords text,
    date_published date
);


create table page (
    id integer primary key,
    content text,
    header varchar(20),
    footer varchar(20),
    book_isnb varchar(50) references book(isbn)
);


--select 
--	constraint_name, table_name, column_name
--from 
--	information_schema.key_column_usage
--where 
--	table_name = 'book_details';


create table book_authors (
    book_isbn varchar(50) references book(isbn),
    author_email varchar(20) references author(email),
    primary key (book_isbn, author_email)
);

