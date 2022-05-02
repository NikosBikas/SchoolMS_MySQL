# Import the modules needed to run the script.
import sys, os, time, platform
import Lib.sql as sql
from mysql.connector import connect, Error
from getpass import getpass
#
#Function that Checks User OS For Clearing The Screen
def clear():
	if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
		os.system('cls') 
	else:
		os.system('clear')

# Main definition - constants
menu_actions  = {}
students_menu_actions = {}  
trainers_menu_actions = {}
assignments_menu_actions = {}  
courses_menu_actions = {}

# =======================
#     MENUS FUNCTIONS
# =======================

def print_banner(title="School Management System v0.03 - Author: Nikolaos Bikas"):
    print("""
.s5SSSs.                                                    .s5ssSs.  .s5SSSs.  
sS     SS. .s5SSSs. .s    s.  .s5SSSs.  .s5SSSs.  .s        SS SS.S%S SS. 
sS    `:; SS.    SS SS    SS. sS    S%S sS    S%S sS        sS SS S%S sS       
SS        sS    `:; sS    S%S sS    S%S sS    S%S sS        SS :; S%S SS        
`:;;;;.   SS        SSSs. S%S SS    S%S SS    S%S SS        SS    S%S `:;;;;.   
      ;;. SS        SS    S%S SS    S%S SS    S%S SS        SS    S%S       ;;. 
      `:; SS        SS    `:; SS    `:; SS    `:; SS        SS    `:;       `:; 
.,;   ;,. SS    ;,. SS    ;,. SS    ;,. SS    ;,. SS    ;,. SS    ;,. .,;   ;,. 
`:;;;;;:' `:;;;;;:' :;    ;:' `:;;;;;:' `:;;;;;:' `:;;;;;:' :;    ;:' `:;;;;;:' 
""")
    total_len = 80
    if title:
        padding = total_len - len(title) - 4
        print("= {} {}\n".format(title, "=" * padding))
    else:
        print("{}\n".format("=" * total_len)) 

# Main menu
def main_menu():
    clear()
    print_banner()
    print ("Main Menu:")
    print ("")
    print ("1 Manage Students")
    print ("2 Manage Trainers")
    print ("3 Manage Assignments")
    print ("4 Manage Courses")
    print ("0 Quit")
    print ("")
    choice = input("Enter your choice: ")
    exec_menu(choice)
    return

# Execute menu
def exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print_banner()
            print ("Invalid selection, please try again.\n")
            time.sleep(2)
            menu_actions['main_menu']()
    return

