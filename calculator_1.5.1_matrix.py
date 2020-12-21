#definitions
import fcntl
import time
import random
import struct
import sys
import termios


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
def multiply (x, y):
    return x * y
def divide(x, y):
    return x / y
def hypot (x, y):
    return (x**2 + y**2)**0.5
def a(x, y, z):
    return (z**2 - y**2)**0.5
def b(x, y, z):
    return (z**2 - x**2)**0.5
    
#opening print
    
print("--------------------------------------------------------------")
print("")
print("Welcome to the calculator!")
print("")
print("This scrpit was written by Samuel Howell.")
print("The source code is available via email -howsamuel33@gmail.com.")
print("Work is being done to improve the overall funtionality of this")
print("program, and contrabutions are welcomed.")
print("Version 1.5.0")
print("")
print("--------------------------------------------------------------")
print("")
print("Operations:")
print("")
print("Basic operations:                   To go to prevoius")
print(" 1.Addition                         page type 'back' at")
print(" 2.Subtraction                      any time.")
print(" 3.Multiplication")
print(" 4.Division                         To exit program,")
print("                                    type, exit/kil/quit")
print("Pythagoras Theorem:")
print(" 5.Find side a                      type 'info for more")
print(" 6.Find side b                      information")
print(" 7.Find side c")
print("                                    Error list: 'error info'")

print("Other functions:")
print(" 8.Quadratic equations")
print(" 9.PI equations:")
print(" 10.Physics")
print("")

print("--------------------------------------------------------------")


#code loop ////////////////////////////

while True:
   choice = input("Enter operation code: ")
   
   #basic facts
   if choice == '':
    print("Nothing entered!")
    continue
    
    
   if choice in ('1', '2', '3', '4'):
   
    while 1:
    
     try:
      num1 = float(input("Enter a: "))
      break
     except ValueError:
      print("Enter a number!")
      continue
      
    while 1:
    
     try:
      num2 = float(input("Enter b: "))
      break
     except ValueError:
      print("Enter a number!")
      continue
      
    while 1:
    
      if choice == '1':
           print("------------")
           print("Answer =",add(num1, num2))
           print("------------")
           break
      if choice == '2':
           print("------------")
           print("Answer =",subtract(num1, num2))
           print("------------")
           break
      if choice == '3':
           print("------------")
           print("Answer =",multiply(num1, num2))
           print("------------")
           break
      if choice == '4':
           print("------------")
           print("Answer =",divide(num1, num2))
           print("------------")
           break
      
#/////////////////////////
#pythagorus
        
   if choice in ('5'):
   
    while 2:
    
     try:
      num2 = float(input("Enter side b: "))
      break
     except ValueError:
      print("Enter a number!")
      continue
      
    while 2:
    
     try:
      num3 = float(input("Enter side c: "))
      print("-------------------------------------------------")
      break
     except ValueError:
      print("Enter a number!")
      
      continue
    while 2:
      if choice == '5':
         the=num3**2 - num2**2
         sidea = the**0.5
         
         print("The length of side a is: ",sidea)
         print("-------------------------------------------------")
         break
         
   if choice in ('6',):
   
    while 3:
    
     try:
      num1 = float(input("Enter side a: "))
      break
     except ValueError:
      print("Enter a number!")
      continue
      
    while 3:
    
     try:
      num3 = float(input("Enter side c: "))
      print("-------------------------------------------------")
      break
     except ValueError:
      print("Enter a number!")
      continue
      
    while 3:
    
      if choice == '6':
         sum=num3**2 - num1**2
         sideb = sum**0.5
         print("The length of side b is: ", sideb)
         print("-------------------------------------------------")
         break

   if choice in ('7'):
   
    while 4:
    
     try:
      num1 = float(input("Enter side a: "))
      break
     except ValueError:
      print("Enter a number!")
      continue
      
    while 4:
    
     try:
      num2 = float(input("Enter side b: "))
      print("-------------------------------------------------")
      break
     except ValueError:
      print("Enter a number!")
      continue
      
    while 4:
    
      if choice == '7':
         hypo = num1**2 + num2**2
         sideh = hypo**0.5
         print("The length of the hypotenuse is: ", sideh)
         print("-------------------------------------------------")
         break

