
lib_records={"sarthak":3,
         "rohan":2,
         "ashish":6,
         "saisha":0,
         "sahil":3,
         "prasad":10,
         "ajinkya":0
         }

def compute_average(records):
    total=sum(records.values())
    length=len(records)
    average=total/length
    print("Average= ",average,"\n")

def max_min(records): 
    non_zero=[]
    for val in records.values():
        if val>0:
            non_zero.append(val)
    maxim=max(non_zero)
    minim=min(non_zero)
    print("Maximum=",maxim," Minimum=",minim,"\n")

def count_zero_borrower(records):
    x=list(records.values()).count(0)
    print(x," People have borrowed zero books\n")

def most_frequent(records):
    from collections import Counter
    non_zero_vals=[val for val in records.values() if val>0]
    freq=Counter(non_zero_vals)  
    common=freq.most_common(1)[0][0]
    print("Mostly People buy ",common," books")



def menu():
    print("1.Average")
    print("2.Maximum and Minimum")
    print("3.Zero borrowed")
    print("4.Most Common")
    choice=int(input("Enter choice (1,2,3,4) for the operation to perform: "))
    print()
    if choice==1:
        compute_average(lib_records)
    elif choice==2:
        max_min(lib_records)
    elif choice==3:
        count_zero_borrower(lib_records) 
    elif choice==4:
        most_frequent(lib_records)     
    else:
        print("Invalid Input")
        
while True:
    menu()   
    exit=input("Do you want to exit program (yes/no): ").lower()
    if exit=="yes":
        break              
