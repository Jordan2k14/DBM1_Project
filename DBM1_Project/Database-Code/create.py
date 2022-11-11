# By Jordan Ukawoko, Chad Long & Luca Bova - DBM1 



import psycopg2  #import of the psycopg2 python librar
import pandas as pd #import of the pandas python library
import pandas.io.sql as psql

##No transaction is started when commands are executed and no commit() or rollback() is required. 
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# get a new connection but this time point to the created "tartupurchases" DB.
con = psycopg2.connect(user = "postgres",
                       password = "sora", 
                       host = "localhost", #Using Docker we can refer to containers by name
                       port = "5433",
                       database = "videogames")

try:
    # Obtain a new DB Cursor (to "tartupurchases" DB )
    cursor = con.cursor();
    print("connected again to the server and cusor now on videogames DB !!")
except (Exception, psycopg2.Error) as error:
    print("Error in Connection",error)


#Create "Genre" Table

try:
    #table_name variable
    genreTable="genre"
    create_genreTablee_query = '''CREATE TABLE '''+ genreTable+'''
    (
        id                    INT           NOT NULL,
        genre_name         VARCHAR(200)  DEFAULT NULL,
        PRIMARY KEY (id)
        );'''

    #Execute this command (SQL Query)
    cursor.execute(create_genreTablee_query)
    
    # Make the changes to the database persistent
    con.commit()
    print("Table ("+ genreTable +") created successfully in PostgreSQL ")
except (Exception, psycopg2.Error) as error:
    # if it exits with an exception the transaction is rolled back.
    con.rollback()


#Create "Publisher" Table

try:
    #table_name variable
    publisherTable="publisher"
    create_publisherTablee_query = '''CREATE TABLE '''+ publisherTable+'''
    (
        id                    INT           NOT NULL,
        publisher_name        VARCHAR(200)  DEFAULT NULL,
        PRIMARY KEY (id)
        );'''

    #Execute this command (SQL Query)
    cursor.execute(create_publisherTablee_query)
    
    # Make the changes to the database persistent
    con.commit()
    print("Table ("+ publisherTable +") created successfully in PostgreSQL ")
except (Exception, psycopg2.Error) as error:
    # if it exits with an exception the transaction is rolled back.
    con.rollback()

#Create "Region" Table

try:
    #table_name variable
    regionTable="region"
    create_regionTablee_query = '''CREATE TABLE '''+ regionTable+'''
    (
        id                    INT           NOT NULL,
        region_name           VARCHAR(200)  DEFAULT NULL,
        PRIMARY KEY (id)
        );'''

    #Execute this command (SQL Query)
    cursor.execute(create_regionTablee_query)
    
    # Make the changes to the database persistent
    con.commit()
    print("Table ("+ regionTable +") created successfully in PostgreSQL ")
except (Exception, psycopg2.Error) as error:
    # if it exits with an exception the transaction is rolled back.
    con.rollback()
    print("Error While Creating the DB: ",error)


#Create "Platform" Table

try:
    #table_name variable
    platformTable="platform"
    create_platformTablee_query = '''CREATE TABLE '''+ platformTable+'''
    (
        id                    INT           NOT NULL,
        platform_name         VARCHAR(200)  DEFAULT NULL,
        PRIMARY KEY (id)
        );'''

    #Execute this command (SQL Query)
    cursor.execute(create_platformTablee_query)
    
    # Make the changes to the database persistent
    con.commit()
    print("Table ("+ platformTable +") created successfully in PostgreSQL ")
except (Exception, psycopg2.Error) as error:
    # if it exits with an exception the transaction is rolled back.
    con.rollback()


#Create "Games" Table

try:
    #table_name variable
    gamesTable="games"
    create_gamesTablee_query = '''CREATE TABLE '''+ gamesTable+'''
    (
        id           INT           NOT NULL,
        genre_id     INT           DEFAULT NULL,
        game_name    VARCHAR(200)  DEFAULT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (genre_id) REFERENCES genre(id)
        );'''

    #Execute this command (SQL Query)
    cursor.execute(create_gamesTablee_query)
    
    # Make the changes to the database persistent
    con.commit()
    print("Table ("+ gamesTable +") created successfully in PostgreSQL ")
except (Exception, psycopg2.Error) as error:
    # if it exits with an exception the transaction is rolled back.
    con.rollback()
    print("Error While Creating the DB: ",error)



#Create "Game Publisher" Table

try:
    #table_name variable
    game_publisherTable="game_publisher"
    create_game_publisherTablee_query = '''CREATE TABLE '''+ game_publisherTable+'''
    (
        id                    INT           NOT NULL,
        game_id               INT           DEFAULT NULL,
        publisher_id          INT           DEFAULT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (game_id) REFERENCES games(id), 
        FOREIGN KEY (publisher_id) REFERENCES publisher(id)
        );'''

    #Execute this command (SQL Query)
    cursor.execute(create_game_publisherTablee_query)
    
    # Make the changes to the database persistent
    con.commit()
    print("Table ("+ game_publisherTable +") created successfully in PostgreSQL ")
except (Exception, psycopg2.Error) as error:
    # if it exits with an exception the transaction is rolled back.
    con.rollback()

#Create "Game Platform" Table

try:
    #table_name variable
    game_plTable="game_pl"
    create_game_plTablee_query = '''CREATE TABLE '''+ game_plTable+'''
    (
        id                    INT           NOT NULL,
        game_publisher_id     INT           DEFAULT NULL,
        platform_id           INT           DEFAULT NULL,
        release_year          INT           DEFAULT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (game_publisher_id) REFERENCES game_publisher(id),
        FOREIGN KEY (platform_id) REFERENCES platform(id)
        );'''

    #Execute this command (SQL Query)
    cursor.execute(create_game_plTablee_query)
    
    # Make the changes to the database persistent
    con.commit()
    print("Table ("+ game_plTable +") created successfully in PostgreSQL ")
except (Exception, psycopg2.Error) as error:
    # if it exits with an exception the transaction is rolled back.
    con.rollback()
    print("Error While Creating the DB: ",error)



#Create "Regional Sales" Table

try:
    #table_name variable
    regionalsalesTable="regional_sales"
    create_regionalsalesTablee_query = '''CREATE TABLE '''+ regionalsalesTable+'''
    (
        region_id                    INT           DEFAULT NULL,
        game_platform_id             INT           DEFAULT NULL,
        num_sales                    DECIMAL(5,2)  DEFAULT NULL,
        FOREIGN KEY (game_platform_id) REFERENCES game_pl(id),
        FOREIGN KEY (region_id) REFERENCES region(id)
        );'''

    #Execute this command (SQL Query)
    cursor.execute(create_regionalsalesTablee_query)
    
    # Make the changes to the database persistent
    con.commit()
    print("Table ("+ regionalsalesTable +") created successfully in PostgreSQL ")
except (Exception, psycopg2.Error) as error:
    # if it exits with an exception the transaction is rolled back.
    con.rollback()
    print("Error While Creating the DB: ",error)
