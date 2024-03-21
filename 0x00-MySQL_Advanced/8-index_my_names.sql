-- a SQL script that creates an index idx_name
--_first on the table names and the first letter of name.
CREATE INDEX idx_name ON names (name(1));
