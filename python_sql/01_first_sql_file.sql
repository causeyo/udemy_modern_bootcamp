CREATE TABLE dogs (
    name TEXT,
    breed TEXT,
    age INTEGER
);

CREATE TABLE cats (
    name TEXT,
    breed TEXT,
    age INTEGER
);

INSERT INTO cats (name, breed, age) VALUES ("Reksio", "Kundel", 5);
INSERT INTO cats (name, breed, age) VALUES ("Piorun", "Wilczur", 2);
INSERT INTO cats (name, breed, age) VALUES ("Longer", "Jamnik", 2);
INSERT INTO cats (name, breed, age) VALUES ("Maggie", "Terrier", 12);

> SELECT * FROM cats
> SELECT name FROM dogs;
> SELECT name, age FROM dogs;
> SELECT * FROM dogs WHERE breed IS "Kundel";
> SELECT * FROM dogs WHERE name IS "Reksio";
> SELECT * FROM dogs WHERE breed IS NOT "Kundel" AND breed IS NOT "Wilczur";
> SELECT * FROM dogs WHERE age > 9;
> SELECT * FROM dogs WHERE name LIKE "%gg%";