# quadratics //////////////

   if choice in ('8'):
    while 5:
     print("")
     print(" (Quadratic eqaution written as: ax^2+bx+c)")
     print("")
    
     while 5:
    
      try:
       a = int(input("Enter a:" ))
       break
      except ValueError:
       print("Enter a number!")
       continue
      
     while 5:
    
      try:
       b = int(input("Enter b:" ))
       break
      except ValueError:
       print("Enter a number!")
       continue
      
     while 5:
    
      try:
       c = int(input("Enter c:" ))
       break
      except ValueError:
       print("Enter a numnber!")
       continue
     
     while 5:
    
       if choice == '8':
         disc = b**2 - 4*a*c
         disc1 = (disc)**0.5
         positive = (-b + disc1) / (2*a)
         negative = (-b - disc1) / (2*a)
         print("---------------------------------------------------")
         print("The positive value of the quadratic is:", positive)
         print("The negative value of the quadratic is:", negative)
         print("---------------------------------------------------")
         break
     

# PI and circles/////////////

   if choice in ('9'):
        print("--------------------------------------------------------------")
        print("Solve for:")
        print("1. Radius")
        print("2. Circumfernce")
        print("3. Diameter")
        print("4. Area")
        print("")
        
        while 1:
        
          pick = input("Enter selection: ")
          
          if pick in ('4'):
          
           while 2:
          
            try:
             radius = int(input("Enter radius: "))
             print("---------------------------------------------------")
             break
            except ValueError:
             print("Enter a number!")
             continue
             
           while 2:
           
            if pick == '4':
            
             PI = 3.1415
             area = PI * radius * radius
             print(" Area of circle = %.2f" %area)
             print("---------------------------------------------------")
             break
    
          
          if pick in ('3'):
          
           while 2:
           
            try:
             radius = int(input("Enter radius: "))
             print("---------------------------------------------------")
             break
            except ValueError:
             print("Enter a number!")
             continue
             
           while 2:
            if pick == '3':
             PI = 3.1415
             diameter = 2 * radius
             print(" Diameter of circle = %.2f" %diameter)
             print("---------------------------------------------------")
             break
             
          if pick in ('2'):
          
           while 2:
            
            try:
             radius = int(input("Enter radius: "))
             print("---------------------------------------------------")
             break
            except ValueError:
             print("Enter a number!")
             continue
             
           while 2:
            if pick == '2':
             PI = 3.1415
             circumference = 2 * PI * radius
             print(" Circumference of circle = %.2f" %circumference)
             print("---------------------------------------------------")
             break
             
          if pick in ('1'):
          
           while 2:
            
            try:
             area = int(input("Enter area: "))
             print("---------------------------------------------------")
             break
            except ValueError:
             print("Enter a number!")
             continue
             
           while 2:
            if pick == '1':
             PI = 3.1415
             radius = (area/PI)**0.5
             print(" Radius of circle = %.2f" %radius)
             print("---------------------------------------------------")
             break
          if pick == 'back':
           break
          break
          
 # physics //////////
 
   if choice == '10':
       print("")
       print("Physics calculations:")
       print(" 1. Speed, Distance, Time")
       print(" 2. coming soon!")
       print("")
       
       while 1:
       
        select = input("Enter Selection: ")
        #print text info
        if select in ('1'):
          print("")
          print("solve for:")
          print("1.velocity")
          print("2.time")
          print("3.distance")
          
          print("")
          while 1:
          
           sdt = input("Enter mode: ")
           
           if sdt in ('1'):
            while 1:
             try:
              distance = float(input("Enter distance: "))
              break
             except ValueError:
              print("Enter only numbers!")
              continue
              
            while 1:
             try:
              time = float(input("Enter time: "))
              break
             except ValueError:
              print("Enter only numbers!")
              continue
              
            while 1:
             if sdt == '1':
              speed = distance/time
              print("The velocity is: ", speed)
              break
             
           if sdt == 'back':
              break
 
           if sdt in ('2'):
            while 1:
             try:
              speed = float(input("Enter speed: "))
              break
             except ValueError:
              print("Enter only numbers!")
              continue
            while 1:
             try:
              distance = float(input("Enter distance: "))
              break
             except ValueError:
              print("Enter only numbers!")
              continue
              
            while 1:
             if sdt == '2':
              time = distance/speed
              print("The time taken is: ",time)
              break
              
           if sdt in ('3'):
           
            while 1:
             try:
              speed = float(input("Enter the velocity: "))
              break
             except ValueError:
              print("Enter only numbers!")
              continue
            while 1:
             try:
              time = float(input("Enter the time: "))
             except ValueError:
              print("Enter only numbers!")
              continue
              
            while 1:
             if sdt == '3':
              distance = time*speed
              print("the distance is: ",distance)
              break
          break
          
        if select in ('2'):
          print("")
          print("coming soon")
          break
          
 # exit solutions: /////////////////////////
   if choice == 'info':
    print("")
    print("This calculator scprit is written and edited by")
    print("Samuel Howell. the program is made using python, witten")
    print("in Xcode. This allows it to be cross platform.")
    print("The source code is available for free from developer")
    print("cantact via email (howsamuel33@gmail.com) or IG @howell_sam101")
    print("Work is being done to improve the overall funtionality of this")
    print("program, and contrabutions are welcomed")
    print("secret code: 2020")
    print("Created on 20th sep 2020.")
    print("Version: 1.5.0")
    print("")
    
   if choice == 'kill':
    print("")
    print("BYE BYE")
    print("")
    break
   
   if choice == 'quit':
    print("")
    print("BYE BYE")
    print("")
    break
   if choice == 'exit':
    print("")
    print("BYE BYE")
    print("")
    break
    
    
   if choice == 'error info':
    print("--------------------------------------------------------------")
    print("Welcome to error page.")
    print("")
    print(" Enter a number!   -A number (e.g 1,2,3) is required.")
    print("                    No letters, no space.")
    print(" Nothing entered! - This is displayed when enter is")
    print("                    is pressed without entering an")
    print("                    an input.")
    print(" Process finished - Means that calculation complete or")
    print("                    input did not match any. Use the")
    print("                    input guide at the start.")
    print("")
    print(" Note that inpus must be written exaclty as stated.")
    print("")
    print(" Contact developer about bugs and issues. Thanks. ")
    print("--------------------------------------------------------------")
   if choice == '2020':
     class message(str):
        def __new__(cls, text, speed):
            self = super(message, cls).__new__(cls, text)
            self.speed = speed
            self.y = -1 * len(text)
            self.x = random.randint(0, display().width)
            self.skip = 0
            return self

        def move(self):
            if self.speed > self.skip:
                self.skip += 1
            else:
                self.skip = 0
                self.y += 1


     class display(list):

        def __init__(self):
            self.height, self.width = struct.unpack('hh', fcntl.ioctl(1, termios.TIOCGWINSZ, '1234'))
            self[:] = [' ' for y in range(self.height) for x in range(self.width)]

        def set_vertical(self, x, y, string):
            string = string[::-1]
            if x < 0:
                x = 80 + x
            if x >= self.width:
                x = self.width - 1
            if y < 0:
                string = string[abs(y):]
                y = 0
            if y + len(string) > self.height:
                string = string[0:self.height - y]
            if y >= self.height:
                return
            start = y * self.width + x
            length = self.width * (y + len(string))
            step = self.width
            self[start:length:step] = string

        def __str__(self):
            return ''.join(self)


     def matrix(iterations, sleep_time=.08):
        messages = []
        d = display()
        for _ in range(iterations):
            messages.append(message('10' * 16, random.randint(1, 5)))
            for text in messages:
                d.set_vertical(text.x, text.y, text)
                text.move()
            sys.stdout.write('\033[1m\033[32m%s\033[0m\r' % d)
            sys.stdout.flush()
            time.sleep(sleep_time)


     if __name__ == '__main__':
        while True:
            try:
                matrix(150)
            except KeyboardInterrupt:
                sys.stdout.write('\n\033[1m\033[32m=== Matrix Stopped ====\033[0m\n')
                break



   else:
    print("")
    print("Process finished...")
    print("")
