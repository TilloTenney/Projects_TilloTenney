--** Data Preparation **

CREATE TABLE appleStore_description_combined AS

SELECT * FROM appleStore_description1
UNION ALL
SELECT * FROM appleStore_description2
UNION ALL
SELECT * FROM appleStore_description3
UNION ALL
SELECT * FROM appleStore_description4

--** EDA **
--Examine the amount of distinct apps in both the AppleStore and the appleStore_description_combined tables.

SELECT COUNT(DISTINCT id) AS unique_apps_in_AppleStore FROM AppleStore; --Count = > 7197

SELECT COUNT(DISTINCT id) AS unique_apps_in_AppleStore_description_combined FROM appleStore_description_combined; --Count = > 7197


--Examine the key fields AppleStore and appleStore_description_combined for any missing data.

SELECT COUNT(*) AS missing_fields_in_AppleStore --Missing values Count = > 0
FROM AppleStore
WHERE track_name IS NULL OR price IS NULL OR user_rating IS NULL OR prime_genre IS NULL or lang_num IS NULL; 

SELECT COUNT(*) AS missing_fields_in_AppleStore__description_combined --Missing values Count = > 0
FROM appleStore_description_combined
WHERE app_desc IS NULL;


--Determine the number of apps available in each genre.

SELECT prime_genre, COUNT(*) AS app_count
FROM AppleStore
GROUP BY prime_genre
ORDER BY app_count DESC;


--View a summary of the app ratings.

SELECT Min(user_rating) AS min_user_rating,
		Max(user_rating) AS max_user_rating,
        Avg(user_rating) AS avg_user_rating
FROM AppleStore --min_user_rating(0), max_user_rating(5), avg_user_rating(3.5269)


--Obtain the app pricing distribution

SELECT (price*2) AS priceBin_start,
		(price*2) + 2 AS priceBin_end,
        COUNT(*) AS num_apps
FROM AppleStore
GROUP BY priceBin_start
ORDER BY priceBin_start


--** DATA ANALYSIS **


--Determine whether paid apps are rated higher than free apps.

SELECT CASE
		WHEN price > 0 then 'Paid'
        ELSE 'Free'
        END AS app_type,
        avg(user_rating) as avg_rating
FROM AppleStore
GROUP BY app_type
ORDER BY avg_rating DESC --Paid apps receive higher user ratings than free ones.


--Examine whether apps with more supported languages have a higher rating.

SELECT CASE
		WHEN lang_num < 10 THEN '<10 lang_num'
        WHEN lang_num BETWEEN 10 AND 30 THEN '10 to 30 lang_num'
        ELSE '>30 lang_num'
        END AS lang_num_group,
        AVG(user_rating) AS avg_user_rating
FROM appleStore
GROUP BY lang_num_group
ORDER BY avg_user_rating DESC --The user_rating average is greater for lang_num between 10 and 30.


--Examine a genre with a low rating.

SELECT prime_genre, 
		AVG(user_rating) AS avg_user_rating
FROM AppleStore
GROUP BY prime_genre
ORDER BY avg_user_rating 
LIMIT 15 --The top 15 low average user rating hold fields that need to be improved to improve the app's quality are listed below.


--Examine the relationship between the length of the app description and the user rating.

SELECT CASE
		WHEN length(B.app_desc) < 500 THEN 'short'
        WHEN length(B.app_desc) BETWEEN 500 AND 1000 THEN 'medium'
        ELSE 'large'
        END AS desc_length_group,
        AVG(A.user_rating) AS avg_user_rating

FROM
	AppleStore AS A
    JOIN
    appleStore_description_combined AS B
    ON
    A.id = B.id
GROUP BY desc_length_group
ORDER BY avg_user_rating DESC --Large desc_length has a high average user_rating.

--Examine the top-rated applications in each genre.

SELECT track_name, prime_genre, user_rating
FROM
(
SELECT track_name, prime_genre, user_rating,
  RANK() OVER(PARTITION By prime_genre ORDER BY user_rating DESC, rating_count_tot DESC) AS rank
FROM AppleStore
) AS a
WHERE a.rank = 1


--** Insights and Recommendations **

/*1. Paid apps receive a higher rating.

2. Apps that support between 10 and 30 languages receive higher scores.

3. Apps for finance and books get bad ratings.

4. Apps with lengthier descriptions receive higher ratings.

5. A new app should strive for an average rating of at least 3.5.

6. There is a lot of competition in the games and entertainment industries.*/
