insert into book 
values 
	('Clean Code', 
	'9780132350884', 
	null, 
	40.34, 
	'Even bad code can work
	the development of the project and the developer company, 
	taking up significant resources for its support and "taming".',
	'Pearson Education'),
	('Python Crash Course, 3rd Edition',
	'978-1718502703',
	null,
	30.49,
	'Python Crash Course is the world’s best-selling 
	guide to the Python programming language.  
	solving problems applications in no time.',
	'No Starch Press'),
	('Design Patterns: Elements of Reusable 
	Object-Oriented Software 1st Edition, Kindle Edition',
	'978-0201633610',
	null,
	35.99,
	'Patterns allow
	reusable designs without having to rediscover the design solutions 
	themselves. Highly influential, Design Patterns is a modern classic
	are and how they can help you design object-oriented 
	software.',
	'Addison-Wesley Professional')
;

delete from book where isbn = '9780132350884' or isbn = '978-1718502703';


insert into author 
values 
	('Eric Matthes', 
	'I recently finished writing Python Crash Course.',
	'ehmatthes@gmail.com'),
	('Robert Martin',
	'Robert Cecil Martin, 
	also known as Uncle Bob.',
	'er.martin@uw.edu'),
	('Erich Gamma',
	'Erich Gamma (born 1961 in Zürich)',
	'erich.g@gmail.com');



insert into book_authors 
values 
	('978-1718502703', 'ehmatthes@gmail.com'),
	('9780132350884', 'er.martin@uw.edu'),
	('978-0201633610', 'erich.g@gmail.com');



alter table page 
add column 
	page_number integer;


insert into page 
values 
	(
	1, 
	'The Bullet class inherits from Sprite, which we import from the pygame
	.sprite module. When you use sprites, you can group related elements in
	your game and act on all the grouped elements at once. To create a bullet
	instance, __init__() needs the current instance of AlienInvasion, and we call
	super() to inherit properly from Sprite. We also set attributes for the screen
	and settings objects, and for the bullet’s color.
	At u, we create the bullet’s rect attribute. The bullet isn’t based on an
	image, so we have to build a rect from scratch using the pygame.Rect() class.
	This class requires the x- and y-coordinates of the top-left corner of the ', 
	'Python Course',
	'Functions.',
	247
	),
	(
	2,
	'We start with a range of x-values containing the numbers 1 through
	1000 . Next, a list comprehension generates the y-values by looping
	through the x-values (for x in x_values), squaring each number (x**2) and',
	'Python Course',
	'Figure 15-7',
	313
	),
	(
	3,
	'"...this new book by Gamma, Helm, Johnson, and Vlissides promises to have an important and lasting
	impact on the discipline of software design. Because Design Patterns bills itself as being concerned',
	'Design Patterns.',
	'C++ Report',
	10
	),
	(
	4,
	'Participants
	• Prototype (Graphic)
	- declares an interface for cloning itself.
	• ConcretePrototype (Staff, WholeNote, HalfNote)
	- implements an operation for cloning itself.
	• Client (GraphicTool)
	- creates a new object by asking a prototype to clone itself.
	Collaborations
	• A client asks a prototype to clone itself.
	Consequences.',
	'Structure',
	'Highly dynamic.',
	139
	),
	(
	5,
	'Be prepared to work hard while reading this book. This is not a “feel good” book that
	you can read on an airplane and finish before you land. This book will make you work, and
	work hard. What kind of work will you be doing? You’ll be reading code—lots of code.
	And you will be challenged to think about what’s right about that code and what’s wrong',
	'Introduction',
	'Acknowledgments',
	28
	),
	(
	6,
	'One might argue that a book about code is somehow behind the times—that code is no
	longer the issue; that we should be concerned about models and requirements instead.
	Indeed some have suggested that we are close to the end of code. That soon all code will
	be generated instead of written. That programmers simply won’t be needed because business 
	people will generate programs from specifications.',
	'Clean Code',
	'Bad Code',
	33
	)
;


alter table page 
add column book_isbn varchar(50) references book(isbn);

update page 
set book_isbn = '978-1718502703'
where id = 1 or id = 2;


update page 
set book_isbn = '978-0201633610'
where id = 3 or id = 4;


update page 
set book_isbn = '9780132350884'
where id = 5 or id = 6;


update book 
set pages = 198
where isbn = '9780132350884';


set lc_monetary to 'en_IE.utf-8';


select book.price, book.title, page.header 
from book
join page on book.isbn = page.book_isbn;



insert into book_details 
values 
	(
	1, 
	'9780132350884', 
	7.8, 
	'English', 
	'Brief introduction to Design Patterns | Kariera Future Processing
	Design patterns are the ready descriptions giving solutions to 
	repetitive and typical project problems. They are the results of 
	experience, hard work and a great number of trials and errors. 
	They also represent considered and best practices of object-oriented 
	programming (SOLID, DRY, KISS and YAGNI).',
	'1994-10-21'
	),
	(
	2,
	'978-0201633610',
	7.5,
	'English',
	'There Will Be Code
	Nonsense: Programmers won''t be needed because business people will generate programs from specifications.
	The level of abstraction of our programing languages will increase but there will be code.
	Well specified requirements can act as executable tests for our code.
	Bad Code
	Bad code can bring a company down.
	There are no excuses for bad code, no reasons: your boss does not give you time, you want to finish faster to get more backlog''s stories finished...
	I will clean it later... Later equals never.',
	'2008-08-01'
	),
	(
	3,
	'978-1718502703',
	8.7,
	'English',
	'6-1: Person
	Use a dictionary to store information about a person you know. Store their first name, last name, age, and 
	the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each 
	piece of information stored in your dictionary.
	
	person = {
	    ''first_name'': ''eric'',
	    ''last_name'': ''matthes'',
	    ''age'': 43,
	    ''city'': ''sitka'',
	    }
	print(person[''first_name''])
	print(person[''last_name''])
	print(person[''age''])
	print(person[''city''])
	Output:
	eric
	matthes
	43
	sitka',
	'2015-11-20'
	);



insert into chapter 
values 
	(
	1,
	6,
	'Glossary',
	'A Python dictionary can be used to model an actual dictionary.',
	'978-1718502703'
	),
	(
	2,
	14,
	'Solutions',
	'There are a few things that can be helpful.',
	'978-1718502703'
	),
	(
	3,
	2,
	'Meaningful names',
	'Use intention-revealing names. Good variable.',
	'9780132350884'
	),
	(
	4,
	1,
	'Clean Code',
	'The book is about good programming.',
	'9780132350884'
	),
	(
	5,
	3,
	'Model-View-Controller Pattern',
	'The model-view-controller (MVC) pattern.',
	'978-0201633610'
	),
	(
	6,
	2,
	'How to Read a Class Diagram',
	'So now you know what design patterns are!.',
	'978-0201633610'
	);



insert into popular_books 
values 
	('978-0201633610', 'erich.g@gmail.com', 56039, 45000),
	('9780132350884', 'er.martin@uw.edu', 192030, 89384),
	('978-1718502703', 'ehmatthes@gmail.com', 293847, 192384);
