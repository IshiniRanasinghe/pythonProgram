#Author name: Ishini S. Ranasinghe
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:20221153
# Date:12 December 2022
list_1=[]
list_2=[]
list_3=[]
list_4=[]

mydict = {}

Progress=0
Trailer=0
Retriever=0
Excluded=0

range_of_marks =[0,20,40,60,80,100,120]

def check(prompt):
    while True :        
        try:
            level =int(input(prompt))
            if level not in range_of_marks :
                print("Out of range")
                continue
            break
        
        except ValueError:
            print("integer required")
            continue

    return level

def dictp(outcome,list_name,display):
    while True:
        if outcome>= 1:
            list_name.extend([level_1,level_2,level_3,student_ID])
            final_marks="%s-%d,%d,%d" % (display,list_name[0],list_name[1],list_name[2])
            mydict.update({student_ID:final_marks})
            del (list_name[0:4])
            outcome = outcome - 1
            continue
        else:
            break

while True:
    student_ID= input("Enter Your Student ID number:")
    if len(student_ID) != 8:
        print("Invalid student number")
        continue
    else:
        level_1=check("\nplease Enter volume of credit at PASS: ")
        level_2=check("please Enter volume of credit at DEFER : ")       
        level_3=check("please Enter volume of credit at FAIL: ")

        if level_1 + level_2 + level_3 == 120:    
            if level_1==120:
                Progress=Progress+1
                print("Progress")
                dictp(Progress,list_1,"Progress")                    
            elif level_1==100:
                Trailer=Trailer+1
                print("progress(module trailer)")
                dictp(Trailer,list_2,"Trailer")          
            elif level_1 + level_2 >= level_3 :
                Retriever=Retriever+1
                print("Do not progress-module retriever")
                dictp(Retriever,list_3,"Retriever")
            elif level_1 + level_2 < level_3 :
                Excluded=Excluded+1
                print("Exclude")
                dictp(Excluded,list_4,"Excluded")
        else :
            print("Total incorrect")
            continue
        
        while True:        
            order=str(input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:"))
            if order=='y' or order=='q':
                break
            else:
                print("invalid command")
                continue
        if order == 'y':
            continue
        else:
            Total=Progress+Trailer+Retriever+Excluded        
            print("............................................................\nHistogram")
            print(f"Progress {Progress}\t:","*" * Progress)
            print(f"Trailer {Trailer}\t:","*" * Trailer)
            print(f"Retriever {Retriever}\t:","*" * Retriever)
            print(f"Excluded {Excluded}\t:","*" * Excluded)
            print(Total,"Outcomes in Total.")
            print("............................................................\nPart 4:")
            print(' '.join(f'{key}: {value}' for key, value in mydict.items()))#https://bobbyhadz.com/blog/python-print-dictionary-without-brackets
            break
            
        
        
                
            

