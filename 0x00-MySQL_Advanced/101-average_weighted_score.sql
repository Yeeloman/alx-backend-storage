--  a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
DELIMITER $$
BEGIN
    UPDATE users
    SET average_score = (
        SELECT IF(SUM(corrections.score * projects.weight) = 0, 0, SUM(corrections.score * projects.weight) / SUM(projects.weight))
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = users.id
    )
    WHERE users.id = corrections.user_id;
END$$
DELIMITER ;
