

/* Q1 - How many games released in 2016? */
SELECT COUNT (release_year) FROM game_pl
WHERE release_year = 2016


/* Q2 - Group the games from highest selling*/
SELECT
g.game_name,
pl.platform_name,
gp.release_year,
pub.publisher_name,
SUM(rs.num_sales) AS global_sales
FROM regional_sales rs
INNER JOIN region r ON rs.region_id = r.id
INNER JOIN game_pl gp ON rs.game_platform_id = gp.id
INNER JOIN game_publisher gpub ON gp.game_publisher_id = gpub.id
INNER JOIN games g ON gpub.game_id = g.id
INNER JOIN platform pl ON gp.platform_id = pl.id
INNER JOIN publisher pub ON gpub.publisher_id = pub.id
GROUP BY g.game_name, pl.platform_name, gp.release_year, pub.publisher_name
ORDER BY SUM(rs.num_sales) DESC;


/* Q3 - What Region Accounts for the majority of Sales? */
SELECT
SUM(rs.num_sales) AS north_america_sales
FROM regional_sales rs
INNER JOIN region r ON rs.region_id = r.id
WHERE region_id = 1


/* Q4 - List the games released by Activision */
SELECT
g.game_name,
pl.platform_name,
gp.release_year,
pub.publisher_name,
SUM(rs.num_sales) AS global_sales
FROM regional_sales rs
INNER JOIN region r ON rs.region_id = r.id
INNER JOIN game_pl gp ON rs.game_platform_id = gp.id
INNER JOIN game_publisher gpub ON gp.game_publisher_id = gpub.id
INNER JOIN games g ON gpub.game_id = g.id
INNER JOIN platform pl ON gp.platform_id = pl.id
INNER JOIN publisher pub ON gpub.publisher_id = pub.id
WHERE publisher_name = 'Activision'
GROUP BY g.game_name, pl.platform_name, gp.release_year, pub.publisher_name



/* Q5 - List the games released for the Nintendo Wii Platform*/
SELECT
g.game_name,
pl.platform_name,
gp.release_year,
pub.publisher_name,
SUM(rs.num_sales) AS global_sales
FROM regional_sales rs
INNER JOIN region r ON rs.region_id = r.id
INNER JOIN game_pl gp ON rs.game_platform_id = gp.id
INNER JOIN game_publisher gpub ON gp.game_publisher_id = gpub.id
INNER JOIN games g ON gpub.game_id = g.id
INNER JOIN platform pl ON gp.platform_id = pl.id
INNER JOIN publisher pub ON gpub.publisher_id = pub.id
WHERE platform_name = 'Wii'
GROUP BY g.game_name, pl.platform_name, gp.release_year, pub.publisher_name



/* Q6 - Find the average number of sales of games released in North America*/
SELECT
AVG(rs.num_sales) AS north_america_avg
FROM regional_sales rs
WHERE region_id = 1



/* Q7 - List all the games that sold more than 10 million copies */
SELECT
g.game_name,
pl.platform_name,
gp.release_year,
pub.publisher_name,
SUM(rs.num_sales) AS global_sales
FROM regional_sales rs
INNER JOIN region r ON rs.region_id = r.id
INNER JOIN game_pl gp ON rs.game_platform_id = gp.id
INNER JOIN game_publisher gpub ON gp.game_publisher_id = gpub.id
INNER JOIN games g ON gpub.game_id = g.id
INNER JOIN platform pl ON gp.platform_id = pl.id
INNER JOIN publisher pub ON gpub.publisher_id = pub.id
WHERE num_sales > 10
GROUP BY g.game_name, pl.platform_name, gp.release_year, pub.publisher_name

