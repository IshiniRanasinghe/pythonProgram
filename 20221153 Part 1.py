#Author name: Ishini S. Ranasinghe
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:20221153
# Date: 5 December 2022

Progress=0
Trailer=0
Retriever=0
Excluded=0

range_of_marks =[0,20,40,60,80,100,120]

def check(abc):
    while True :        
        try:
            level =int(input(abc))
            if level not in range_of_marks:
                print("Out of range")
                continue
            break
        
        except ValueError:
            print("integer required")
            continue

    return level
print("Choose Your Option\n1 = Student\n2 = Staff")
while True:
    try:
        user = int(input("\nWould you prefer to continue as a staff member or a student?(please enter the number):"))
        if user!= 1 and user!= 2:
            print("Invalid Input")
            continue
        break
    except :
        print("Invalid Input")
        
while True:
    level_1=check("\nplease Enter volume of credit at PASS: ")
    level_2=check("please Enter volume of credit at DEFER : ")       
    level_3=check("please Enter volume of credit at FAIL: ")
    
    if level_1 + level_2 + level_3 == 120:
        if level_1==120:
            Progress=Progress+1
            print("Progress")                    
        elif level_1==100:
            Trailer=Trailer+1
            print("progress(module trailer)")            
        elif level_1 + level_2 >= level_3 :
            Retriever=Retriever+1
            print("Do not progress-module retriever")                                                                                                                                                                            
        elif level_1 + level_2 < level_3 :
            Excluded=Excluded+1
            print("Exclude")                
    else :
        print("Total incorrect")
        continue
    if user== 1:
        break
    
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
        print("............................................................")        
        break 
        
    
    
            
        

