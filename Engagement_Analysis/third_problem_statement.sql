USE engagement;

SELECT
    p.post_id,
    p.post_content,
    SUM(CASE WHEN ur.reaction_type = 'like' THEN 1 ELSE 0 END +
        CASE WHEN ur.reaction_type = 'comment' THEN 1 ELSE 0 END +
        CASE WHEN ur.reaction_type = 'share' THEN 1 ELSE 0 END) AS total_reactions
FROM
    Posts p
LEFT JOIN
    UserReactions ur ON p.post_id = ur.post_id
WHERE
    ur.reaction_date BETWEEN DATE_SUB(NOW(), INTERVAL 1 MONTH) AND NOW() #Change the interval period to get output properly. Dates used in this table are from aug 2023.
GROUP BY
    p.post_id, p.post_content
ORDER BY
    total_reactions DESC
LIMIT
    3; -- Retrieve the top 3 most engaging posts