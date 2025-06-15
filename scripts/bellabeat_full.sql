-- STEP 1: Categorize Daily Activity into Step Engagement Levels
DROP TABLE IF EXISTS user_daily_summary;

CREATE TABLE user_daily_summary AS
SELECT
    Id,
    DATE(ActivityDate) AS activity_date,
    TotalSteps,
    TotalDistance,
    Calories,
    CASE
        WHEN TotalSteps < 5000 THEN 'Low'
        WHEN TotalSteps BETWEEN 5000 AND 9999 THEN 'Moderate'
        ELSE 'High'
    END AS step_engagement_level
FROM dailyactivity;

-- STEP 2: Parse and Summarize Sleep Data from Minute-Level Records
DROP TABLE IF EXISTS user_sleep_summary;

CREATE TABLE user_sleep_summary AS
SELECT
    Id,
    -- Convert '3/13/2016 2:39:30 AM' → '2016-03-13'
    printf(
        '%04d-%02d-%02d',
        CAST(SUBSTR(date, INSTR(date, ' ') - 4, 4) AS INT),  -- year
        CAST(SUBSTR(date, 1, INSTR(date, '/') - 1) AS INT),  -- month
        CAST(
            SUBSTR(
                date,
                INSTR(date, '/') + 1,
                INSTR(SUBSTR(date, INSTR(date, '/') + 1), '/') - 1
            ) AS INT
        )  -- day
    ) AS sleep_date,
    COUNT(*) AS TotalMinutesAsleep,
    COUNT(*) AS TotalTimeInBed,
    100.0 AS sleep_efficiency
FROM minute_sleep
GROUP BY Id, sleep_date;

-- STEP 3: Aggregate Step Engagement Distribution
SELECT 
    step_engagement_level,
    COUNT(*) AS days_logged
FROM user_daily_summary
GROUP BY step_engagement_level;

-- STEP 4: Aggregate Average Sleep Duration and Efficiency
SELECT 
    ROUND(AVG(TotalMinutesAsleep) / 60.0, 2) AS avg_hours_asleep,
    ROUND(AVG(sleep_efficiency), 1) AS avg_sleep_efficiency
FROM user_sleep_summary;

-- STEP 5: Join Daily Activity and Sleep Data to Explore Correlation
DROP TABLE IF EXISTS sleep_step_join;

CREATE TABLE sleep_step_join AS
SELECT 
    a.Id,
    a.activity_date,
    a.step_engagement_level,
    s.TotalMinutesAsleep
FROM user_daily_summary a
JOIN user_sleep_summary s
    ON a.Id = s.Id AND a.activity_date = DATE(s.sleep_date, '+1 day');

-- STEP 6: Analyze Sleep Duration by Step Engagement
SELECT
    step_engagement_level,
    ROUND(AVG(TotalMinutesAsleep) / 60.0, 2) AS avg_sleep_hours
FROM sleep_step_join
GROUP BY step_engagement_level;
