from datetime import date
from tabulate import tabulate
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
    use_db = "use schoolms"
    
    with connection.cursor() as cursor:
        cursor.execute(create_db)
        cursor.execute(use_db)
        print("DB schoolms was created succefully!")
        time.sleep(0)



def createTablesInDatabase(connection):    
    Assignments_table = """ create table if not exists Assignments(
    ID int auto_increment  primary key,
	Title varchar(50) NOT NULL,
	Description nvarchar(50) NULL,
	SubmissionDate datetime NULL,
	OralMark decimal(5, 2) NULL,
	TotalMark decimal(5, 2) NULL
    ); """

    Trainers_table  = """ create table if not exists Trainers(
	ID int auto_increment primary key,
    FirstName varchar(45) not null,
    LastName varchar(45) not null,
    Subject varchar(45) not null
    );  """

    Students_table = """ create table if not exists Students(
	ID int auto_increment primary key,
    FirstName varchar(45) not null,
    LastName varchar(45) not null,
    DateOfBirth date not null,
    TuitionFees decimal(6, 2) null
    );  """

    Courses_table = """ create table if not exists Courses(
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
    Students_ID int not null,
    Courses_ID int not null,
    foreign key (Students_ID) references Students(ID),
    foreign key (Courses_ID) references Courses(ID)
    ); """

    with connection.cursor() as cursor:
        cursor.execute(Assignments_table)
        print("Assignments Table was Created!")
        time.sleep(0)
        cursor.execute(Trainers_table)
        print("Trainers Table was Created!")
        time.sleep(0)
        cursor.execute(Students_table)
        print("Students Table was Created!")
        time.sleep(0)
        cursor.execute(Courses_table)
        print("Courses Table was Created!")
        time.sleep(0)
        cursor.execute(assPerCourse_table)
        print("Assignments per Course Table was Created!")
        time.sleep(0)
        cursor.execute(stdsPerCourse_table)
        print("Assignments per Students Table was Created!")
        time.sleep(0)

def insertDummyDataToTables(connection):
    Assignments_data = """ insert into Assignments(Title,Description,SubmissionDate,OralMark,TotalMark)
    values ('Assignment 1','Individual Project 1', '2021/11/29' , 80 ,100),
    ('Assignment 2','Individual Project - Part A', '2021/12/21' , 80 ,100),
    ('Assignment 3','Individual Project - Part B', '2021/02/02' , 80 ,100),
    ('Assignment 4','Second Assignment', '2022/02/24' , 80 ,100),
    ('Assignment 5','Third Assignment', '2022/03/09' , 80 ,100),
    ('Assignment 6','Fourth Assignment', '2022/03/15' , 80 ,100),
    ('Assignment 7','Fifth Assignment', '2022/03/21' , 80 ,100),
    ('Assignment 8','Group Project', '2022/04/26' , 80 ,100); """
    
    Trainers_data = """ insert into Trainers(FirstName,LastName,Subject)
    values ('Name1','Last_Name1','Python'),
    ('Name2','Last_Name2','C#'),
    ('Name3','Last_Name3','Java'),
    ('Name4','Last_Name4','JavaScript'); """

    Course_data = """ insert into Courses(Title,Stream,Type,StartDate,EndDate,TrainersID)
    values ('BC13JAFT','Java','Full_time','2021/10/18','2022/04/20',(select ID from Trainers where Subject='Java')),
    ('BC13JAPT','Java','Part_time','2021/10/18','2022/01/20',(select ID from Trainers where Subject='Java')),
    ('C13C#FT','C#','Full_time','2021/10/18','2022/04/20',(select ID from Trainers where Subject='C#')),
    ('BC13C#PT','C#','Part_time','2021/10/18','2022/01/20',(select ID from Trainers where Subject='C#')),
    ('C13PYFT','Python','Full_time','2021/10/18','2022/04/20',(select ID from Trainers where Subject='Python')),
    ('BC13PYPT','Python','Part_time','2021/10/18','2022/01/20',(select ID from Trainers where Subject='Python')),
    ('C13JSFT','JavaScript','Full_time','2021/10/18','2022/04/20',(select ID from Trainers where Subject='JavaScript')),
    ('BC13JSPT','JavaScript','Part_time','2021/10/18','2022/01/20',(select ID from Trainers where Subject='JavaScript'));"""
    
    Students_data = """ insert into Students(FirstName,LastName,DateOfBirth,TuitionFees)
    values ('Name1','Last_Name1','1994/06/10',2000),
    ('Name2','Last_Name2','1987/06/10',2000),
    ('Name3','Last_Name3','1990/06/10',2000),
    ('Name4','Last_Name4','1976/06/10',2000),
    ('Name5','Last_Name5','1999/06/10',2000),
    ('Name6','Last_Name6','2000/06/10',2000),
    ('Name7','Last_Name7','1994/06/10',2000),
    ('Name8','Last_Name8','1994/06/10',2000); """
    
    stdsPerCourse_data = """ insert into StudentsPerCourse(Students_ID, Courses_ID) 
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
    
    assPerCourse_data = """ insert into AssignmentsPerCourse(Assignments_ID, Courses_ID) 
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
        cursor.execute(Assignments_data)
        connection.commit()
        print("Assignments data inserted!")
        time.sleep(0)        
        cursor.execute(Trainers_data)
        connection.commit()
        print("Trainers data inserted!")
        time.sleep(0)  
        cursor.execute(Course_data)
        connection.commit()
        print("Course data inserted!")
        time.sleep(0)          
        cursor.execute(Students_data)
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
    sql_insert_query = "select * from Students;"
    
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()

    headers = ["ID", "First Name", "Last Name", "Date of Birth", "Tuition Fees"]
    table_data = [(row[0], row[1], row[2], row[3], row[4]) for row in result]

    print(tabulate(table_data, headers=headers, tablefmt="pretty"))

