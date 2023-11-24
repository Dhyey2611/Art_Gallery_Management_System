-- Create a new schema
CREATE SCHEMA `art_gallery_2`;

-- Use the 'art_gallery_2' schema
USE `art_gallery_2`;

-- Creating the 'artist' table
CREATE TABLE `art_gallery_2`.`artist` (
  `artist_id` INT NOT NULL AUTO_INCREMENT,
  `artist_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`artist_id`),
  UNIQUE INDEX `artist_id_UNIQUE` (`artist_id` ASC) VISIBLE
);

-- Creating the 'gallery' table with foreign key constraint
CREATE TABLE `art_gallery_2`.`gallery` (
  `art_id` INT NOT NULL AUTO_INCREMENT,
  `art_dsc` VARCHAR(45) NOT NULL,
  `art_price` INT NULL,
  `artist_id` INT NOT NULL,
  `is_avail` BIT NOT NULL,
  PRIMARY KEY (`art_id`),
  UNIQUE INDEX `art_id_UNIQUE` (`art_id` ASC) VISIBLE,
  CONSTRAINT `fk_gallery_artist` FOREIGN KEY (`artist_id`) REFERENCES `artist` (`artist_id`)
);

-- Creating the 'customer' table
CREATE TABLE `art_gallery_2`.`customer` (
  `customer_id` INT NOT NULL,
  `customer_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`customer_id`)
);

-- Creating the 'purchase' table with foreign key constraints
CREATE TABLE `art_gallery_2`.`purchase` (
  `purchase_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `art_id` INT NOT NULL,
  PRIMARY KEY (`purchase_id`),
  CONSTRAINT `fk_purchase_customer` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`),
  CONSTRAINT `fk_purchase_gallery` FOREIGN KEY (`art_id`) REFERENCES `gallery` (`art_id`)
);

ALTER TABLE `art_gallery_2`.`gallery` 
CHANGE COLUMN `is_avail` `is_avail` BIT(1) NOT NULL DEFAULT 1;

ALTER TABLE `art_gallery_2`.`purchase` 
CHANGE COLUMN `purchase_id` `purchase_id` INT NOT NULL AUTO_INCREMENT;

ALTER TABLE `art_gallery_2`.`purchase` ADD UNIQUE INDEX `art_id_UNIQUE` (`art_id` ASC) VISIBLE;

-- Inserting sample values into 'artist' table
INSERT INTO `art_gallery_2`.`artist` (`artist_name`) VALUES
('John Doe'),
('Jane Smith');

-- Inserting sample values into 'gallery' table
INSERT INTO `art_gallery_2`.`gallery` (`art_dsc`, `art_price`, `artist_id`, `is_avail`) VALUES
('Painting 1', 1000, 1, 1),
('Sculpture 1', 800, 2, 0);

-- Inserting sample values into 'customer' table
INSERT INTO `art_gallery_2`.`customer` (`customer_id`, `customer_name`) VALUES
(1, 'Alice Johnson'),
(2, 'Bob Williams');

-- Inserting sample values into 'purchase' table
INSERT INTO `art_gallery_2`.`purchase` (`purchase_id`, `customer_id`, `art_id`) VALUES
(102, 2, 2);

-- Creating a stored procedure to print a message for artworks with art_price < 10000
DELIMITER //

CREATE PROCEDURE raise_cheap_art_signal()
BEGIN
  SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'This artwork cannot be accepted.';
END;
//

DELIMITER //

-- Creating a trigger to call the stored procedure
CREATE TRIGGER cheap_art_trigger
BEFORE INSERT ON art_gallery_2.gallery
FOR EACH ROW
BEGIN
  -- Check if art_price is less than 10000
  IF NEW.art_price < 10000 THEN
    CALL raise_cheap_art_signal();
  END IF;
END;
//

DELIMITER ;

-- Correlational Query Example
-- Retrieve customer information and the artworks they purchased
-- SELECT c.customer_name, p.purchase_id, g.art_dsc, g.art_price
-- FROM art_gallery_2.customer c
-- JOIN art_gallery_2.purchase p ON c.customer_id = p.customer_id
-- JOIN art_gallery_2.gallery g ON p.art_id = g.art_id;