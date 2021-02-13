import sqlite3
from sqlite3 import Error

import os.path
from os import path

def create_connection(db_file):
    #Create a database connection to a SQLite database 
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as error:
        print(error)
    finally:
        if conn:
            conn.close()

def getDatabase():
    #Asks user for the address of a database if backspace is pressed 
    # then it defults to the defaultHistory.db
    default = r"defaultHistory.db"
    user_input = input("Please enter the location of the question database or press backspace: %s"%default + chr(8)*4)
    if not user_input:
        user_input = default
    create_connection(user_input)

#checks if a defult database is created
# if not it creates it.
if not path.exists("defaultHistory.db"):
    create_connection(r"defaultHistory.db")
    #Connecting to sqlite
    conn = sqlite3.connect(r'defaultHistory.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Droping questions table if already exists.
    cursor.execute("DROP TABLE IF EXISTS questions")

    #Creating table as per requirement
    questions = '''CREATE TABLE questions(
        `question_id` INT(11) NOT NULL,
        `question` TEXT NULL DEFAULT NULL,
        `false_answers` VARCHAR(4) NULL DEFAULT NULL,
        `points` INT NULL,
        `answer_id` INT(11) NOT NULL,
        PRIMARY KEY (`question_id`),
        CONSTRAINT `fk_questions_answers`
        FOREIGN KEY (`answer_id`)
        REFERENCES `answers` (`answer_id`)
    )'''

    question = '''INSERT INTO questions(question_id, question, false_answers, answer_id, points)
              VALUES(1, 'Which queen had the shortest reign of Henry VIII’s six wives?', 1, 1, 100),
                (2, 'In 16th-century Japan, who was Yasuke?', 2, 2, 100),
                (3, 'Who wrote the 12th-century account Historia regum Britanniae (The History of the Kings of Britain), which is often credited with making the legend of King Arthur popular?', 3, 3, 100),
                (4, 'It is thought that Harriet Tubman directly rescued around 100 people from slavery and gave instructions to help dozens more. But in which conflict did she become the first woman to lead an armed assault?', 1, 1, 100),
                (5, 'In which country is the Bay of Pigs?', 2, 2, 100),
                (6, 'Which medieval queen was married to both Louis VII of France and Henry II of England?', 3, 3, 100),
                (7, 'Who was the first human to journey into space?', 1, 1, 100),
                (8, 'Whose body was exhumed from Westminster Abbey, more than two years after his death, to be ‘executed’ for treason?', 2, 2, 100),
                (9, 'Who ultimately succeeded King Alfred the Great as ‘king of the Anglo-Saxons’?', 3, 3, 100),
                (10, 'By what nickname is Edward Teach better known?', 1, 1, 100),
                (11, 'Julius Caesar was assassinated on 15 March 44 BC, a date now often known by what term?', 2, 2, 200),
                (12, 'Where did the Great Fire of London begin, on 2 September 1666?', 3, 3, 200),
                (13, 'What German dance, which sees partners spinning together in close contact, was condemned as depraved when it was first seen in Regency society?', 1, 1, 200),
                (14, 'Which king preceded Queen Victoria?', 2, 2, 200),
                (15, 'Guy Bailey, Roy Hackett and Paul Stephenson made history in 1963, as part of a protest against a bus company that refused to employ black and Asian drivers in which UK city?', 3, 3, 200),
                (16, 'Who famously duelled Alexander Hamilton on 11 July 1804, resulting in the founding father’s death?', 1, 1, 200),
                (17, 'What, in the 16th and 17th centuries, was a ‘drunkard’s cloak’?', 2, 2, 200),
                (18, 'What is considered the world’s oldest writing system?', 3, 3, 200),
                (19, 'Who was the mother of Emperor Nero and the wife of Emperor Claudius?', 1, 1, 200),
                (20, 'Which pioneer of hair products became America’s first black female millionaire?', 2, 2, 200),
                (21, 'What was Mary Anning (1799–1847) famous for?', 3, 3, 300),
                (22, 'Who gave Queen Elizabeth I the soubriquet ‘Gloriana’?', 1, 1, 300),
                (23, 'Although never taking her seat, who was the first woman to be elected to the houses of parliament?', 2, 2, 300),
                (24, 'Where was Napoleon Bonaparte born?', 3, 3, 300),
                (25, 'Can you name the five beach codenames used by Allied forces on D-Day?', 1, 1, 300),
                (26, 'Where was the first British colony in the Americas?', 2, 2, 300),
                (27, 'In August 1819, around 60,000 peaceful pro-democracy protestors were attacked in an open square in Manchester. This event was known as…', 3, 3, 300),
                (28, 'Which rock band formed in 1994 takes its name from a term used by the Allies in the Second World War to describe various UFOs?', 1, 1, 300),
                (29, 'In which year did Emily Wilding Davison die as a result of a collision with King George V’s horse during the Epsom Derby?', 2, 2, 300),
                (30, 'In medieval history, what was a ‘schiltron’?', 3, 3, 300) '''

    cursor.execute(questions)
    cursor.execute(question)
    print("Table questions created successfully........")

     #Dropping answers table if already exists.
    cursor.execute("DROP TABLE IF EXISTS answers")

    #Creating table as per requirement
    answers ='''CREATE TABLE answers(
        `answer_id` INT(11) NOT NULL,
        `answer` TEXT NULL DEFAULT NULL,
        PRIMARY KEY (`answer_id`)
    )'''

    answer = ''' INSERT INTO answers(answer_id, answer)
              VALUES(1, 'Anne of Cleves'),
                (2, 'Yasuke is known as the first foreign-born samurai in 16th-century Japan'),
                (3, 'Geoffrey of Monmouth'),
                (4, 'Harriet Tubman served in the America Civil War'),
                (5, 'It was the site of a failed attempt by a group of Cuban émigrés, with the backing of the US government, to invade the island in 1961.'),
                (6, 'Eleanor of Aquitaine'),
                (7, 'Soviet cosmonaut Yuri Gagarin, in April 1961'),
                (8, 'The body of Oliver Cromwell was exhumed in 1661.'),
                (9, 'Edward the Elder, son of Alfred and Ealhswith of Mercia'),
                (10, 'Edward Teach is better known to history as the notorious 17th-century pirate ‘Blackbeard’'),
                (11, 'The Ides of March'),
                (12, 'In Thomas Farriner’s bakery on Pudding Lane (though technically the bakehouse was not located on Pudding Lane proper, but on Fish Yard, a small enclave off Pudding Lane)'),
                (13, 'The Waltz'),
                (14, 'King William IV (who was Victoria’s uncle)'),
                (15, 'Bristol'),
                (16, 'Aaron Burr, the sitting vice president of the USA'),
                (17, 'The drunkard’s cloak was a form of humiliating punishment used in the past for people who were perceived to have abused alcohol'),
                (18, 'Cuneiform, an ancient writing system that was first used in around 3400 BC'),
                (19, 'Agrippina the Younger'),
                (20, 'Sarah Breedlove – who later became known as Madam CJ Walker'),
                (21, 'Collecting fossils, she was a palaeontologist'),
                (22, 'Edmund Spenser, in his epic poem ‘The Faerie Queene’'),
                (23, 'Countess Markievicz'),
                (24, 'Corsica'),
                (25, 'Utah; Omaha; Gold; Juno and Sword'),
                (26, 'Roanoke'),
                (27, 'The Peterloo Massacre'),
                (28, 'The Foo Fighters'),
                (29, '1913'),
                (30, 'A battle formation that consisted of soldiers with long spears placed into circular, tightly packed formations') '''

    cursor.execute(answers)
    cursor.execute(answer)
    print("Table answers created successfully........")

    # Commit changes in the database
    conn.commit()

    #Closing the connection
    conn.close()
getDatabase()