def displayStdsPerCourse(connection):
    sql_insert_query = """select Students.ID as StudentsID, Students.FirstName as First_Name, Students.LastName as Last_Name,
    Courses.ID as Courses_ID, Courses.Title as Courses_Title, Courses.Stream as Course_Stream,
    Courses.Type as Course_Type
    from Students, Courses, StudentsPerCourse
    where Students.ID = StudentsPerCourse.Students_ID and Courses.ID = StudentsPerCourse.Courses_ID
    order by Courses.Title, Students.FirstName;"""
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()

    headers = ["Students ID", "First Name", "Last Name", "Course ID", "Course Title", "Course Stream", "Course Type"]
    table_data = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in result]
    print(tabulate(table_data, headers=headers, tablefmt="pretty"))
    
def displayStdsMultipleCourses(connection):
    sql_insert_query = """select Students.ID as StudentID, Students.FirstName as FirstName, Students.LastName as LastName,
    count(*) as NumberOfCourses
    from Students, StudentsPerCourse, Courses
    where Students.ID = StudentsPerCourse.Students_ID
    and Courses.ID = StudentsPerCourse.Courses_ID
    group by Students.ID, Students.FirstName, Students.LastName
    having count(*) > 1;"""
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()

    headers = ["Students ID", "First Name", "Last Name", "Number of Courses"]
    table_data = [(row[0], row[1], row[2], row[3]) for row in result]

    print(tabulate(table_data, headers=headers, tablefmt="pretty"))

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
    sql_insert_query="insert into Students(FirstName,LastName,DateOfBirth,TuitionFees) values ('"+ FirstName +"','"+ LastName +"','"+ Date +"','"+ TuituinFees +"')";  
    with connection.cursor() as cursor:
       cursor.execute(sql_insert_query)
       connection.commit()      
       print("New Student Added")

def displayTrainers(connection):
    sql_insert_query = "select * from Trainers;"
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()

    headers = ["ID", "First Name", "Last Name", "Subject"]
    table_data = [(row[0], row[1], row[2], row[3]) for row in result]

    print(tabulate(table_data, headers=headers, tablefmt="pretty"))

