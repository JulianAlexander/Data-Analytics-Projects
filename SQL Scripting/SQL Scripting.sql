-- 1a. Display the first and last names of all actors from the table actor.
use sakila; -- using sakila DB
SELECT * FROM actor; -- looking through the actor table to see column names
SELECT first_name, last_name FROM actor; -- selecting the first and last names from the actor table

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
use sakila; -- using sakila DB
SELECT * FROM actor; -- selecting the actor table to verify formatting
SELECT CONCAT(first_name, " ", last_name) AS `Actor Name` FROM actor; -- concating first name and last name into new column, Actor Name

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
use sakila; -- using sakila DB
SELECT * FROM actor WHERE first_name = "Joe"; -- creates query to return whole row from actor table where first_name is Joe

-- 2b. Find all actors whose last name contain the letters GEN:
use sakila;
SELECT * FROM actor WHERE last_name LIKE '%GEN%'; -- query which looks for 'GEN' in the last name column and returns all rows

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
use sakila;
SELECT * FROM actor WHERE last_name LIKE '%LI%' -- query which looks for 'LI' in last_name
ORDER BY last_name, first_name; -- Order by last name first, then first name

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
use sakila;
SELECT * FROM country -- using the country table
WHERE country = "Afghanistan" OR country = "Bangladesh" OR country = "China"; -- query to select all rows with country name equal to Afghanistan, Bangladesh, or China

-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.
use sakila;
ALTER TABLE actor ADD middle_name varchar(255) AFTER first_name; -- adding column middle name after column first name
SELECT * FROM actor;

-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
use sakila;
ALTER TABLE actor modify middle_name blob; -- changing the data type of middle name column to blob

-- 3c. Now delete the middle_name column.
use sakila;
ALTER TABLE actor DROP middle_name; -- use DROP command to delete middle name column

-- 4a. List the last names of actors, as well as how many actors have that last name.
use sakila;
SELECT last_name,Count(*) as count FROM actor GROUP BY last_name ORDER BY count DESC; -- query asks for all last names and a count from the actor table

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
 use sakila;
 SELECT last_name,COUNT(*) as count FROM actor Group by last_name having count >= 2 order by count desc; -- asks for last names only where the count is greater or equal to 2
 
-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
use sakila;
SET SQL_SAFE_UPDATES = 0;
UPDATE actor set first_name = "HARPO" where first_name = "GROUCHO" AND last_name = "WILLIAMS"; 
SELECT * FROM actor where first_name = "HARPO";
-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! (Hint: update the record using a unique identifier.)
UPDATE actor set first_name = "GROUCHO" where first_name = "HARPO" AND last_name = "WILLIAMS";

-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
use sakila;
describe address;

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
use sakila;
SELECT * FROM address;
SELECT staff.first_name, staff.last_name, address.address, address.district, address.city_id, address.phone 
FROM staff
INNER JOIN address ON address.address_id = staff.address_id;

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
use sakila;
SELECT * from payment;
SELECT payment.staff_id, SUM(payment.amount), staff.first_name, staff.last_name
FROM payment
JOIN staff ON payment.staff_id = staff.staff_id 
WHERE payment.payment_date BETWEEN '2005-08-01' AND '2015-08-30'
GROUP BY staff.staff_id;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
use sakila;
SHOW Tables;
SELECT * FROM film;
SELECT * FROM film_actor;
SELECT film_actor.film_id, film.title, COUNT(film_actor.actor_id)
FROM film_actor
INNER JOIN film ON film_actor.film_id = film.film_id
GROUP BY film_actor.film_id;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
use sakila;
SELECT * FROM inventory;
SELECT * FROM film WHERE title = 'Hunchback Impossible';
SELECT COUNT(inventory.film_id), film.title
FROM inventory
INNER JOIN film ON film.film_id = inventory.film_id
WHERE film.title = 'Hunchback Impossible';

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
use sakila;
SELECT * FROM payment;
SELECT * FROM customer;
SELECT customer.customer_id, customer.first_name, customer.last_name, SUM(payment.amount)
FROM customer
JOIN payment ON customer.customer_id = payment.customer_id
GROUP BY customer.last_name ORDER BY customer.last_name;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films 
-- starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of movies 
-- starting with the letters K and Q whose language is English.
use sakila;
SELECT * FROM film;
SELECT * FROM language;
SELECT film.title FROM film
WHERE film.language_id = (SELECT language_id WHERE language_id = 1)
AND (film.title LIKE 'K%' OR film.title LIKE 'Q%');

