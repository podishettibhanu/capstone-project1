SELECT title, price_gbp
FROM books
WHERE price_gbp > 30;

SELECT title, price_gbp
FROM books
ORDER BY price_gbp DESC
LIMIT 10;

SELECT DISTINCT star_rating
FROM books
ORDER BY star_rating;

SELECT title, price_gbp, star_rating
FROM books
WHERE price_gbp BETWEEN 10 AND 20;

SELECT title, price_gbp, price_inr
FROM books
WHERE star_rating IN (4, 5);

SELECT
    books.title,
    books.price_gbp,
    books.price_inr,
    books.star_rating,
    categories.category_name
FROM books
JOIN categories
ON books.category_id = categories.category_id
ORDER BY books.price_inr DESC
LIMIT 10;