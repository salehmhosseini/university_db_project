import sqlite3

# ANSI escape code for green color
GREEN = '\033[92m'
RESET = '\033[0m'
RED = '\033[91m'
YELLOW = '\033[93m'
PINK = '\033[95m'
PURPLE = '\033[94;95m'
ORANGE = '\033[91;93m'


# Create a connection to the SQLite database
conn = sqlite3.connect('crud.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# TODO add other drop table statements into drop_table_queries list 
# Define the drop table queries
drop_table_queries = [
     """
     DROP TABLE IF EXISTS `department` ;
     
     """ ,
     """
     DROP TABLE IF EXISTS `crud`.`professor` ;

     """ , 
     """
     DROP TABLE IF EXISTS `food_reservation` ;

     """ , 
     """
     DROP TABLE IF EXISTS `student` ;

     """
]

# Execute the drop table queries
for query in drop_table_queries:
    cursor.execute(query)

# Commit the changes to the database
conn.commit()


# Print a statement indicating successful execution
print('\n')
print(GREEN + "There was no problem in dropping the tables" + RESET)

# TODO add other create table statements into create_table_queries list 
# Define the create table query
create_table_queries = ["""
CREATE TABLE IF NOT EXISTS `department` (
  `department_id` INTEGER NOT NULL,
  `department_name` VARCHAR(20) NOT NULL,
  `department_phone_number` VARCHAR(11) NULL,
  `department_email` VARCHAR(45) NULL,
  `department_no_of_student` INTEGER UNSIGNED NULL,
  `department_take_course_start` DATE NULL,
  `department_take_course_end` DATE NULL,
  `department_head_id` INTEGER NOT NULL,
  PRIMARY KEY (`department_id`, `department_head_id`),
  FOREIGN KEY (`department_head_id`)
    REFERENCES `professor` (`prof_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);
""", 
""" 
CREATE TABLE IF NOT EXISTS `professor` (
  `prof_id` INT NOT NULL,
  `prof_firstname` VARCHAR(20) NOT NULL,
  `prof_lastname` VARCHAR(20) NOT NULL,
  `prof_phone_number` VARCHAR(11) NULL,
  `prof_address` VARCHAR(45) NULL,
  `prof_email` VARCHAR(45) NULL,
  `prof_degree` VARCHAR(45),
  `prof_job_position` VARCHAR(45) NULL,
  `prof_gender` VARCHAR(45) NULL,
  `prof_birth_date` DATE NULL,
  `prof_sal` DOUBLE UNSIGNED NULL,
  `prof_employment_statuse` VARCHAR(45) NULL,
  `prof_room_number` INT NULL,
  `department_department_id` INT NOT NULL,
  PRIMARY KEY (`prof_id`, `department_department_id`),
  CONSTRAINT `fk_professor_department1`
    FOREIGN KEY (`department_department_id`)
    REFERENCES `department` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
""" ,
""" 
CREATE TABLE IF NOT EXISTS `food_reservation` (
  `food_reservation_id` INT NOT NULL,
  `food_reservation_date` DATE NULL,
  `food_reservation_type` VARCHAR(45) NULL,
  `food_reservation_resturant` VARCHAR(20) NULL,
  `food_food_name` VARCHAR(20) NULL,
  PRIMARY KEY (`food_reservation_id`))
  
""" , 
""" 
CREATE TABLE IF NOT EXISTS `student` (
  `student_id` INT NOT NULL,
  `student_firstname` VARCHAR(20) NOT NULL,
  `student_lastname` VARCHAR(20) NOT NULL,
  `student_gender` VARCHAR(20) NULL,
  `student_address` VARCHAR(45) NULL,
  `student_major` VARCHAR(20) NULL,
  `student_avg` FLOAT NULL,
  `student_entry_year` YEAR(4) NULL,
  `student_email` VARCHAR(45) NULL,
  `student_phone_number` VARCHAR(11) NULL,
  `student_degree` VARCHAR(20) NULL,
  `student_birth_date` DATE NULL,
  `student_leader_name` VARCHAR(45) NULL,
  `professor_prof_id` INT NOT NULL,
  `food_reservation_food_reservation_id` INT NOT NULL,
  `student_balance` INT NULL,
  `student_passed_units` INT NULL,
  `student_current_units` INT NULL,
  `student_sum_units` INT NULL,
  PRIMARY KEY (`student_id`, `professor_prof_id`, `food_reservation_food_reservation_id`),
  CONSTRAINT `fk_student_professor1`
    FOREIGN KEY (`professor_prof_id`)
    REFERENCES `professor` (`prof_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_food_reservation1`
    FOREIGN KEY (`food_reservation_food_reservation_id`)
    REFERENCES `food_reservation` (`food_reservation_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
"""
]

# Execute the create table queries
for query in create_table_queries:
    cursor.execute(query)

# Commit the changes to the database
conn.commit()

# Print a statement indicating successful execution
print(GREEN +'There was no problem in creating the tables'+RESET)

# TODO add other create index statements into index_queries list
# TODO add IF NOT EXISTS for all queries that you  add

# Define the create index queries
index_queries = [
    """
    CREATE UNIQUE INDEX IF NOT EXISTS `department_id_UNIQUE` ON `department` (`department_id` ASC);
    """,
    """
    CREATE UNIQUE INDEX IF NOT EXISTS `department_phone_number_UNIQUE` ON `department` (`department_phone_number` ASC);
    """,
    """
    CREATE UNIQUE INDEX IF NOT EXISTS `department_email_UNIQUE` ON `department` (`department_email` ASC);
    """,
    """
    CREATE INDEX IF NOT EXISTS `fk_department_professor1_idx` ON `department` (`department_head_id` ASC);
    """ , 
    """
    CREATE UNIQUE INDEX IF NOT EXISTS `prof_phone_UNIQUE` ON `professor` (`prof_phone_number` ASC) ;
    """ , 
    """
     CREATE UNIQUE INDEX IF NOT EXISTS `prof_email_UNIQUE` ON `professor` (`prof_email` ASC) ;
     """ ,
     """
     CREATE UNIQUE INDEX IF NOT EXISTS `prof_id_UNIQUE` ON `professor` (`prof_id` ASC) 
     """ , 
     """
     CREATE INDEX IF NOT EXISTS `fk_professor_department1_idx` ON `professor` (`department_department_id` ASC) ;
    """ , 
    """
    CREATE UNIQUE INDEX IF NOT EXISTS `student_email_UNIQUE` ON `student` (`student_email` ASC) ;
    """ , 
    """ 
     CREATE UNIQUE INDEX IF NOT EXISTS `student_phone_UNIQUE` ON `student` (`student_phone_number` ASC) ;
     """ , 
     """
     CREATE INDEX IF NOT EXISTS `fk_student_professor1_idx` ON `student` (`professor_prof_id` ASC) ;
     """ , 
     """
     CREATE INDEX IF NOT EXISTS `fk_student_food_reservation1_idx` ON `student` (`food_reservation_food_reservation_id` ASC) ;
     """
]

# Execute the index queries
for query in index_queries:
    cursor.execute(query)

# Commit the changes to the database
conn.commit()

# Print a statement indicating successful execution
print(GREEN +'There was no problem in creating the indexes'+RESET)
print('\n\n')

# show the schema of desired table 
table_name = 'department'

# Execute the PRAGMA statement to retrieve table information
cursor.execute(f"PRAGMA table_info({table_name})")

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Print the table schema
print(PINK+f"Schema of table '{table_name}':"+RESET)
for row in rows:
    column_name = row[1]
    data_type = row[2]
    not_null = "NOT NULL" if row[3] else "NULL"
    primary_key = "PRIMARY KEY" if row[5] else ""
    print(YELLOW +f"{column_name} {data_type} {not_null} {primary_key}"+ RESET)

print('\n')
print(GREEN+'####################'+RESET)
print(GREEN+'show table informations afer insertion\n'+RESET)

#TODO insert new records into insert_queries list
# insert queries 
# Define the INSERT query
insert_queries = ["""
INSERT INTO `department` (
  `department_id`,
  `department_name`,
  `department_phone_number`,
  `department_email`,
  `department_no_of_student`,
  `department_take_course_start`,
  `department_take_course_end`,
  `department_head_id`
) VALUES (
  22035,
  'engineering',
  '05132282704',
  'um.ac.engineering@gmail.com',
  100,
  '2023-01-01',
  '2023-12-31',
  203
);
""", 
"""

INSERT INTO `professor` (
  `prof_id`,
  `prof_firstname`,
  `prof_lastname`,
  `prof_phone_number`,
  `prof_address`,
  `prof_email`,
  `prof_degree`,
  `prof_job_position`,
  `prof_gender`,
  `prof_birth_date`,
  `prof_sal`,
  `prof_employment_statuse`,
  `prof_room_number`,
  `department_department_id`
) VALUES (
  203,
  'Mohsen',
  'KAhani',
  '09308277238',
  'Azadi street',
  'Kahani@example.com',
  'PhD',
  'Professor',
  'Male',
  '1970-01-01',
  5000.00,
  'Full-time',
  101,
  22035
);
""" , 
 """
INSERT INTO `food_reservation` (
  `food_reservation_id`,
  `food_reservation_date`,
  `food_reservation_type`,
  `food_reservation_resturant`,
  `food_food_name`
) VALUES (
  298,
  '2023-07-02',
  'Dine-In',
  'Restaurant Poonak',
  'Pizza'
);
""" , 

"""
INSERT INTO `student` (
  `student_id`,
  `student_firstname`,
  `student_lastname`,
  `student_gender`,
  `student_address`,
  `student_major`,
  `student_avg`,
  `student_entry_year`,
  `student_email`,
  `student_phone_number`,
  `student_degree`,
  `student_birth_date`,
  `student_leader_name`,
  `professor_prof_id`,
  `food_reservation_food_reservation_id`,
  `student_balance`,
  `student_passed_units`,
  `student_current_units`,
  `student_sum_units`
) VALUES (
  4001262499,
  'Saleh',
  'Mohammadhosseini',
  'Male',
  'Fallahi Street',
  'Computer Engineering',
  15,
  2021,
  'salehmhosseini2002@gmail.com',
  '09020092705',
  'Bachelor',
  '2002-01-01',
  'Ghiasi',
  203,
  298,
  1000,
  30,
  90,
  120
);
"""

]

for query in insert_queries:
     # Execute the INSERT query
     cursor.execute(query)

#TODO add new tables into select_queryies list
# SELECT queries
# Define the SELECT query
select_queryies =[ """
SELECT *
FROM `department`;
""" , 
""" 
SELECT *
FROM `professor`;
""" , 
"""SELECT *
FROM `food_reservation`;
""" ,

"""SELECT *
FROM `student`;
""" 

]

for query in select_queryies:
     # Execute the SELECT query
     cursor.execute(query)

     # Fetch all the rows returned by the query
     rows = cursor.fetchall()
     table_name = query.split('FROM ')[1].split(';')[0].strip('`')
     
     # Print the table name
     print(PURPLE+"Table: ", table_name+RESET)
     
     # Print the retrieved data
     for row in rows:
          print(row)
     print('\n')

# Commit the changes to the database
conn.commit()


# UPDATE queries 
#TODO add new UPDATE stateents into update_queries list
update_queries = [
"""
UPDATE `student`
SET
  `student_address` = 'Shariati Street'
WHERE
  `student_id` = 4001262499;
"""
]


for query in update_queries:
     # Execute the SELECT query
     cursor.execute(query)

#TODO add new select statements into select_queryies list to show modifications after UPDATE
# Define the SELECT query
select_queryies =[  
"""SELECT *
FROM `student`;
""" 
]
print(GREEN+"##################"+RESET)
print(GREEN+"show tables after UPDATE\n"+GREEN)
for query in select_queryies:
     # Execute the SELECT query
     cursor.execute(query)

     # Fetch all the rows returned by the query
     rows = cursor.fetchall()
     table_name = query.split('FROM ')[1].split(';')[0].strip('`')
     
     # Print the table name
     print(PURPLE+"Table: ", table_name+RESET)
     
     # Print the retrieved data
     for row in rows:
          print(row)
     print('\n')

# DELETE queries
#TODO add new delete statements into delete_queries list
delete_queries =[ """
DELETE FROM `food_reservation`
WHERE `food_reservation_id` = 298;
"""]

for query in delete_queries:
     # Execute the DELETE query
     cursor.execute(query)
 
 
# Define the SELECT query
# TODO add new select statements into select_queryies list to show that DELETE operation works correctly
select_queryies =[  
"""SELECT *
FROM `food_reservation`;
""" 
]    
     
print(GREEN+"##################"+RESET)
print(GREEN+"show tables after DELETE\n"+GREEN)
for query in select_queryies:
     # Execute the SELECT query
     cursor.execute(query)

     # Fetch all the rows returned by the query
     rows = cursor.fetchall()
     table_name = query.split('FROM ')[1].split(';')[0].strip('`')
     
     # Print the table name
     print(PURPLE+"Table: ", table_name+RESET)
     
     # Print the retrieved data
     for row in rows:
          print(row)
     print('\n')
     
     
print('successfully execution\n')



# DELETE all from database
# Get a list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Loop through all tables and delete all records
for table in tables:
    table_name = table[0]
    delete_query = f"DELETE FROM {table_name};"
    cursor.execute(delete_query)

# Commit the changes to the database
conn.commit()


# Close the cursor and connection
cursor.close()
conn.close()