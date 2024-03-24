#Author name: Ishini S. Ranasinghe
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:20221153
# Date: 10 December 2022
text_file = open("Ishini's Data.txt","a")

list_1=[]
list_2=[]
list_3=[]
list_4=[]

Progress=0
Trailer=0
Retriever=0
Excluded=0

range_of_marks =[0,20,40,60,80,100,120]

def check(prompt):
    while True :        
        try:
            level =int(input(prompt))
            if level not in range_of_marks:
                print("Out of range")
                continue
            break
        
        except ValueError:
            print("integer required")
            continue

    return level

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
        while True:
            if Progress >= 1:
                print("progress - ",end="")
                print(','.join(map(str,list_1[0:3]))) #https://www.entechin.com/how-to-print-a-list-without-square-brackets-in-python/
                file_print="%s-%d,%d,%d"%("Progress",list_1[0],list_1[1],list_1[2])
                text_file.write(f"{file_print}\n")
                del (list_1[0:3])
                Progress=Progress-1
                continue
            
            else:
                break
            
        while True:
            if Trailer >= 1:
                print("Trailer - ",end="")
                print(','.join(map(str,list_2[0:3])))
                file_print="%s-%d,%d,%d"%("Trailer",list_2[0],list_2[1],list_2[2])
                text_file.write(f"{file_print}\n")
                del (list_2[0:3])
                Trailer=Trailer -1
                continue
            
            else:
                break
            
        while True:
            if Retriever >= 1:
                print("Retriever - ",end="")
                print(','.join(map(str,list_3[0:3])))
                file_print="%s-%d,%d,%d"%("Retriever",list_3[0],list_3[1],list_3[2])
                text_file.write(f"{file_print}\n")
                del (list_3[0:3])
                Retriever=Retriever -1
                continue
            
            else:
                break
            
        while True:
            if Excluded >= 1:
                print("Excluded - ",end="")
                print(','.join(map(str,list_4[0:3])))
                file_print="%s-%d,%d,%d"%("Excluded",list_4[0],list_4[1],list_4[2])
                text_file.write(f"{file_print}\n")
                del (list_4[0:3])
                Excluded=Excluded -1
                continue
            else:
                break

        break
text_file.close()
    
    
            
        

