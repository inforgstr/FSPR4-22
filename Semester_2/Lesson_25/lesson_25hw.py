import datetime


import filters.ALevel_filters as Alevel


posts = [
    {
        "title": "Django Web Development",
        "tags": "programming, Python, web development, framework, Django",
        "body": "Build robust and scalable web applications using the Django framework with its powerful features like ORM, templating, and authentication.",
        "published": datetime.date(2023, 1, 1),
    },
    {
        "title": "React Native Mobile App Development",
        "tags": "programming, JavaScript, mobile app, development, framework, React Native",
        "body": "Create cross-platform mobile applications using React Native framework and leverage its component-based architecture and native UI elements.",
        "published": datetime.date(2021, 1, 1),
    },
    {
        "title": "Angular Frontend Framework",
        "tags": "programming, JavaScript, frontend development, framework, Angular",
        "body": "Develop dynamic and interactive web applications using the Angular framework with its powerful features like two-way data binding and dependency injection.",
        "published": datetime.date(2022, 3, 21),
    },
    {
        "title": "Ruby on Rails Web Development",
        "tags": "programming, Ruby, web development, framework, Ruby on Rails",
        "body": "Build modern web applications rapidly using Ruby on Rails framework with its conventions, MVC architecture, and built-in libraries.",
        "published": datetime.date(2023, 10, 14),
    },
    {
        "title": "Flask Microframework",
        "tags": "programming, Python, web development, framework, Flask",
        "body": "Create lightweight and modular web applications using the Flask microframework and its flexible routing, templating, and extension ecosystem.",
        "published": datetime.date(2023, 10, 7),
    },
    {
        "title": "Vue.js Frontend Framework",
        "tags": "programming, JavaScript, frontend development, framework, Vue.js",
        "body": "Develop interactive user interfaces and single-page applications using the Vue.js framework with its intuitive syntax and reactivity.",
        "published": datetime.date(2021, 10, 13),
    },
    {
        "title": "Laravel PHP Framework",
        "tags": "programming, PHP, web development, framework, Laravel",
        "body": "Build elegant and feature-rich web applications using the Laravel framework with its expressive syntax, ORM, routing, and caching capabilities.",
        "published": datetime.date(2020, 12, 5),
    },
    {
        "title": "Spring Boot Java Framework",
        "tags": "programming, Java, web development, framework, Spring Boot",
        "body": "Develop enterprise-grade Java applications quickly with Spring Boot framework, leveraging its auto-configuration, dependency management, and production-ready features.",
        "published": datetime.date(2022, 1, 3),
    },
    {
        "title": "Express.js Node.js Framework",
        "tags": "programming, JavaScript, web development, framework, Express.js, Node.js",
        "body": "Build scalable and high-performance web applications using the Express.js framework with Node.js, focusing on simplicity and minimalist design.",
        "published": datetime.date(2022, 2, 17),
    },
    {
        "title": "ASP.NET Core Framework",
        "tags": "programming, C#, web development, framework, ASP.NET Core",
        "body": "Create modern and cross-platform web applications using the ASP.NET Core framework with its powerful features like MVC pattern, dependency injection, and built-in support for RESTful APIs.",
        "published": datetime.date(2023, 7, 10),
    },
    {
        "title": "Ember.js Frontend Framework",
        "tags": "programming, JavaScript, frontend development, framework, Ember.js",
        "body": "Build ambitious web applications using the Ember.js framework with its conventions, data binding, and routing capabilities.",
        "published": datetime.date(2023, 5, 21),
    },
    {
        "title": "Symfony PHP Framework",
        "tags": "programming, PHP, web development, framework, Symfony",
        "body": "Develop scalable and maintainable web applications using the Symfony framework with its reusable components, ORM, and testing utilities.",
        "published": datetime.date(2022, 9, 14),
    },
    {
        "title": "Product A",
        "tags": "tag1, tag2, tag3",
        "body": "This is the body of Product A.",
        "published": datetime.date(2021, 8, 27),
    },
]

# Create json file which consists posts ordered by date and tag
Alevel.find_similars(posts)
