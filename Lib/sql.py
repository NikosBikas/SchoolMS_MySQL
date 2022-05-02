from datetime import date
import time

def warningMessage():
    while True:
        print("Warning the program establishes a connection with mysql server and creates/overwrites a database named schoolms!")
        print("Within exiting the database is dropped automatically!\n")
        if input('Do You Want To Continue? (y,n):') != 'y' :
            exit()
        else:
            break

def dropDataBase(connection):
    drop_db = "drop database if exists schoolms;"
    
    with connection.cursor() as cursor:
        cursor.execute(drop_db)
        print("DB schoolms was dropped succefully!")
        time.sleep(0)

def createDataBaseInMySql(connection):
    create_db = "create database if not exists schoolms"
    use_db = "use schoolMS"
    
    with connection.cursor() as cursor:
        cursor.execute(create_db)
        cursor.execute(use_db)
        print("DB schoolms was created succefully!")
        time.sleep(0)



def createTablesInDatabase(connection):    
    assignments_table = """ create table if not exists Assignments(
    ID int auto_increment  primary key,
	Title varchar(50) NOT NULL,
	Description nvarchar(50) NULL,
	SubmissionDate datetime NULL,
	OralMark decimal(5, 2) NULL,
	TotalMark decimal(5, 2) NULL
    ); """

    trainers_table  = """ create table if not exists Trainers(
	ID int auto_increment primary key,
    FirstName varchar(45) not null,
    LastName varchar(45) not null,
    Subject varchar(45) not null
    );  """

    students_table = """ create table if not exists Students(
	ID int auto_increment primary key,
    FirstName varchar(45) not null,
    LastName varchar(45) not null,
    DateOfBirth date not null,
    TuitionFees decimal(6, 2) null
    );  """

    courses_table = """ create table if not exists Courses(
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
    ); """

    assPerCourse_table = """ create table if not exists AssignmentsPerCourse(
	Assignments_ID int not null,
	Courses_ID int not null,
    foreign key (Assignments_ID) references Assignments(ID),
    foreign key (Courses_ID) references Courses(ID)
    ); """

    stdsPerCourse_table = """ create table if not exists StudentsPerCourse(
    students_ID int not null,
    courses_ID int not null,
    foreign key (students_ID) references Students(ID),
    foreign key (courses_ID) references Courses(ID)
    ); """

    with connection.cursor() as cursor:
        cursor.execute(assignments_table)
        print("Assignments Table was Created!")
        time.sleep(0)
        cursor.execute(trainers_table)
        print("Trainers Table was Created!")
        time.sleep(0)
        cursor.execute(students_table)
        print("Students Table was Created!")
        time.sleep(0)
        cursor.execute(courses_table)
        print("Courses Table was Created!")
        time.sleep(0)
        cursor.execute(assPerCourse_table)
        print("Assignments per Course Table was Created!")
        time.sleep(0)
        cursor.execute(stdsPerCourse_table)
        print("Assignments per Students Table was Created!")
        time.sleep(0)

