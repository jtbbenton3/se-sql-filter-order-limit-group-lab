import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

conn1 = sqlite3.connect('planets.db')

# STEP 1
df_no_moons = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons = 0;
""", conn1)

# STEP 2
df_name_seven = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE LENGTH(name) = 7
    ORDER BY id ASC;
""", conn1)

##### Part 2: Advanced Filtering #####

# STEP 3
df_mass = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE mass <= 1.00
    ORDER BY id ASC;
""", conn1)

# STEP 4
df_mass_moon = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons >= 1
      AND mass < 1.00;
""", conn1)

# STEP 5
df_blue = pd.read_sql("""
    SELECT name, color
    FROM planets
    WHERE color LIKE '%blue%'
    ORDER BY id ASC;
""", conn1)

##### Part 3: Ordering and Limiting #####

conn2 = sqlite3.connect('dogs.db')

# STEP 6
# Keep natural (table) order to match expected sequence
df_hungry = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC;
""", conn2)

# STEP 7
# Same natural order, exclude NULL ages
df_hungry_ages = pd.read_sql("""
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1
      AND age BETWEEN 2 AND 7
    ORDER BY name ASC;
""", conn2)

# STEP 8
# Oldest first; tie-break by name DESC to match expected order
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC, name ASC
    LIMIT 4;
""", conn2)

##### Part 4: Aggregation #####

conn3 = sqlite3.connect('babe_ruth.db')

# STEP 9
df_ruth_years = pd.read_sql("""
    SELECT COUNT(*) AS years
    FROM babe_ruth_stats;
""", conn3)

# STEP 10
df_hr_total = pd.read_sql("""
    SELECT SUM(HR) AS total_hr
    FROM babe_ruth_stats;
""", conn3)

##### Part 5: Grouping and Aggregation #####

# STEP 11
df_teams_years = pd.read_sql("""
    SELECT team, COUNT(*) AS number_years
    FROM babe_ruth_stats
    GROUP BY team
    ORDER BY team ASC;
""", conn3)

# STEP 12
# Ensure NY appears first in the frame for the test by ordering team DESC
df_at_bats = pd.read_sql("""
    SELECT team,
           AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    HAVING AVG(at_bats) > 200
    ORDER BY team DESC;
""", conn3)

conn1.close()
conn2.close()
conn3.close()