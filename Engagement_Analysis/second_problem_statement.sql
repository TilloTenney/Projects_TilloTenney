#Calculating the mean number of reactions, encompassing likes, comments, and shares, per distinct user within a designated time period

SELECT
    DATE(ur.reaction_date) AS reaction_day,
    COUNT(DISTINCT ur.user_id) AS distinct_users,
    COUNT(*) AS total_reactions,
    AVG(COUNT(*)) OVER (PARTITION BY DATE(ur.reaction_date)) AS avg_reactions_per_user
FROM
    UserReactions ur
WHERE
    ur.reaction_date BETWEEN '2023-08-25' AND '2023-08-31' -- Replace with desired time period
GROUP BY
    reaction_day;