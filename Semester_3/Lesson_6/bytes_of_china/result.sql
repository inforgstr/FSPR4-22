create table customer (
    customer_id integer primary key,
    first_name varchar(30),
    last_name varchar(30)
);


create table review (
    review_id integer primary key,
    customer_id integer references customer(customer_id),
    rating decimal (2, 1),
    review_text text,
    review_date date
);



insert into customer
values (1, 'John', 'Wilson'),
    (2, 'Emma', 'Tylor'),
    (3, 'Nick', 'Smith');


create table category (
    name varchar(50) primary key,
    description text,
    price money,
    is_special boolean
);


create table menu (
    dish_code varchar(20) primary key,
    dish_name varchar(100),
    price money,
    description text,
    hot_spicy boolean
);

create table menu_categories (
    category_name varchar(50) references category(name),
    dish_code varchar(20) references menu(dish_code),
    primary key (category_name, dish_code)
);


insert into review
values (
        1,
        2,
        3.9,
        'A reasonable place to eat for lunch, if you are in a rush!',
        '2020-03-15'
    ),
    (
        2,
        3,
        5.0,
        'Awesome service. Would love to host another birthday party at Bytes of China!',
        '2020-05-22'
    ),
    (
        3,
        1,
        4.5,
        'Other than a small mix-up, I would give it a 5.0!',
        '2020-04-01'
    );


set lc_monetary to 'en_IE.utf-8';
select *
from category;


insert into category
values ('Appetizers', null, null, false),
    ('Soup', null, null, false),
    ('Chicken', null, null, false),
    ('Beef', null, null, false),
    ('Veal', null, null, false),
    ('Vegeterian', null, null, false),
    ('Rice and Noodles', null, null, false),
    (
        'Luncheon Specials',
        'Served with Hot and Sour Soup or Egg Drop Soup and Fried or Steamed Rice  
        between 11:00 am and 3:00 pm from Monday to Friday.',
        8.95,
        true
    ),
    ('House Specials', null, null, false);


insert into menu
values (
        'C1',
        'Chicken with Broccoli',
        6.95,
        'Diced chicken stir-fried with succulent broccoli florets.',
        False
    ),
    (
        'C2',
        'Sweet and Sour Chicken',
        6.75,
        'Marintated chicken with tangy sweet and sour sauce
	together with pineapples and green peppers.',
        false
    ),
    (
        'C3',
        'Chicken Wings',
        6.95,
        'Finger-licking mouth-watering entree to spice up any lunch or dinner.',
        true
    ),
    (
        'L1',
        'Chicken with Broccoli',
        null,
        'Diced chicken stir-fried with succulent broccoli florets.',
        false
    ),
    (
        'L2',
        'Beef with Garlic Sauce',
        null,
        'Sliced beef steak marinated in garlic sauce for that tangy flavor.',
        true
    ),
    (
        'L3',
        'Fresh Mushroom with Snow Peapods and Baby Corns',
        null,
        'Colorful entree perfect for vegetarians and mushroom lovers.',
        false
    ),
    (
        'HS1',
        'Sesame Chicken',
        15.95,
        'Crispy chunks of chicken flavored with a savory sesame sauce.',
        false
    ),
    (
        'HS2',
        'Special Minced Chicken',
        16.95,
        'Marinated chicken breast sauteed with colorful 
	vegetables topped with pine nuts and shreeded lettuce.',
        false
    ),
    (
        'HS3',
        'Hunan Special Half & Half',
        17.95,
        'Shredded beef in Peking sauce and shredded 
	chicken in garlic sauce.',
        true
    );


insert into menu_categories
values ('Chicken', 'C1'),
    ('Chicken', 'C2'),
    ('Chicken', 'C3'),
    ('Luncheon Specials', 'L1'),
    ('Luncheon Specials', 'L2'),
    ('Luncheon Specials', 'L3'),
    ('House Specials', 'HS1'),
    ('House Specials', 'HS2'),
    ('House Specials', 'HS3');


select menu.dish_name,
    menu.dish_code,
    category.name as category,
    category.price
from menu_categories
    join menu on menu_categories.dish_code = menu.dish_code
    join category on category.name = menu_categories.category_name
where category.is_special = true;
