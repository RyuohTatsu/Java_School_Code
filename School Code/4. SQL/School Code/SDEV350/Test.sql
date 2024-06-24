-- Drop table Student if it already exists (including any constraints)
DROP TABLE Student CASCADE CONSTRAINTS;

-- Create a new table named Student with four columns
CREATE TABLE Student (
  Student_ID CHAR(5) CONSTRAINT PK_Student_ID PRIMARY KEY,  -- Define as CHAR for fixed length
  Last_Name VARCHAR(16) NOT NULL,
  First_Name VARCHAR(16) NOT NULL,
  Start_Date DATE NOT NULL
);

-- Enforce format for Student ID (assuming validation happens before insertion)
ALTER TABLE Student
  ADD CHECK (Student_ID LIKE 'S____');  -- Check format: 'S' followed by 4 characters

-- Insert a new row of data into the Student table (assuming data adheres to format)
INSERT INTO Student VALUES ('S1001', 'Walters', 'Brian', '09-MAR-24');
INSERT INTO Student VALUES ('S1002', 'Jones', 'Alice', '10-MAR-24');
INSERT INTO Student VALUES ('S1003', 'Smith', 'David', '11-MAR-24');

-- Save the changes made to the database
COMMIT;

-- Select all data from the Student table
SELECT * FROM Student;