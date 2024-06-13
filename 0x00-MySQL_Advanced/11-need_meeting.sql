-- Create a view need_meeing that list all students with a score under 80 (strict)
-- no last_meeting or more than 1 month
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 AND ((last_meeting < NOW() - INTERVAL 1 MONTH) OR last_meeting IS NULL);
