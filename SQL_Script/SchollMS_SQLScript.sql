-- drop database if exists schoolms;
create database if not exists schoolms;
use schoolms;
-- Create Tables
-- drop table assignments;
create table if not exists Assignments(
    ID int auto_increment  primary key,
	Title varchar(50) NOT NULL,
	Description nvarchar(50) NULL,
	SubmissionDate datetime NULL,
	OralMark decimal(5, 2) NULL,
	TotalMark decimal(5, 2) NULL
    );
-- drop table trainers;
create table if not exists Trainers(
	ID int auto_increment primary key,
    FirstName varchar(45) not null,
    LastName varchar(45) not null,
    Subject varchar(45) not null
);
-- drop table students;
create table if not exists Students(
	ID int auto_increment primary key,
    FirstName varchar(45) not null,
    LastName varchar(45) not null,
    DateOfBirth date not null,
    TuitionFees decimal(6, 2) null
);
-- drop table courses;
create table if not exists Courses(
	ID int auto_increment  primary key,
    Title varchar(45) not null,
    Stream varchar(45) not null,
    Type varchar(45) not null,
    StartDate date null,
    EndDate date null,
    TrainersID int ,
    index Trainers_ID (TrainersID),
    foreign key (TrainersID)
		references Trainers(ID)
);

-- drop table assignmentspercourse;
create table if not exists AssignmentsPerCourse(
	Assignments_ID int not null,
	Courses_ID int not null,
    foreign key (Assignments_ID) references Assignments(ID),
    foreign key (Courses_ID) references Courses(ID)
);

-- drop table studentspercourse;
create table if not exists StudentsPerCourse(
students_ID int not null,
courses_ID int not null,
foreign key (students_ID) references Students(ID),
foreign key (courses_ID) references Courses(ID)
);

-- Insert Data to the tables
insert into Assignments(Title,Description,SubmissionDate,OralMark,TotalMark)
values ('Assignment 1','Individual Project 1', '2021/11/29' , 80 ,100),
('Assignment 2','Individual Project - Part A', '2021/12/21' , 80 ,100),
('Assignment 3','Individual Project - Part B', '2021/02/02' , 80 ,100),
('Assignment 4','Second Assignment', '2022/02/24' , 80 ,100),
('Assignment 5','Third Assignment', '2022/03/09' , 80 ,100),
('Assignment 6','Fourth Assignment', '2022/03/15' , 80 ,100),
('Assignment 7','Fifth Assignment', '2022/03/21' , 80 ,100),
('Assignment 8','Group Project', '2022/04/26' , 80 ,100);

-- drop table trainers;
insert into Trainers(FirstName,LastName,Subject)
values ('Name1','Last_Name1','Python'),
('Name2','Last_Name2','C#'),
('Name3','Last_Name3','Java'),
('Name4','Last_Name4','JavaScript');

insert into Courses(Title,Stream,Type,StartDate,EndDate,TrainersID)
values ('BC13JAFT','Java','Full_time','2021/10/18','2022/04/20',(select ID from trainers where Subject='Java')),
('BC13JAPT','Java','Part_time','2021/10/18','2022/01/20',(select ID from trainers where Subject='Java')),
('C13C#FT','C#','Full_time','2021/10/18','2022/04/20',(select ID from trainers where Subject='C#')),
('BC13C#PT','C#','Part_time','2021/10/18','2022/01/20',(select ID from trainers where Subject='C#')),
('C13PYFT','Python','Full_time','2021/10/18','2022/04/20',(select ID from trainers where Subject='Python')),
('BC13PYPT','Python','Part_time','2021/10/18','2022/01/20',(select ID from trainers where Subject='Python')),
('C13JSFT','JavaScript','Full_time','2021/10/18','2022/04/20',(select ID from trainers where Subject='JavaScript')),
('BC13JSPT','JavaScript','Part_time','2021/10/18','2022/01/20',(select ID from trainers where Subject='JavaScript'));

