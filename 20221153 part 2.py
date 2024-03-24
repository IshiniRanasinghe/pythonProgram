#Author name: Ishini S. Ranasinghe
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:20221153
# Date: 8 December 2022

list_1=[]
list_2=[]
list_3=[]
list_4=[]

Progress=0
Trailer=0
Retriever=0
Excluded=0

range_of_marks =[0,20,40,60,80,100,120]

def check(lists):
    while True :        
        try:
            level =int(input(lists))
            if level not in range_of_marks:
                print("Out of range")
                continue
            break
        except ValueError:
            print("integer required")
            continue
    return level

def lists(outcome,list_name,display):
    while True:
            if outcome >= 1:
                print(display,end="")
                print(', '.join(map(str,list_name[0:3]))) #https://www.entechin.com/how-to-print-a-list-without-square-brackets-in-python/
                del (list_name[0:3])
                outcome=outcome-1
                continue            
            else:
                break
        
while True:
    level_1=check("\nplease Enter volume of credit at PASS: ")
    level_2=check("please Enter volume of credit at DEFER : ")       
    level_3=check("please Enter volume of credit at FAIL: ")

    if level_1 + level_2 + level_3 == 120:    
        if level_1==120:
            Progress=Progress+1
            print("Progress")
            list_1.extend([level_1,level_2,level_3])
        elif level_1==100:
            Trailer=Trailer+1
            print("progress(module trailer)")
            list_2.extend([level_1,level_2,level_3])
        elif level_1 + level_2 >= level_3 :
            Retriever=Retriever+1
            print("Do not progress-module retriever")
            list_3.extend([level_1,level_2,level_3])
        elif level_1 + level_2 < level_3 :
            Excluded=Excluded+1
            print("Exclude")
            list_4.extend([level_1,level_2,level_3])
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
        print("............................................................")              
        print("part2")
        lists(Progress,list_1,"progress - ")
        lists(Trailer,list_2,"Trailer - ")
        lists(Retriever,list_3,"Retriever - ")
        lists(Excluded,list_4,"Excluded - ")
        break
    
        
    
    
            
        

