-- 3
-- with previous_query as (
-- 	select *, count(album_id) as 'quantity'
-- 	from track
-- 	group by 2
-- ) 
-- select album.title as 'Track Title', 
-- previous_query.quantity from previous_query
-- join album on previous_query.album_id = album.id;
-- 
-- 

select album.title as 'Track Title', 
	count(album_id) as 'qantity'
	from track
	join album on track.album_id = album.id
	group by track.album_id;

	
-- 4
select count(District) as 'District count', Country.Code, countryLanguage.Language,
Country.Name as 'Country', Country.Continent as 'Continent',
City.Name as 'City', City.District 'District' from City
join countryLanguage on countryLanguage.CountryCode = Country.Code
join Country on Country.Code = City.CountryCode
group by District
order by Country;


-- 5
select Country.Code, Country.Name as 'Country', count(City.Name) as 'Number of cities' from Country
join City on City.CountryCode = Country.Code
group by 1
order by 2;


-- 6
select Country.Code, Country.Name, Country.Population from Country
join City on City.CountryCode = Country.Code
group by 1
order by 3 desc;


-- 7
select Country.Code, Country.Name as 'Country', City.Name as 'City', 
Country.Population as 'Country Population', 
City.Population as 'City Population' from Country
join City on City.CountryCode = Country.Code
order by 2;


-- 8
select Country.Code, Country.Name as 'Country', 
count(CountryLanguage.Language) as 'Number of Languages' from Country
join CountryLanguage on Country.Code = CountryLanguage.CountryCode
group by 1
order by 3 desc;
