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
"""
CREATE TABLE IF NOT EXISTS `final_exam` (
  `final_exam_date` VARCHAR(45) NOT NULL,
  `final_exam_description` VARCHAR(45) NULL,
  `final_exam_id` INT NOT NULL,
  PRIMARY KEY (`final_exam_id`))
""",
"""
CREATE TABLE IF NOT EXISTS`course` (
  `course_id` INT NOT NULL,
  `course_name` VARCHAR(20) NOT NULL,
  `course_no_of_unit` INT UNSIGNED NOT NULL,
  `final_exam_final_exam_id` INT NOT NULL,
  PRIMARY KEY (`course_id`, `final_exam_final_exam_id`),
  CONSTRAINT `fk_Course_Final_Exam1`
    FOREIGN KEY (`final_exam_final_exam_id`)
    REFERENCES `final_exam` (`final_exam_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
""",
"""
CREATE TABLE IF NOT EXISTS `classroom` (
  `classroom_id` INT NOT NULL,
  `classroom_number` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`classroom_id`))
""",
"""
CREATE TABLE IF NOT EXISTS `semester` (
  `Semester_id` INT NOT NULL,
  `Semester_year` INT NULL,
  `semester_term` INT NULL,
  PRIMARY KEY (`Semester_id`))
""",
"""
CREATE TABLE IF NOT EXISTS `sessions_time` (
  `sessions_time_id` INT NOT NULL,
  `session_day_of_week` VARCHAR(45) NULL,
  `sessions_time` INT NULL,
  PRIMARY KEY (`sessions_time_id`))
""",
"""
CREATE TABLE IF NOT EXISTS `sessions` (
  `sessions_id` INT NOT NULL,
  `sessions_no_of_student` INT NULL,
  `sessions_capacity` INT NULL,
  `sessions_description` VARCHAR(45) NULL,
  `classroom_classroom_id` INT NOT NULL,
  `course_course_id` INT NOT NULL,
  `department_department_id` INT NOT NULL,
  `professor_prof_id` INT NOT NULL,
  `sessions_mark` INT NULL,
  `semester_Semester_id` INT NOT NULL,
  `sessions_time_sessions_time_id` INT NOT NULL,
  PRIMARY KEY (`classroom_classroom_id`, `course_course_id`, `sessions_id`, `department_department_id`, `professor_prof_id`, `semester_Semester_id`, `sessions_time_sessions_time_id`),
  CONSTRAINT `fk_Sessions_classroom1`
    FOREIGN KEY (`classroom_classroom_id`)
    REFERENCES `classroom` (`classroom_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Sessions_Course1`
    FOREIGN KEY (`course_course_id`)
    REFERENCES `course` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sessions_department1`
    FOREIGN KEY (`department_department_id`)
    REFERENCES `department` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sessions_professor1`
    FOREIGN KEY (`professor_prof_id`)
    REFERENCES `professor` (`prof_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sessions_semester1`
    FOREIGN KEY (`semester_Semester_id`)
    REFERENCES `semester` (`Semester_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sessions_sessions_time1`
    FOREIGN KEY (`sessions_time_sessions_time_id`)
    REFERENCES `sessions_time` (`sessions_time_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
""",
"""
CREATE TABLE IF NOT EXISTS `library` (
  `library_no_of_books` INT NULL,
  `library_name` VARCHAR(45) NOT NULL,
  `library_no_of_employees` INT NULL,
  `library_established_year` YEAR NULL,
  `library_id` INT NOT NULL,
  PRIMARY KEY (`library_id`))
""",
"""
CREATE TABLE IF NOT EXISTS `student_activity` (
  `activity_id` INT NOT NULL,
  `activity_name` VARCHAR(20) NOT NULL,
  `date_started` VARCHAR(45) NULL,
  `date_ended` VARCHAR(45) NULL,
  PRIMARY KEY (`activity_id`))
""",
"""
CREATE TABLE IF NOT EXISTS `book_reservation` (
  `book_reservation_time_domain` INT NULL,
  `book_reservation_id` INT NOT NULL,
  `book_reservation_date` VARCHAR(45) NULL,
  `student_student_id` INT NOT NULL,
  PRIMARY KEY (`book_reservation_id`, `student_student_id`),
  CONSTRAINT `fk_book_reservation_student1`
    FOREIGN KEY (`student_student_id`)
    REFERENCES `student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
""",
"""
CREATE TABLE IF NOT EXISTS `book` (
  `book_name` VARCHAR(20) NOT NULL,
  `book_id` INT NOT NULL,
  `aouthor` VARCHAR(45) NOT NULL,
  `publisher` VARCHAR(45) NULL,
  `publication_date` VARCHAR(45) NULL,
  `library_library_id` INT NOT NULL,
  `book_reservation_book_reservation_id` INT NOT NULL,
  PRIMARY KEY (`book_id`, `library_library_id`, `book_reservation_book_reservation_id`),
  CONSTRAINT `fk_book_library1`
    FOREIGN KEY (`library_library_id`)
    REFERENCES `library` (`library_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_book_book_reservation1`
    FOREIGN KEY (`book_reservation_book_reservation_id`)
    REFERENCES `book_reservation` (`book_reservation_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
""",
"""
CREATE TABLE IF NOT EXISTS `lab` (
  `lab_name` VARCHAR(20) NOT NULL,
  `lab_reasercher_nomber` INT NOT NULL,
  `lab_description` VARCHAR(60) NOT NULL,
  `professor_prof_id` INT NOT NULL,
  PRIMARY KEY (`lab_name`, `professor_prof_id`),
  CONSTRAINT `fk_lab_professor1`
    FOREIGN KEY (`professor_prof_id`)
    REFERENCES `professor` (`prof_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
""",
"""
CREATE TABLE IF NOT EXISTS `paper` (
  `paper_paper_id` INT NOT NULL,
  `paper_paper_title` VARCHAR(45) NULL,
  `professor_prof_id` INT NOT NULL,
  PRIMARY KEY (`paper_paper_id`, `professor_prof_id`),
  CONSTRAINT `fk_paper_professor1`
    FOREIGN KEY (`professor_prof_id`)
    REFERENCES `professor` (`prof_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
""",
"""
CREATE TABLE IF NOT EXISTS `activity_of_student` (
  `student_student_id` INT NOT NULL,
  `student_activity_activity_id` INT NOT NULL,
  PRIMARY KEY (`student_student_id`, `student_activity_activity_id`),
  CONSTRAINT `fk_activity_of_student_student1`
    FOREIGN KEY (`student_student_id`)
    REFERENCES `student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_activity_of_student_student_activity1`
    FOREIGN KEY (`student_activity_activity_id`)
    REFERENCES `student_activity` (`activity_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
""",
"""
REATE TABLE IF NOT EXISTS `student_has_sessions` (
  `student_has_sessions_id` INT NOT NULL,
  `shs_mark` FLOAT NULL,
  `shs_sign` TINYINT(1) NOT NULL,
  `shs_session_mark` FLOAT NULL,
  `shs_absence_number` INT NULL,
  `shs_is_current` TINYINT(1) NULL,
  `student_student_id` INT NOT NULL,
  `student_professor_prof_id` INT NOT NULL,
  `student_food_reservation_food_reservation_id` INT NOT NULL,
  `sessions_classroom_classroom_id` INT NOT NULL,
  `sessions_course_course_id` INT NOT NULL,
  `sessions_sessions_id` INT NOT NULL,
  `sessions_department_department_id` INT NOT NULL,
  `sessions_professor_prof_id` INT NOT NULL,
  `sessions_semester_Semester_id` INT NOT NULL,
  `sessions_sessions_time_sessions_time_id` INT NOT NULL,
  PRIMARY KEY (`student_has_sessions_id`, `student_student_id`, `student_professor_prof_id`, `student_food_reservation_food_reservation_id`, `sessions_classroom_classroom_id`, `sessions_course_course_id`, `sessions_sessions_id`, `sessions_department_department_id`, `sessions_professor_prof_id`, `sessions_semester_Semester_id`, `sessions_sessions_time_sessions_time_id`),
  CONSTRAINT `fk_student_has_sessions_student1`
    FOREIGN KEY (`student_student_id` , `student_professor_prof_id` , `student_food_reservation_food_reservation_id`)
    REFERENCES `student` (`student_id` , `professor_prof_id` , `food_reservation_food_reservation_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_has_sessions_sessions1`
    FOREIGN KEY (`sessions_classroom_classroom_id` , `sessions_course_course_id` , `sessions_sessions_id` , `sessions_department_department_id` , `sessions_professor_prof_id` , `sessions_semester_Semester_id` , `sessions_sessions_time_sessions_time_id`)
    REFERENCES `sessions` (`classroom_classroom_id` , `course_course_id` , `sessions_id` , `department_department_id` , `professor_prof_id` , `semester_Semester_id` , `sessions_time_sessions_time_id`)
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
     """
     CREATE INDEX `fk_Course_Final_Exam1_idx` ON ``course` (`final_exam_final_exam_id` ASC) VISIBLE) ;
     """,
     """
     CREATE UNIQUE INDEX `course_id_UNIQUE` ON `course` (`course_id` ASC) VISIBLE) ;
     """,
     """
     CREATE UNIQUE INDEX `classroom_id_UNIQUE` ON `classroom` (`classroom_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_Sessions_classroom1_idx` ON `sessions` (`classroom_classroom_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_Sessions_Course1_idx` ON `sessions` (`course_course_id` ASC) VISIBLE );
     """,
     """
     CREATE INDEX `fk_sessions_department1_idx` ON `sessions` (`department_department_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_sessions_professor1_idx` ON `sessions` (`professor_prof_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_sessions_semester1_idx` ON `sessions` (`semester_Semester_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_sessions_sessions_time1_idx` ON `sessions` (`sessions_time_sessions_time_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_book_reservation_student1_idx` ON `book_reservation` (`student_student_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_book_library1_idx` ON `book` (`library_library_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_book_book_reservation1_idx` ON `book` (`book_reservation_book_reservation_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_lab_professor1_idx` ON `lab` (`professor_prof_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_paper_professor1_idx` ON `paper` (`professor_prof_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_activity_of_student_student_activity1_idx` ON `activity_of_student` (`student_activity_activity_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_student_has_sessions_student1_idx` ON `student_has_sessions` (`student_student_id` ASC, `student_professor_prof_id` ASC, `student_food_reservation_food_reservation_id` ASC) VISIBLE) ;
     """,
     """
     CREATE INDEX `fk_student_has_sessions_sessions1_idx` ON `student_has_sessions` (`sessions_classroom_classroom_id` ASC, `sessions_course_course_id` ASC, `sessions_sessions_id` ASC, `sessions_department_department_id` ASC, `sessions_professor_prof_id` ASC, `sessions_semester_Semester_id` ASC, `sessions_sessions_time_sessions_time_id` ASC) VISIBLE) ;
     """,
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
  202,
  'Mostafa',
  'Nori Baighi',
  '09308277222',
  'Azadi street',
  'Nori@example.com',
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
""",
"""
INSERT INTO `final_exam`(
`final_exam_date`,
`final_exam_description`,
`final_exam_id`
)
VALUES (
    '2023-07-13',
    'Algorithm Design exam',
    13
)
""",
"""
INSERT INTO `course` (
`course_id`,
`course_name`.
`course_no_of_unit`,
`final_exam_final_exam_id`
)
VALUES (
    11,
    'Algorithm Design',
    3,
    13
)
""",
"""
INSERT INTO `classroom` (
`classroom_id`,
`classroom_number`
)
VALUES (
    37,
    'B37'
)
""",
"""
INSERT INTO `semester` (
`semester_id`,
`semester_year`,
`semester_term`
)
VALUES (
232,
2323,
2
)
""",
"""
INSERT INTO `sessions_time` (
`sessions_time_id`,
`sessions_day_of_week`,
`sessions_time`
)
VALUES (
    1,
    'saturday',
    10
)
""",
"""
INSERT INTO `sessions` (
`sessions_id`,
`sessions_no_of_student`,
`sessions_capacity`,
`sessions_description`,
`classroom_classroom_id`,
`course_course_id`,
`department_department_id`,
`professor_prof_id`,
`sessions_mark`,
`semester_semester_id`,
`sessions_time_sessions_time_id`
)
VALUES (
    111,
    0,
    30,
    'Algorithm Design presented by Dr.Nouri Baighi',
    37,
    11,
    22035,
    202,
    0,
    232,
    1
)
""",
"""
INSERT INTO `library` (
`library_no_of_books`,
`library_name`,
`library_no_of_employees`,
`library_established_year`,
`library_id`
)
VALUES (
    100,
    'library',
    10,
    2020,
    23
)
""",
"""
INSERT INTO `student_activity` (
`activity_id`,
`activity_name`,
`date_started`,
`date_ended`
)
VALUES (
    1,
    'TA',
    '23-01-01',
    '23-07-02'
)
""",
"""
INSERT INTO `book_reservation` (
`book_reservation_time_domain`,
`book_reservation_id`,
`book_reservation_data`,
`student_student_id`
)
VALUES (
    14,
    1,
    '23-07-02',
    4001262499
)
""",
"""
INSERT INTO `book` (
`book_name`,
`book_id`,
`aouthor`,
`publisher`,
`publication_date`,
`library_library_id`,
`book_reservation_book_reservation_id`
)
VALUES (
    'Good To GREAT',
    123,
    'Jim C. Collins',
    'HarperCollins',
    '2001-06-16',
    23,
    1
)
""",
"""
INSERT INTO `lab` (
`lab_name`,
`lab_reasercher_nomber`,
`lab_description`,
`professor_prof_id`
)
VALUES (
    'lab',
    7,
    'Hardware lab',
    203
)
""",
"""
INSERT INTO `paper`(
`paper_paper_id`,
`paper_paper_title`,
`professor_prof_id`
)
VALUES (
    1010,
    'paper title',
    203
)
""",
"""
INSERT INTO `activity_of_student` (
`student_student_id`,
`student_activity_activity_id`
)
VALUES (
    4001262499,
    1
)
""",
"""
INSERT INTO `student_has_sessions` (
`student_has_sessions_id`,
`shs_mark`,
`shs_sign`,
`shs_session_mark`,
`shs_absence_number`,
`shs_is_current`,
`student_student_id`,
`student_professor_prof_id`,
`student_food_reservation_food_reservation_id`,
`sessions_classroom_classroom_id`,
`sessions_course_course_id`,
`sessions_sessions_id`,
`sessions_department_department_id`,
`sessions_professor_prof_id`,
`sessions_semester_Semester_id`,
`sessions_sessions_time_sessions_time_id`
)
VALUES (
1,
0,
0,
0,
0,
1,
4001262499,
203,
298,
37,
11,
111,
22035,
203,
232,
2
)
""",
]

for query in insert_queries:
     # Execute the INSERT query
     cursor.execute(query)

#TODO add new tables into select_queryies list: done
# SELECT queries
# Define the SELECT query
select_queryies =[
"""SELECT *
FROM `department`;
""" ,

""" SELECT *
FROM `professor`;
""" ,

""" SELECT *
FROM `food_reservation`;
""" ,

"""SELECT *
FROM `student`;
""" ,

"""SELECT *
FROM `final_exam`;
""" ,

"""SELECT *
FROM `course`;
""" ,

"""SELECT *
FROM  `classroom`;
""" ,

"""SELECT *
FROM `semester`;
""" ,

"""SELECT *
FROM `sessions_time`;
""" ,

"""SELECT *
FROM `sessions`;
""" ,

"""SELECT *
FROM `library`;
""" ,

"""SELECT *
FROM `student_activity`;
""" ,

"""SELECT *
FROM `book_reservation`;
""" ,

"""SELECT *
FROM `book`;
""" ,

"""SELECT *
FROM `lab`;
""" ,

"""SELECT *
FROM `paper`;
""" ,

"""SELECT *
FROM `activity_of_student`;
""" ,

"""SELECT *
FROM `student_has_sessions`;
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
