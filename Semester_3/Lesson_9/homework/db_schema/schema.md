// Store
```
Table store {
  id integer [pk]   
  name varchar(50)
  address varchar(100)
  phone varchar(100)
  map_link varchar(100)
  description varchar(200)
  start_time timestamp
  end_time timestamp 
}

Table category {
  id integer [pk]
  name varchar(50)
  description varchar(50)
}

Table product {
  id integer [pk] 
  name varchar(100) 
  desciption varchar(200) 
  created_at timestamp 
  price money 
  rating decimal 
  company_name varchar(50) 
  quantity decimal 
  // manufacturer_id integer 
  // category_id integer 
  // seller_id integer 
}

Table seller {
  id integer [pk]
  first_name varchar(50) 
  last_name varchar(50)
  age integer
  rating decimal
  work_start_time timestamp  
  work_end_time timestamp
  seller_type varchar(30) // individual, business, professional
  trading_exp varchar(20)
  password varchar(20)
  email varchar(100)
  date_of_birth date
  contacts varchar(50)
}

Table purchase {
  id integer [pk] 
  customer_id integer 
  product_id integer 
  seller_id integer 
  amount real 
  purchase_date timestamp 
  purchase_tax real
  purchase_status varchar(20)
}

Table sell {
  id integer [pk] 
  product_id integer 
  customer_id integer 
  seller_id integer 
  quantity real 
  sale_tax real 
  sale_status varchar(20) // 'pending', 'completed', 'cancelled' 
  sale_date timestamp  
}

Table manufacturer {
  id integer [pk] 
  name varchar(40)
  quality varchar(20)
  contacts varchar(100)
  lead_time time
  warranty boolean
  country varchar(30) 
  industry varchar(50)
  exp_time varchar(20)
}

Table customer {
  id integer [pk]
  first_name varchar(30)
  last_name varchar(30)
  phone_number varchar(40)
  contacts varchar(50)
  cash money
}

Table bucket {
  id integer [pk] 
  customer_id integer 
  product_id integer 
  product_amount real 
}

Table review {
  id integer [pk] 
  rating decimal 
  customer_id integer 
  product_id integer 
  comment text
  posted_date timestamp
}
```