def insertDummyDataToTables(connection):
    assignments_data = """ insert into assignments(Title,Description,SubmissionDate,OralMark,TotalMark)
    values ('Assignment 1','Individual Project 1', '2021/11/29' , 80 ,100),
    ('Assignment 2','Individual Project - Part A', '2021/12/21' , 80 ,100),
    ('Assignment 3','Individual Project - Part B', '2021/02/02' , 80 ,100),
    ('Assignment 4','Second Assignment', '2022/02/24' , 80 ,100),
    ('Assignment 5','Third Assignment', '2022/03/09' , 80 ,100),
    ('Assignment 6','Fourth Assignment', '2022/03/15' , 80 ,100),
    ('Assignment 7','Fifth Assignment', '2022/03/21' , 80 ,100),
    ('Assignment 8','Group Project', '2022/04/26' , 80 ,100); """
    
    trainers_data = """ insert into trainers(FirstName,LastName,Subject)
    values ('Name1','Last_Name1','Python'),
    ('Name2','Last_Name2','C#'),
    ('Name3','Last_Name3','Java'),
    ('Name4','Last_Name4','JavaScript'); """

    course_data = """ insert into courses(Title,Stream,Type,StartDate,EndDate,TrainersID)
    values ('BC13JAFT','Java','Full_time','2021/10/18','2022/04/20',(select ID from trainers where Subject='Java')),
    ('BC13JAPT','Java','Part_time','2021/10/18','2022/01/20',(select ID from trainers where Subject='Java')),
    ('C13C#FT','C#','Full_time','2021/10/18','2022/04/20',(select ID from trainers where Subject='C#')),
    ('BC13C#PT','C#','Part_time','2021/10/18','2022/01/20',(select ID from trainers where Subject='C#')),
    ('C13PYFT','Python','Full_time','2021/10/18','2022/04/20',(select ID from trainers where Subject='Python')),
    ('BC13PYPT','Python','Part_time','2021/10/18','2022/01/20',(select ID from trainers where Subject='Python')),
    ('C13JSFT','JavaScript','Full_time','2021/10/18','2022/04/20',(select ID from trainers where Subject='JavaScript')),
    ('BC13JSPT','JavaScript','Part_time','2021/10/18','2022/01/20',(select ID from trainers where Subject='JavaScript'));"""
    
    students_data = """ insert into students(FirstName,LastName,DateOfBirth,TuitionFees)
    values ('Name1','Last_Name1','1994/06/10',2000),
    ('Name2','Last_Name2','1987/06/10',2000),
    ('Name3','Last_Name3','1990/06/10',2000),
    ('Name4','Last_Name4','1976/06/10',2000),
    ('Name5','Last_Name5','1999/06/10',2000),
    ('Name6','Last_Name6','2000/06/10',2000),
    ('Name7','Last_Name7','1994/06/10',2000),
    ('Name8','Last_Name8','1994/06/10',2000); """
    
    stdsPerCourse_data = """ insert into studentspercourse(students_ID, courses_ID) 
    values (1 , 6),
    (1 , 3),
    (2 , 6),
    (3 , 3),
    (4 , 1),
    (4 , 8),
    (5 , 2),
    (6 , 4),
    (7 , 7),
    (8 , 8); """
    
    assPerCourse_data = """ insert into assignmentspercourse(assignments_ID, courses_ID) 
    values (1 , 6),
    (2 , 6),
    (3 , 6),
    (4 , 6),
    (5 , 6),
    (6 , 6),
    (7 , 6),
    (8 , 6); """

    with connection.cursor() as cursor:
        print("Inserting dummy data to the tables: \n")
        cursor.execute(assignments_data)
        connection.commit()
        print("Assignments data inserted!")
        time.sleep(0)        
        cursor.execute(trainers_data)
        connection.commit()
        print("Trainers data inserted!")
        time.sleep(0)  
        cursor.execute(course_data)
        connection.commit()
        print("Course data inserted!")
        time.sleep(0)          
        cursor.execute(students_data)
        connection.commit()
        print("Students data inserted!")
        time.sleep(0)  
        cursor.execute(stdsPerCourse_data)
        connection.commit()
        print("StdsPerCourse data inserted!")
        time.sleep(0)          
        cursor.execute(assPerCourse_data)
        connection.commit()
        print("AssPerCourse data inserted!")
        time.sleep(0)  

def displayStudents(connection):
    sql_insert_query = "select * from students;"
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()
        print("ID | FirstName | LastName | DateOfBirth | TuitionFees \n")
        for row in result:            
            print(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}')

def displayStdsPerCourse(connection):
    sql_insert_query = """select students.ID as StudentsID, students.FirstName as First_Name, students.LastName as Last_Name,
    courses.ID as Courses_ID, courses.Title as Courses_Title, courses.Stream as Course_Stream,
    courses.Type as Course_Type
    from students, courses, studentspercourse
    where students.ID = studentspercourse.Students_ID and courses.ID = studentspercourse.Courses_ID
    order by courses.Title, students.FirstName;"""
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()
        print("Students ID | First_Name | Last_Name | Course_ID | Course_Title | Course_Stream | Course_Type  \n")
        for row in result:            
            print(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}')

def displayStdsMultipleCourses(connection):
    sql_insert_query = """select students.ID as StudentID, students.FirstName as FirstName, students.LastName as LastName,
    count(*) as NumberOfCourses
    from students, studentspercourse, courses
    where students.ID = studentspercourse.students_ID
    and courses.ID = studentspercourse.Courses_ID
    group by students.ID, students.FirstName, students.LastName
    having count(*) > 1;"""
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()
        print("Students_ID | First_Name | Last_Name | Number Of Courses  \n")
        for row in result:            
            print(f'{row[0]},{row[1]},{row[2]},{row[3]}')