def displayTrainersPerCourse(connection):
    sql_insert_query = """select Trainers.ID as TrainersID, Trainers.FirstName as First_Name, Trainers.LastName as Last_Name,
    Courses.ID as CourseID, Courses.Title as Course_Title, Courses.Stream as Course_Stream,
    Courses.Type as Course_Type
    from Trainers ,Courses 
    where Trainers.ID = Courses.TrainersID
    order by Trainers.ID;"""
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()

    headers = ["Trainers ID", "First Name", "Last Name", "Course ID", "Course Title", "Course Stream", "Course Type"]
    table_data = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in result]

    print(tabulate(table_data, headers=headers, tablefmt="pretty"))

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
    sql_insert_query="insert into Trainers(FirstName,LastName,Subject) values ('"+ FirstName +"','"+ LastName +"','"+ Subject +"')";  
    with connection.cursor() as cursor:
       cursor.execute(sql_insert_query)
       connection.commit()      
       print("New Trainer Added")

def displayAssignments(connection):
    sql_insert_query = "select * from Assignments;"
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()

    headers = ["Title", "Description", "Submission Date", "Oral Mark", "Total Mark"]
    table_data = [(row[0], row[1], row[2], row[3], row[4], row[5]) for row in result]

    print(tabulate(table_data, headers=headers, tablefmt="pretty"))

def displayAssPerCourse(connection):
    sql_insert_query = """select Assignments.ID as AssignmentID, Assignments.Title as Title, Assignments.Description AS Description,
    Courses.ID as CourseID, Courses.Title as Course_Title, Courses.Stream as Course_Stream,
    Courses.Type as Course_Type
    from Assignments, Courses, AssignmentsPerCourse
    where Assignments.ID = AssignmentsPerCourse.Assignments_ID and Courses.ID = AssignmentsPerCourse.Courses_ID
    order by Courses.ID;"""
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()

    headers = ["Assignment ID", "Title", "Description", "Course ID", "Course Title", "Course Stream", "Course Type"]
    table_data = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in result]

    print(tabulate(table_data, headers=headers, tablefmt="pretty"))

def displayAssPerStudentPerCourse(connection):
    sql_insert_query = """select Assignments.ID as AssignmentID, Assignments.Title as Title, Assignments.Description AS Description,
    Courses.ID as CourseID, Courses.Title as Course_Title, Courses.Stream as Course_Stream,
    Courses.Type as Course_Type, Students.ID AS StudentID, Students.FirstName AS FirstName, Students.LastName AS LastName
    from Assignments, Courses, Students, AssignmentsPerCourse, StudentsPerCourse
    where Assignments.ID = AssignmentsPerCourse.Assignments_ID AND Courses.ID = AssignmentsPerCourse.Courses_ID
    and Students.ID = StudentsPerCourse.Students_ID AND Courses.ID = StudentsPerCourse.Courses_ID
    order by Assignments.ID;
    """
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()

    headers = ["Assignment ID", "Title", "Description", "Course ID", "Course Title", "Course Stream", "Course Type", "Student ID", "First Name", "Last Name"]
    table_data = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) for row in result]

    print(tabulate(table_data, headers=headers, tablefmt="pretty"))

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
    sql_insert_query="insert into Assignments(Title,Description,SubmissionDate,OralMark,TotalMark) values ('"+ Title +"','"+ Description +"','"+ SubDate +"','"+ oralMark +"','"+ totalMark +"')";  
    with connection.cursor() as cursor:
       cursor.execute(sql_insert_query)
       connection.commit()      
       print("New Assignment Added")

def displayCourses(connection):
    sql_insert_query = "select * from Courses;"
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        result = cursor.fetchall()

    headers = ["Course ID", "Title", "Stream", "Type", "Start Date", "End Date", "Trainers ID"]
    table_data = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in result]

    print(tabulate(table_data, headers=headers, tablefmt="pretty"))

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
    sql_insert_query="insert into Courses(Title,Stream,Type,StartDate,EndDate,TrainersID) values ('"+ title +"','"+ stream +"','"+ type +"','"+ startDate +"','"+ endDate +"',(select ID from Trainers where Subject='"+ stream +"'))";  
    with connection.cursor() as cursor:
        cursor.execute(sql_insert_query)
        connection.commit()      
        print("New course Added")
