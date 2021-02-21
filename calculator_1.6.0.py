# MENU functions ######################################################################
def intro_screen():
    print("--------------------------------------------------------------")
    print("")
    print("Welcome to the calculator!")
    print("")
    print("This scrpit was written by Samuel Howell.")
    print("The source code is available via email -howsamuel33@gmail.com.")
    print("Work is being done to improve the overall funtionality of this")
    print("program. Contrabutions are welcomed.")
    print("Version 1.6.0")
    print("")
    print("--------------------------------------------------------------")
 
def mode_list():
    print("")
    print("--------------------------------------------------------------")
    print("Calculator v1.6.0")
    print("")
    print("MAIN MENU")
    print("")
    print("1. Basic operations")
    print("2. Pythagoras Theorem")
    print("3. Other functions")
    print("")
    print("4. Help")
    print("5. Developer contact")
    print("--------------------------------------------------------------")
def contact():
    while True:
        print("")
        print("--------------------------------------------------------------")
        print("DEVELOPER CONTACT")
        print("")
        print("Email - howsamuel33@gmail.com")
        print("")
        print("SOCIAL MEDIA")
        print("snapchat - ")
        print("Instagram - @howell_sam101")
        print("")
        print("Contact via DMs or email to suggest changes and to report bugs.")
        print("The project is available on git hub by going to the following")
        print("link: https://github.com/howellsam101/calculator")
        print("")
        print("--------------------------------------------------------------")
        print("Press enter to go back")
        print("--------------------------------------------------------------")
        print("")
        exit = input("")
        if exit == '':
            break
        if exit == 'back':
            break
            
def help_menu():
    while True:
        print("--------------------------------------------------------------")
        print("CALCULATOR HELP MENU")
        print("")
        print("Operation codes:")
        print(" Type 'back' at any time to go to previous page.")
        print(" Type 'exit' in main menu to exit program.")
        print(" Type 'help' at any time to access this page")
        print("")
        print("Error codes: ")
        print(" Enter a number!  - A number (e.g 1,2,3) is required")
        print("                    no letters, no space.")
        print(" Nothing entered! - This is displayed when enter is")
        print("                    is pressed without entering an")
        print("                    an input.")
        print(" Process finished - means that calculation complete or")
        print("                    input did not match any. Use the")
        print("                    input guide at the start.")
        print("")
        print("Report bugs to howsamuel33@gmail.com or DM @howell_sam101 on instagram.")
        exit = input("")
        if exit == 'back':
            break
    
def basic():
    while True:
        print("")
        print("--------------------------------------------------------------")
        print("Basic operations")
        print("--------------------------------------------------------------")
        print("")
        mode = input("Enter equation: ").replace("^", "**").replace("x", "*")
    
        if mode == 'back':
            break
            
        if mode == 'exit':
            exit()
            
        else:
            answer = eval(mode)
            while True:
                print("--------------------------------------------------------------")
                print(mode,"= ",answer)
                print("--------------------------------------------------------------")
                print("Press enter to continue.")
                stop = input("")
                
                if stop == '':
                    break
        
            
def pythagoras():
    while True:
        print("--------------------------------------------------------------")
        print("1. Find side a")
        print("2. Find side b")
        print("3. Find side c")
        print("--------------------------------------------------------------")
        
        mode = input("Option: ")
        if mode == '1':
            find_a()
        if mode == '2':
            find_b()
        if mode == '3':
            find_c()
        if mode == 'help':
            help_menu()
        if mode == 'back':
            break
        
        
def other_modes():
    while True:
        print("--------------------------------------------------------------")
        print("Other Modes:")
        print("1. Quadratics")
        print("2. PI")
        print("3. Physics")
        print("--------------------------------------------------------------")
        mode = input("Enter operation code: ")
        if mode == '1':
            quadratics()
        if mode == '2':
            PI()
        if mode == '3':
            physics()
        if mode == 'help':
            help_menu()
        if mode == 'back':
            break

def physics():
    while True:
        print("Physics options:")
        print("1. Distance formula")
        print("2. Coming soon!")
        mode = input("Option: ")
        if mode == '1':
            distance()
        if mode == '2':
            print("Check back in futre updates.")
        if mode == 'help':
            help_menu()
        if mode == 'back':
            break

# Formula FUNCTIONS #####################################################################

def distance():
    while True:
        print("Solve for:")
        print("1. Speed")
        print("2. Time")
        print("3. Distance")
        mode = input("Option: ")
        if mode == '1':
            speed()
        if mode == '2':
            time()
        if mode == '3':
            distance()
        if mode == 'help':
            help_menu()
        if mode == 'back':
            break
        