-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
use sakila;
SELECT * FROM film;
SELECT * FROM actor;
SELECT * FROM film_actor;
SELECT film.title, film.film_id, film_actor.actor_id, actor.first_name, actor.last_name FROM (film, actor)
JOIN film_actor ON film_actor.actor_id = actor.actor_id
WHERE film_actor.film_id = (SELECT film.film_id WHERE film.title = 'Alone Trip');

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and 
-- email addresses of all Canadian customers. Use joins to retrieve this information.
use sakila;
SELECT * FROM customer;
SELECT * FROM country;
SELECT * FROM address;
SELECT * FROM city;
SELECT customer.first_name, customer.last_name, customer.email, customer.address_id FROM customer
WHERE customer.address_id IN (
		SELECT address.address_id FROM address
			WHERE address.city_id IN (
				SELECT city.city_id FROM city
					WHERE city.country_id IN (
						SELECT country.country_id FROM country
							WHERE country.country = 'Canada')
                            )
						);

-- 7d. Sales have been lagging among young families, and you wish to target all family movies 
-- for a promotion. Identify all movies categorized as famiy films.
use sakila;
SELECT * FROM film;
SELECT * FROM category;
SELECT * FROM film_category;
SELECT film.title, film.description, film.rating, film_category.category_id FROM film
JOIN film_category ON film.film_id = film_category.film_id
WHERE film_category.category_id IN (
	SELECT category.category_id FROM category
		WHERE category.name = 'Family');
                

-- 7e. Display the most frequently rented movies in descending order.
use sakila;
SELECT film.title, film.description, count(film.title) AS filmCount FROM film LEFT JOIN (inventory, rental)
ON (inventory.film_id = film.film_id AND rental.inventory_id = inventory.inventory_id)
GROUP BY film.title ORDER BY filmCount DESC;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
use sakila;
SELECT sum(payment.amount), payment.staff_id FROM (payment) 
GROUP BY payment.staff_id;
-- 7g. Write a query to display for each store its store ID, city, and country.
use sakila;
SELECT store.store_id, address.address, city.city, country.country FROM (store, address, city, country)
WHERE store.address_id = address.address_id AND address.city_id = city.city_id AND city.country_id = country.country_id;
-- 
-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
use sakila;
SELECT category.name, sum(payment.amount) FROM  (category)
JOIN film_category USING (category_id) -- I think the USING query is much easier than WHERE or nested subqueries, at least for now
JOIN inventory USING (film_id)
JOIN rental USING (inventory_id)
JOIN payment USING (rental_id)
GROUP BY category.name ORDER BY sum(payment.amount) DESC LIMIT 5;

-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres 
-- by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you 
-- can substitute another query to create a view. 

use sakila;
CREATE VIEW Top_Gross_Genres AS
SELECT category.name, sum(payment.amount) FROM  (category)
JOIN film_category USING (category_id) 
JOIN inventory USING (film_id)
JOIN rental USING (inventory_id)
JOIN payment USING (rental_id)
GROUP BY category.name ORDER BY sum(payment.amount) DESC LIMIT 5;
-- 8b. How would you display the view that you created in 8a?
SELECT * FROM top_gross_genres;
-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
use sakila;
DROP VIEW top_gross_genres;