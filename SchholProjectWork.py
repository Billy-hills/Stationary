import csv
import sys
f=open("d:\emoji.csv")
data=csv.reader(f)
checkpswrd=1
checkid=1
user=input("Enter id:")
for r in data:
    if (r[0]==user):
        checkid=0
        p=input("enter password")
        if (r[1]==p):
            checkpswrd=0
            print("\nHello",user,"welcome")
            break
f.close()
if (checkid==1):
    sys.stderr.write("\n\nInvali Id Try again")
elif (checkpswrd==1):
    sys.stderr.write("\nKya",user,"password bhul gaye")
else:
    import os
    while(True):
        print("\n1.Add Record")
        print("\n2.Display all record")
        print("\n3.Search student record by name")
        print("\n4.Search student record by rollno.")
        print("\n5.Delete student record by name")
        print("\n6.Update student record by name")
        print("\n7.To exit\n")
        n=int(input("Enter your choice="))
        if (n==7):
            break
        elif (n==1):
            try:
                print("\nEnter student details\n")
                n=input("Enter name:")
                cl=input("Enter class:")
                roll=input("Enter rollno:")
                fees=input("Enter fees:")
                per=input("Enter percentage:")
                f=open("d:/data.txt","a")
                f.write(n+"-"+roll+'-'+cl+'-'+fees+'-'+per+"\n")
                f.close()
            except ValueError:
                sys.stderr.write("Enter Valid values!")
        elif (n==2):
            try:
                f=open("d:/data.txt","r")
                s=f.read()
                l=len(s)
                if (l==0):
                    sys.stderr.write("Empty File Add Record!!")
                else:
                    print(".......Records are.......")
                    print("Name-Rollno.-class-Fees-Percentage")
                    print(s)
                f.close()
            except FileNotFoundError:
                sys.stderr.write("Add values to your file first!!")
        elif (n==3):
            try:
                f=open("d:/data.txt","r")
                s=input("Enter student name:")
                flag=0
                while (True):
                    t=f.readline()
                    l=len(t)
                    if (l==0):
                        break
                    g=t.split('-')
                    if (g[0]==s):
                        print("\nRecord found")
                        print("Name is=",g[0])
                        print("Rollno. is=",g[1])
                        print("Class is=",g[2])
                        print("Fees is=",g[3])
                        print("Percentage is=",g[4])
                        flag=1
                        break
                    if (flag==0):
                        sys.stderr.write("Record not found!!")
                f.close()
            except FileNotFoundError:
                sys.stderr.write("Add Record First!!!")
        elif (n==4):
            try:
                f=open("d:/data.txt","r")
                s=input("Enter student rollno:")
                flag=0
                while (True):
                    t=f.readline()
                    l=len(t)
                    if (l==0):
                        break
                    g=t.split('-')
                    if (g[1]==s):
                        print("\nRecord found")
                        print("Name is=",g[0])
                        print("Rollno. is=",g[1])
                        print("Class is=",g[2])
                        print("Fees is=",g[3])
                        print("Percentage is=",g[4])
                        flag=1
                        break
                    if (flag==0):
                        sys.stderr.write("No such record found try again!!")
                f.close()
            except FileNotFoundError:
                sys.stderr.write("Add Record First!!!")
        elif (n==5):
            try:
                f=open("d:/data.txt","r")
                t=open("d:/khali.txt","w")
                s=input("Enter student name=")
                h=0
                flag=0
                while(True):
                    q=f.readline()
                    l=len(q)
                    if (l==0):
                        break
                    g=q.split('-')
                    if (g[0]!=s):
                        t.write(q)
                    if(g[0]==s):
                        h=1
                f.close()
                t.close()
                if (h==1):
                    print("Record Deleted succesfully :)")
                    os.remove("d:/data.txt")
                    os.rename("d:/khali.txt","d:/data.txt")
                elif (h==0):
                    sys.stderr.write("No such record found try again!!")
            except FileNotFoundError:
                sys.stderr.write("Add Record First!!!")
        elif (n==6):
            try:
                h=0
                f=open("d:/data.txt","r")
                tt=open("d:/khali.txt","w")
                s=input("Enter student name=")
                flag=0
                while(True):
                    t=f.readline()
                    l=len(t)
                    if(l==0):
                        break
                    g=t.split('-')
                    if(g[0]==s):
                        print("Current details\n",t)
                        print("-------------")
                        newroll=input("Want to change rollno.?Enter new else press enter=")
                        newcl=input("Want to change class?Enter new else press enter=")
                        newfees=input("Want to change fees?Enter new else press enter=")
                        newper=input("Want to change persentage?Enter new else press enter=")
                        if(len(newroll)==0):
                            newroll=g[1]
                        if (len(newcl)==0):
                            newcl=g[2]
                        if (len(newfees)==0):
                            newfees=g[3]
                        if (len(newper)==0):
                            newper=g[4]
                        tt.write("\n"+g[0]+"-"+newroll+"-"+newcl+"-"+newfees+"-"+newper+"\n")
                        h=1
                        break
                    else:
                        tt.write(t)
                f.close()
                tt.close()
                if (h==1):
                    print("Record Updated")
                    os.remove("d:/data.txt")
                    os.rename("d:\khali.txt","d:/data.txt")
                elif (h==0):
                    sys.stderr.write("No such record found try again!!")
            except FileNotFoundError:
                sys.stderr.write("Add Record First!!!")
            except ValueError:
                sys.stderr.write("Enter a word not number :(")
    print("\nBye",user)
    input()