def addNewStudent(connection):
    while True:
        try: 
            FirstName = input("Enter Students First name: ")
        except ValueError:
            print("Invalid Input!")
            continue
        if FirstName == "":
            print("This field cant be empty!")
            continue
        break
    while True:
        try: 
            LastName = input("Enter Students Last name: ")
        except ValueError:
            print("Invalid Input!")
            continue
        if LastName == "":
            print("This field cant be empty!")
            continue
        break
    while True:
            try:
                DateInput = input("Enter Date Of Birth (format YYYY-MM-DD): ")
                y, m, d = map(int, DateInput.split('-'))
                Date = date(y, m, d)
                if DateInput == "":
                    print("This field cant be empty!")
                    continue
                break
            except ValueError:
                print("Date is not in correct format (YYYY-MM-DD). Try again ")
                continue 
    while True:
        try: 
            TuituinFees = float(input("Enter Tuition Fees(accepted values up to 9999): "))
        except ValueError:
            print("Invalid Input TuitionFees Should be numeric!")
            continue
        if TuituinFees == "":
            print("This field cant be empty!")
            continue
        break
    Date = str(Date)
    TuituinFees = str(TuituinFees)  
    sql_insert_query="insert into students(FirstName,LastName,DateOfBirth,TuitionFees) values ('"+ FirstName +"','"+ LastName +"','"+ Date +"','"+ TuituinFees +"')";  
    with connection.cursor() as cursor:
       cursor.execute(sql_insert_query)
       connection.commit()      
       print("New Student Added")

def displayTrainers(connection):
    sql_insert_query = "select * from trainers;"
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()
        print("ID | FirstName | LastName | Subject\n")
        for row in result:            
            print(f'{row[0]},{row[1]},{row[2]},{row[3]}')

def displayTrainersPerCourse(connection):
    sql_insert_query = """select trainers.ID as TrainersID, trainers.FirstName as First_Name, trainers.LastName as Last_Name,
    courses.ID as CourseID, courses.Title as Course_Title, courses.Stream as Course_Stream,
    Courses.Type as Course_Type
    from Trainers ,Courses 
    where Trainers.ID = courses.TrainersID
    order by Trainers.ID;"""
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()
        print("Trainers_ID | First_Name | Last_Name | Course_ID | Course_Title | Course_Stream | Course_Type\n")
        for row in result:            
            print(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}')

def addNewTrainer(connection):
    while True:
        try:
            FirstName = input("Enter Trainers First name: ")
        except ValueError:
            print("Invalid Input!")
            continue    
        if FirstName == "":
            print("This field cant be empty!")
            continue
        break
    while True:
        try:
            LastName = input("Enter his/her Last name: ")
        except ValueError:
            print("Invalid Input!")
            continue    
        if LastName == "":
            print("This field cant be empty!")
            continue
        break
    while True:    
        try:
            Subject = input("Enter subject: ")
        except ValueError:
            print("Invalid Input!")
            continue               
        if Subject == "":
            print("This field cant be empty!")
            continue
        elif Subject != ("C#" or "Python" or "JavaScript" or "Java"):
            print("Wrong Input! Available options: C# , Python, JavaScript, Java")
            continue
        break
    sql_insert_query="insert into trainers(FirstName,LastName,Subject) values ('"+ FirstName +"','"+ LastName +"','"+ Subject +"')";  
    with connection.cursor() as cursor:
       cursor.execute(sql_insert_query)
       connection.commit()      
       print("New Trainer Added")

def displayAssignments(connection):
    sql_insert_query = "select * from assignments;"
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()
        print("Title | Description | SubmissionDate | OralMark | TotalMark\n")
        for row in result:            
            print(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}')

def displayAssPerCourse(connection):
    sql_insert_query = """select assignments.ID as AssignmentID, assignments.Title as Title, assignments.Description AS Description,
    courses.ID as CourseID, courses.Title as Course_Title, courses.Stream as Course_Stream,
    courses.Type as Course_Type
    from assignments, courses, assignmentspercourse
    where assignments.ID = assignmentspercourse.Assignments_ID and courses.ID = assignmentspercourse.Courses_ID
    order by courses.ID;"""
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()
        print("Assignment_ID | Title | Description | Course_ID | Course_Title | Course_Stream | Course_Type\n")
        for row in result:            
            print(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}')