def speed():
    while True:
        while True:
            try:
                distance = float(input("Enter distance:" ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        while True:
            try:
                time = float(input("Enter time: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        speed = distance/time
        print("--------------------------------------------------------------")
        print("The speed is: ", speed)
        print("--------------------------------------------------------------")
        print("Press enter to continue.")
        exit = input("")
        if exit == '':
            break
        
def time():
    while True:
        while True:
            try:
                distance = float(input("Enter distance: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        while True:
            try:
                speed = float(input("Enter speed: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        time = distance/speed
        print("--------------------------------------------------------------")
        print("The time is: ", time)
        print("--------------------------------------------------------------")
        print("Press enter to continue.")
        exit = input("")
        if exit == '':
            break
            
def distance():
    while True:
        while True:
            try:
                speed = float(input("Enter speed: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        while True:
            try:
                time = float(input("Enter time: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        distance = speed*time
        print("--------------------------------------------------------------")
        print("The speed is: ", distance)
        print("--------------------------------------------------------------")
        print("Press enter to continue.")
        exit = input("")
        if exit == '':
            break
            
def PI():
    while True:
        print("PI options:")
        print("1. Radius")
        print("2. Circumfernce")
        print("3. Diameter")
        print("4. Area")
        print("")
        mode = input("Option: ")
        if mode == '1':
            radius()
        if mode == '1':
            circumfernce()
        if mode == '1':
            diameter()
        if mode == '1':
            area()
        if mode == 'help':
            help_menu()
        if mode == 'back':
            break
            
def radius():
    while True:
        while True:
            try:
                area = int(input("Enter area: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        PI = 3.1415
        radius = (area/PI)**0.5
        print("--------------------------------------------------------------")
        print("Radius of circle = %.2f" %radius)
        print("--------------------------------------------------------------")
        print("Press enter to continue.")
        exit = input("")
        if exit == '':
            break
            
def circumfernce():
    while True:
        while True:
            try:
                radius = int(input("Enter radius: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        PI = 3.1415
        circumfernce = 2*PI*radius
        print("--------------------------------------------------------------")
        print(" Circumference of circle = %.2f" %circumference)
        print("--------------------------------------------------------------")
        print("Press enter to continue.")
        print("")
        exit = input("")
        if exit == '':
            break
            
def diameter():
    while True:
        while True:
            try:
                radius = int(input("Enter radius: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        PI = 3.1415
        diameter = 2*radius
        print("--------------------------------------------------------------")
        print("Diameter of circle = %.2f" %diameter)
        print("--------------------------------------------------------------")
        print("Press enter to continue.")
        print("")
        exit = input("")
        if exit == '':
            break
            
def area():
    while True:
        while True:
            try:
                radius = int(input("Enter radius: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        PI = 3.1415
        area = PI*radius*radius
        print("--------------------------------------------------------------")
        print("Area of circle = %.2f" %area)
        print("--------------------------------------------------------------")
        print("Press enter to continue.")
        print("")
        exit = input("")
        if exit == '':
            break

def quadratics():
    while True:
        print("")
        print("(A quadratic eqaution is written as: ax^2+bx+c)")
        print("")
        while True:
            try:
                a = int(input("Enter a: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        while True:
            try:
                b = int(input("Enter b: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        while True:
            try:
                c = int(input("Enter c: " ))
                break
            except ValueError:
                print("Enter a number!")
                continue
        answer = ((b**2 - 4*a*c)**0.5)
        positive = (-b + answer) / (2*a)
        negative = (-b - answer) / (2*a)
        print("--------------------------------------------------------------")
        print("The positive value of the quadratic is:", positive)
        print("The negative value of the quadratic is:", negative)
        print("--------------------------------------------------------------")
        print("Press enter to continue")
        print("")
        exit = input("")
        if exit == '':
            break

def find_a():
    while True:
        while True:
            try:
                num1 = float(input("Enter side b: "))
                break
            except ValueError:
                print("Enter a number!")
                continue
        while True:
            try:
                num2 = float(input("Enter side c: "))
                break
            except ValueError:
                print("Enter a number!")
                continue
            
        answer = ((num2**2 - num1**2)**0.5)
        print("--------------------------------------------------------------")
        print("The length of side a is: ",answer)
        print("--------------------------------------------------------------")
        print("Press enter to continue")
        print("")

        exit = input("")
        if exit == '':
            break
            
def find_b():
    while True:
        while True:
            try:
                num1 = float(input("Enter side a: "))
                break
            except ValueError:
                print("Enter a number!")
                continue
        while True:
            try:
                num2 = float(input("Enter side c: "))
                break
            except ValueError:
                print("Enter a number!")
                continue
                
        answer = ((num2**2 - num1**2)**0.5)
        print("--------------------------------------------------------------")
        print("The length of side b is: ",answer)
        print("--------------------------------------------------------------")
        print("Press enter to continue")
        print("")
        exit = input("")
        if exit == '':
            break
            
def find_c():
    while True:
        while True:
            try:
                num1 = float(input("Enter side a: "))
                break
            except ValueError:
                print("Enter a number!")
                continue
        while True:
            try:
                num2 = float(input("Enter side b: "))
                break
            except ValueError:
                print("Enter a number!")
                continue
        answer = ((num1**2 + num2**2)**0.5)
        print("--------------------------------------------------------------")
        print("The length of side c is: ",answer)
        print("--------------------------------------------------------------")
        print("Press enter to continue")
        print("")
        exit = input("")
        if exit == '':
            break


 
# MAIN LOOP ############################

intro_screen()

while True:
    mode_list()
    mode = input("Enter option: ")
    print("--------------------------------------------------------------")
    
    if mode == '1':
        basic()
    if mode == '2':
        pythagoras()
    if mode == '3':
        other_modes()
    if mode == '4':
        help_menu()
    if mode == '5':
        contact()
        
    if mode == '':
        print("Nothing entered!")
        print("")
        continue
    if mode == 'exit':
        print("--------------------------------------------------------------")
        print("//////////////////////////////////////////////////////////////")
        print("")
        print("BYE, ")
        print("")
        break
    else:
        print("Process ended")

