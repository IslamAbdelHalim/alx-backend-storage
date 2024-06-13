-- Create index idx_name_irst_score on the table names

CREATE INDEX idx_name_first_score ON names (name(1), score);