def displayAssPerStudentPerCourse(connection):
    sql_insert_query = """select assignments.ID as AssignmentID, assignments.Title as Title, assignments.Description AS Description,
    courses.ID as CourseID, courses.Title as Course_Title, courses.Stream as Course_Stream,
    courses.Type as Course_Type, students.ID AS StudentID, students.FirstName AS FirstName, students.LastName AS LastName
    from assignments, courses, students, assignmentspercourse, studentspercourse
    where assignments.ID = assignmentspercourse.Assignments_ID AND courses.ID = assignmentspercourse.Courses_ID
    and students.ID = studentspercourse.Students_ID AND courses.ID = studentspercourse.Courses_ID
    order by assignments.ID;
    """
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()
        print("Assignment_ID | Title | Description | Course_ID | Course_Title | Course_Stream | Course_Type | Student_ID | First_Name | Last_Name\n")
        for row in result:            
            print(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}')

def addNewAssignment(connection):
    while True:
        try:
            Title = input("Enter assignment Title: ")
        except ValueError:
            print("Invalid Input!")
            continue    
        if Title == "":
            print("This field cant be empty!")
            continue
        break
    while True:
        try:
            Description = input("Enter Description: ")
        except ValueError:
            print("Invalid Input!")
            continue    
        if Description == "":
            print("This field cant be empty!")
            continue
        break
    while True:
            try:
                DateInput = input("Enter Submission Date (format YYYY-MM-DD): ")
                y, m, d = map(int, DateInput.split('-'))
                SubDate = date(y, m, d)
                if DateInput == "":
                    print("This field cant be empty!")
                    continue
                break
            except ValueError:
                print("Date is not in correct format (YYYY-MM-DD). Try again ")
                continue
    while True:
        try:
            oralMark = input("Enter oral mark: ")
        except ValueError:
            print("Invalid Input!")
            continue    
        if oralMark == "":
            print("This field cant be empty!")
            continue
        break
    while True:
        try:
            totalMark = input("Enter total mark: ")
        except ValueError:
            print("Invalid Input!")
            continue    
        if totalMark == "":
            print("This field cant be empty!")
            continue
        break
    SubDate = str(SubDate)
    sql_insert_query="insert into assignments(Title,Description,SubmissionDate,OralMark,TotalMark) values ('"+ Title +"','"+ Description +"','"+ SubDate +"','"+ oralMark +"','"+ totalMark +"')";  
    with connection.cursor() as cursor:
       cursor.execute(sql_insert_query)
       connection.commit()      
       print("New Assignment Added")

def displayCourses(connection):
    sql_insert_query = "select * from courses;"
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()
        print("Course_ID | Title | Stream | Type | Start_Date | End_Date | Trainers_ID\n")
        for row in result:            
            print(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}')

def addNewCourse(connection):
    while True:
        try:
            title = input('Enter Coure Title:')
        except ValueError:
            print("Invalid Input!")
            continue    
        if title == "":
            print("This field cant be empty!")
            continue
        break
    while True:    
        try:
            stream = input('Enter Course Stream:')
        except ValueError:
            print("Invalid Input!")
            continue               
        if stream == "":
            print("This field cant be empty!")
            continue
        elif stream != ("C#" or "Python" or "JavaScript" or "Java"):
            print("Wrong Input! Available options: C# , Python, JavaScript, Java")
            continue
        break
    while True:
        try:
            type = input('Enter Course Type:')
        except ValueError:
            print("Invalid Input!")
            continue               
        if type == "":
            print("This field cant be empty!")
            continue 
        elif type != ("Part_Time" or "Full_Time"):
            print("Wrong Input! Available options: Part_Time,Full_Time")
            continue
        break      
    while True:
            try:
                DateInput = input("Enter Course Starting Date (format YYYY-MM-DD): ")
                y, m, d = map(int, DateInput.split('-'))
                startDate = date(y, m, d)
                if DateInput == "":
                    print("This field cant be empty!")
                    continue
                break
            except ValueError:
                print("Date is not in correct format (YYYY-MM-DD). Try again ")
                continue
            
    while True:
            try:
                DateInput = input("Enter Course Starting Date (format YYYY-MM-DD): ")
                y, m, d = map(int, DateInput.split('-'))
                endDate = date(y, m, d)
                if DateInput == "":
                    print("This field cant be empty!")
                    continue
                break
            except ValueError:
                print("Date is not in correct format (YYYY-MM-DD). Try again ")
                continue
    startDate = str(startDate)
    endDate = str(endDate)
    sql_insert_query="insert into courses(Title,Stream,Type,StartDate,EndDate,TrainersID) values ('"+ title +"','"+ stream +"','"+ type +"','"+ startDate +"','"+ endDate +"',(select ID from trainers where Subject='"+ stream +"'))";  
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        connection.commit()      
        print("New course Added")
