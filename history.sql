-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema jeopardy
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `jeopardy` ;

-- -----------------------------------------------------
-- Schema jeopardy
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `jeopardy` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `jeopardy` ;

-- -----------------------------------------------------
-- Table `jeopardy`.`answers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jeopardy`.`answers` ;

CREATE TABLE IF NOT EXISTS `jeopardy`.`answers` (
  `answer_id` INT(11) NOT NULL,
  `answer` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`answer_id`),
  UNIQUE INDEX `answer_id_UNIQUE` (`answer_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 20
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `jeopardy`.`questions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jeopardy`.`questions` ;

CREATE TABLE IF NOT EXISTS `jeopardy`.`questions` (
  `question_id` INT(11) NOT NULL,
  `question` TEXT NULL DEFAULT NULL,
  `false_answers` VARCHAR(4) NULL DEFAULT NULL,
  `points` INT NULL,
  `answer_id` INT(11) NOT NULL,
  PRIMARY KEY (`question_id`),
  UNIQUE INDEX `question_id_UNIQUE` (`question_id` ASC) VISIBLE,
  INDEX `fk_questions_answers_idx` (`answer_id` ASC) VISIBLE,
  CONSTRAINT `fk_questions_answers`
    FOREIGN KEY (`answer_id`)
    REFERENCES `jeopardy`.`answers` (`answer_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
Use jeopardy;
INSERT INTO answers (answer_id, answer)
VALUES
(1, 'Anne of Cleves'),
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
(12, 'In Thomas Farriner’s bakery on Pudding Lane (though technically the bakehouse was not located on Pudding Lane proper, but on Fish Yard, a small enclave off Pudding Lane) | Learn more with this guide to the Great Fire of London'),
(13, 'The Waltz'),
(14, 'King William IV (who was Victoria’s uncle)'),
(15, 'Bristol | Read more about the Bristol bus boycott'),
(16, 'Aaron Burr, the sitting vice president of the USA | Read more about the Hamilton-Burr duel'),
(17, 'The drunkard’s cloak was a form of humiliating punishment used in the past for people who were perceived to have abused alcohol'),
(18, 'Cuneiform, an ancient writing system that was first used in around 3400 BC'),
(19, 'Agrippina the Younger'),
(20, 'Sarah Breedlove – who later became known as Madam CJ Walker'),
(21, 'Collecting fossils, she was a palaeontologist'),
(22, 'Edmund Spenser, in his epic poem ‘The Faerie Queene’'),
(23, 'Countess Markievicz'),
(24, 'Corsica'),
(25, 'Utah; Omaha; Gold; Juno and Sword'),
(26, 'Roanoke (and read more about its disappearance)'),
(27, 'The Peterloo Massacre'),
(28, 'The Foo Fighters'),
(29, '1913'),
(30, 'A battle formation that consisted of soldiers with long spears placed into circular, tightly packed formations')
;

INSERT INTO questions (question_id, question, false_answers, answer_id, points)
VALUES
(1, 'Which queen had the shortest reign of Henry VIII’s six wives?', 1, 1, 300),
(2, 'In 16th-century Japan, who was Yasuke?', 2, 2, 300),
(3, 'Who wrote the 12th-century account Historia regum Britanniae (The History of the Kings of Britain), which is often credited with making the legend of King Arthur popular?', 3, 3, 300),

(4, 'It is thought that Harriet Tubman directly rescued around 300 people from slavery and gave instructions to help dozens more. But in which conflict did she become the first woman to lead an armed assault?', 1, 1, 300),
(5, 'In which country is the Bay of Pigs?', 2, 2, 300),
(6, 'Which medieval queen was married to both Louis VII of France and Henry II of England?', 3, 3, 300),
(7, 'Who was the first human to journey into space?', 1, 1, 300),
(8, 'Whose body was exhumed from Westminster Abbey, more than two years after his death, to be ‘executed’ for treason?', 2, 2, 300),
(9, 'Who ultimately succeeded King Alfred the Great as ‘king of the Anglo-Saxons’?', 3, 3, 300),
(10, 'By what nickname is Edward Teach better known?', 1, 1, 300),
(11, 'Julius Caesar was assassinated on 15 March 44 BC, a date now often known by what term?', 2, 2, 300),
(12, 'Where did the Great Fire of London begin, on 2 September 1666?', 3, 3, 300),
(13, 'What German dance, which sees partners spinning together in close contact, was condemned as depraved when it was first seen in Regency society?', 1, 1, 300),
(14, 'Which king preceded Queen Victoria?', 2, 2, 300),
(15, 'Guy Bailey, Roy Hackett and Paul Stephenson made history in 1963, as part of a protest against a bus company that refused to employ black and Asian drivers in which UK city?', 3, 3, 300),
(16, 'Who famously duelled Alexander Hamilton on 11 July 1804, resulting in the founding father’s death?', 1, 1, 300),
(17, 'What, in the 16th and 17th centuries, was a ‘drunkard’s cloak’?', 2, 2, 300),
(18, 'What is considered the world’s oldest writing system?', 3, 3, 300),
(19, 'Who was the mother of Emperor Nero and the wife of Emperor Claudius?', 1, 1, 300),
(20, 'Which pioneer of hair products became America’s first black female millionaire?', 2, 2, 300),
(21, 'What was Mary Anning (1799–1847) famous for?', 3, 3, 300),
(22, 'Who gave Queen Elizabeth I the soubriquet ‘Gloriana’?', 1, 1, 300),
(23, 'Although never taking her seat, who was the first woman to be elected to the houses of parliament?', 2, 2, 300),
(24, 'Where was Napoleon Bonaparte born?', 3, 3, 300),
(25, 'Can you name the five beach codenames used by Allied forces on D-Day?', 1, 1, 300),
(26, 'Where was the first British colony in the Americas?', 2, 2, 300),
(27, 'In August 1819, around 60,000 peaceful pro-democracy protestors were attacked in an open square in Manchester. This event was known as…', 3, 3, 300),
(28, 'Which rock band formed in 1994 takes its name from a term used by the Allies in the Second World War to describe various UFOs?', 1, 1, 300),
(29, 'In which year did Emily Wilding Davison die as a result of a collision with King George V’s horse during the Epsom Derby?', 2, 2, 300),
(30, 'In medieval history, what was a ‘schiltron’?', 3, 3, 300)
;