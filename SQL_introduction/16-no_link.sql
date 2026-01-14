-- Lists all records of the table second_table with name values, ordered by score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
