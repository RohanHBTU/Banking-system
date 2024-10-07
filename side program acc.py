import time
import datetime
def loading(line):
     print('',end="")
     print()
     print(line,end="")
     for j in range(4):
          time.sleep(1)
          print('.', end='')
     print()
     print()
     time.sleep(0.5)
def again(input_field,count):
     if count<2:
          input_field=input("                                               You have entered incorrect value, please re-enter >>  ")
     else:
          input_field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
     return input_field
def acc_check():
     global ch
     ch=1
     count1=0
     acc=input("                                                    Do you already have an account(s) with us.(Y/N) >>  ")
     print('',end='')
     while acc.upper() not in ('YES','Y','NO','N'):
          count1+=1
          acc=again(acc,count1)
          if count1>=2 and acc.upper()=='Q':
               ch=2
               print('',end="")
               print()
               break
     if ch!=2:
          if acc.upper() in ('YES','Y'):
               print()
               username=input("                                                          Enter your UserID >>  ")
               PIN=input("                                                             Enter your PIN >>  ")
               loading("                                                                       Loading")
               print("Successfully Logged In".center(154))
               #database se iD aur pin pata laga ke aage transac karna
          else:
               print()
               print("For registering with us: ".center(154))
               print()
               username=input("                                                          Enter your New UserID >>  ")
               name=input("                                                           Enter your Full Name >>  ")
               sex=input("                                                            Enter your sex(M/F) >>  ")
               add=input("                                                   Enter your Address(In short) >>  ")
               city=input("                                                                Enter your City >>  ")
               dob=input("                                           Enter your Date of birth(YYYY-MM-DD) >>  ")
               mob=input("                                                       Enter your mobile number >>  ")
               email=input("                                                      Enter your E-mail address >>  ")
               while True:
                    newPIN1=input("                                                             Enter your New PIN >>  ")
                    newPIN2=input("                                                           Enter your PIN again >>  ")
                    if newPIN1==newPIN2:
                         #database mei id aur pin save karo
                         loading("                                                                       Loading")
                         print("Your account has been successfully registered and Logged In".center(154))
                         break
                    print()
                    print("Both Pins Didn't match, please re-enter".center(154))
                    print()
def menu():
     print('',end='')
     print()
     print()
     print("                                           Hello username, Today is",datetime.date.today(),".")
     #username ki jagah jis username se login hua hai vo aayega
     print()
     print("We offer Following Services:".center(135))
     print()
     print("                                                               >>  Pay                   (1)")
     print("                                                               >>  Passbook              (2)")
     print("                                                               >>  Deposit Money         (3)")
     print("                                                               >>  Open another Account  (4)")
     print("                                                               >>  Close Account         (5)")
     print("                                                               >>  Exit                  (6)")
     print()
     option=input("                                     To Choose any above option, type the number in front of them >>  ")
     '''if option==1:
          
     elif option==2:
     elif option==3:
     elif option==4:
     elif option==5:'''
acc_check()
while ch!=2:
     menu()
     ch=2
else:
     print()
     print("Thank you for your valuable time".center(154))