insert into Students(FirstName,LastName,DateOfBirth,TuitionFees)
values ('Name1','Last_Name4','1994/06/10',2000),
('Name2','Last_Name2','1987/06/10',2000),
('Name3','Last_Name3','1990/06/10',2000),
('Name4','Last_Name4','1976/06/10',2000),
('Name5','Last_Name5','1999/06/10',2000),
('Name6','Last_Name6','2000/06/10',2000),
('Name7','Last_Name7','1994/06/10',2000),
('Name8','Last_Name8','1994/06/10',2000);

insert into StudentsPerCourse(students_ID, courses_ID) 
values (1 , 6),
(1 , 3),
(2 , 6),
(3 , 3),
(4 , 1),
(4 , 8),
(5 , 2),
(6 , 4),
(7 , 7),
(8 , 8);

insert into AssignmentsPerCourse(assignments_ID, courses_ID) 
values (1 , 6),
(2 , 6),
(3 , 6),
(4 , 6),
(5 , 6),
(6 , 6),
(7 , 6),
(8 , 6);

-- Display all students 
select * 
from Students;
-- Display all trainers
select * 
from Trainers;
-- Display all assignments
select * 
from Assignments;
-- Display all courses
select * 
from Courses;

-- select Students_ID
-- from studentspercourse;

-- select *
-- from assignmentspercourse;

-- select * from studentspercourse;

-- Display all the students per course
select students.ID as StudentsID, students.FirstName as First_Name, students.LastName as Last_Name,
courses.ID as Courses_ID, courses.Title as Courses_Title, courses.Stream as Course_Stream,
courses.Type as Course_Type
from students, courses, studentspercourse
where students.ID = studentspercourse.Students_ID and courses.ID = studentspercourse.Courses_ID
order by courses.Title, students.FirstName;

-- Display all the Trainers per Course
select trainers.ID as TrainersID, trainers.FirstName as First_Name, trainers.LastName as Last_Name,
courses.ID as CourseID, courses.Title as Course_Title, courses.Stream as Course_Stream,
Courses.Type as Course_Type
from Trainers ,Courses 
where Trainers.ID = courses.TrainersID
order by Trainers.ID;

-- Display all the Assignments per Course
select assignments.ID as AssignmentID, assignments.Title as Title, assignments.Description AS Description,
courses.ID as CourseID, courses.Title as Course_Title, courses.Stream as Course_Stream,
courses.Type as Course_Type
from assignments, courses, assignmentspercourse
where assignments.ID = assignmentspercourse.Assignments_ID and courses.ID = assignmentspercourse.Courses_ID
order by courses.ID;

-- Display all the Assignments per Course per Student
select assignments.ID as AssignmentID, assignments.Title as Title, assignments.Description AS Description,
courses.ID as CourseID, courses.Title as Course_Title, courses.Stream as Course_Stream,
courses.Type as Course_Type, students.ID AS StudentID, students.FirstName AS FirstName, students.LastName AS LastName
from assignments, courses, students, assignmentspercourse, studentspercourse
where assignments.ID = assignmentspercourse.Assignments_ID AND courses.ID = assignmentspercourse.Courses_ID
and students.ID = studentspercourse.Students_ID AND courses.ID = studentspercourse.Courses_ID
order by assignments.ID;

-- Display a list of Students that belong to more than one Courses
select students.ID as StudentID, students.FirstName as FirstName, students.LastName as LastName,
count(*) as NumberOfCourses
from students, studentspercourse, courses
where students.ID = studentspercourse.students_ID
and courses.ID = studentspercourse.Courses_ID
group by students.ID, students.FirstName, students.LastName
having count(*) > 1;



-- select * 
-- from studentspercourse;
-- Update Command 
-- update assignments
-- set SubmissionDate = '2021/11/29'
-- where ID = 1;
-- Use AUTO_INCREMENT=1 to reset the counter ID if we delete a row
-- alter table assignments AUTO_INCREMENT=1;
-- alter table trainers auto_increment=1;
-- alter table courses AUTO_INCREMENT=1;