# Execute students menu
def exec_menu_students(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        students_menu_actions['students_menu']()
    else:
        try:
            students_menu_actions[ch]()
        except KeyError:
            print_banner()
            print ("Invalid selection, please try again.\n")
            time.sleep(2)
            students_menu_actions['students_menu']()
    return
# Execute trainers menu
def exec_menu_trainers(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        trainers_menu_actions['trainers_menu']()
    else:
        try:
            trainers_menu_actions[ch]()
        except KeyError:
            print_banner()
            print ("Invalid selection, please try again.\n")
            time.sleep(2)
            trainers_menu_actions['trainers_menu']()
    return

# Execute assignments menu
def exec_menu_assignemts(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        assignments_menu_actions['assignments_menu']()
    else:
        try:
            assignments_menu_actions[ch]()
        except KeyError:
            print_banner()
            print ("Invalid selection, please try again.\n")
            time.sleep(2)
            assignments_menu_actions['assignments_menu']()
    return

# Execute courses menu
def exec_menu_courses(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        courses_menu_actions['courses_menu']()
    else:
        try:
            courses_menu_actions[ch]()
        except KeyError:
            print_banner()
            print ("Invalid selection, please try again.\n")
            time.sleep(2)
            courses_menu_actions['courses_menu']()
    return

# Students menu
def students_menu():
    clear()
    print_banner()
    print ("Students managment menu:")
    print ("")
    print ("1 Display a list of all students")
    print ("2 Add a new student")
    print ("3 Display Students per Course")
    print ("4 Display Students that attend more than one course")
    print ("9 Return to main menu")
    print ("")
    choice = input("Enter your choice: ")
    exec_menu_students(choice)
    return
# Menu Item Display all Students
def displayStudents():
    print_banner()
    sql.displayStudents(connection)
    print("")   
    input("Press Enter to return at the Students managment menu...")
    return students_menu()

# Menu Item Add a new Student
def addStudents():
    print_banner()
    sql.addNewStudent(connection)
    input("Press Enter to return at the Students managment menu...")
    return students_menu()

# Menu Item Display Students per Course
def displayStudentsPerCourse():
    print_banner()
    print("")
    sql.displayStdsPerCourse(connection)
    print("")   
    input("Press Enter to return at the Students managment menu...")
    return students_menu()

# Menu Item Display Students that belong  to more than one courses
def displayStudentsMultipleCourses():
    print_banner()
    sql.displayStdsMultipleCourses(connection)
    print("")
    input("Press Enter to return at the Students managment menu...")
    return students_menu()

# Trainers Menu
def trainers_menu():
    clear()
    print_banner()
    print ("Trainers managment menu:")
    print ("")
    print ("1 Display a list of all trainers")
    print ("2 Add a new trainer")
    print ("3 Display Trainers per Course")
    print ("9 Return to main menu")
    print ("")
    choice = input("Enter your choice: ")
    exec_menu_trainers(choice)
    return
# Menu Item Display Trainers
def displayTrainers():
    print_banner()
    sql.displayTrainers(connection)
    print("")
    input("Press Enter to return at the Trainers managment menu...")
    return trainers_menu()

# Menu Item Add a new Trainer
def addTrainer():
    print_banner()
    sql.addNewTrainer(connection)
    input("Press Enter to return at the Trainers managment menu...")
    return trainers_menu()
# Menu Item Display Trainers Per Course
def displayTrainersPerCourse():
    print_banner()
    print("")
    sql.displayTrainersPerCourse(connection)
    print("")
    input("Press Enter to return at the Trainers managment menu...")
    return trainers_menu()
# Assignments Menu
def assignments_menu():
    clear()
    print_banner()
    print ("Assignments managment menu:")
    print ("")
    print ("1 Display a list of all Assignements")
    print ("2 Add a new assignement")
    print ("3 Display Assignements per Course")
    print ("4 Display Assignments per Student")
    print ("9 Return to main menu")
    print ("")
    choice = input("Enter your choice: ")
    exec_menu_assignemts(choice)
    return

def displayAssignments():
    clear()
    print_banner()
    print("\nAssignments are the following:")
    sql.displayAssignments(connection)
    print("")
    input("Press Enter to return at the Assignments managment menu...")  
    return assignments_menu()  

# Menu Item Add a new Assignment
def addAssignment():
    print_banner()
    sql.addNewAssignment(connection)
    input("Press Enter to return at the Assignments managment menu...")
    return assignments_menu()

# Menu Item Display All Assignments per Course
def displayAssignmentsPerCourse():
    print_banner()
    sql.displayAssPerCourse(connection)
    input("Press Enter to return at the Assignments managment menu...")
    return assignments_menu()

# Menu Item Display Al Assignments per Student
def displayAssignmentsPerStudents():
    print_banner()
    sql.displayAssPerStudentPerCourse(connection)
    input("Press Enter to return at the Assignments managment menu...")
    return assignments_menu()

# Courses Menu
def courses_menu():
    clear()
    print_banner()
    print ("Courses managment menu:")
    print ("")
    print ("1 Display list of Courses")
    print ("2 Add a new Course")
    print ("9 Return to main menu")
    print ("")
    choice = input("Enter your choice: ")
    exec_menu_courses(choice)
    return
# Menu Item Display Courses
def printCourses():
    clear()
    print_banner()
    sql.displayCourses(connection)
    print("")
    input("Press Enter to return at the Courses managment menu...")
    return courses_menu()
# Menu Item Add Course
def addCourses():
    clear()
    print_banner()
    sql.addNewCourse(connection)
    print("")
    input("Press Enter to return at the Courses managment menu...")
    return courses_menu()

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    print_banner()
    sql.dropDataBase(connection)
    print("Bye Bye...")
    time.sleep(1)
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': students_menu,
    '2': trainers_menu,
    '3': assignments_menu,
    '4': courses_menu,
    '9': back,
    '0': exit,
}

# Student Menu definition
students_menu_actions = {
    'students_menu': students_menu,
    '1': displayStudents,
    '2': addStudents,
    '3': displayStudentsPerCourse,
    '4': displayStudentsMultipleCourses,
    '9': back,
}

# Trainers Menu definition
trainers_menu_actions = {
    'trainers_menu': trainers_menu,
    '1': displayTrainers,
    '2': addTrainer,
    '3': displayTrainersPerCourse,
    '9': back,
}
# Assignments Menu definition
assignments_menu_actions = {
    'assignments_menu': assignments_menu,
    '1': displayAssignments,
    '2': addAssignment,
    '3': displayAssignmentsPerCourse,
    '4': displayAssignmentsPerStudents,
    '9': back,
}

# Courses Menu definition
courses_menu_actions = {
    'courses_menu': courses_menu,
    '1': printCourses,
    '2': addCourses,
    '9': back,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    clear()
    print_banner(title="School Management System v0.03 - Author: Nikolaos Bikas || MySQL Login Session!")
    sql.warningMessage()
    clear()
    print_banner(title="School Management System v0.03 - Author: Nikolaos Bikas || MySQL Login Session!")    
    count = 3
    while count != 0:
        try:
            with connect(
                host=input("Enter host address (eg: 127.0.0.1): "),
                user=input("Enter username: "),
                password=getpass("Enter password: "),
            ) as connection:
                print("Connected Successfully!")
                time.sleep(1)
                clear()
                print_banner(title="School Management System v0.03 - Author: Nikolaos Bikas || MySQL Login Session!")
                sql.dropDataBase(connection)
                clear()
                print_banner(title="School Management System v0.03 - Author: Nikolaos Bikas || MySQL Login Session!")
                sql.createDataBaseInMySql(connection)
                time.sleep(1)
                clear()
                print_banner(title="School Management System v0.03 - Author: Nikolaos Bikas || MySQL Login Session!")
                sql.createTablesInDatabase(connection)
                time.sleep(1)
                clear()
                print_banner(title="School Management System v0.03 - Author: Nikolaos Bikas || MySQL Login Session!")
                sql.insertDummyDataToTables(connection)
                time.sleep(1)
                clear()
                main_menu()
        except Error as e:
            count -= 1
            clear()
            print_banner(title="School Management System v0.03 - Author: Nikolaos Bikas || MySQL Login Session!") 
            print(f"Error Message: {e}!")
            input("")            
            continue
        break


