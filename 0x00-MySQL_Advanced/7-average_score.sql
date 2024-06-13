-- Createstored procedure AddBonus: new correction for student

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN userid INT)
BEGIN

    SET @avg_score = (SELECT AVG(score) FROM corrections WHERE user_id = userid);

    UPDATE users SET average_score = @avg_score
    WHERE id = userid;
END;
//
DELIMITER ; 
