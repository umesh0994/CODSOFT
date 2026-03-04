import os
from datetime import datetime

F = "tasks.txt"
R, G, Y, C, X = "\033[91m", "\033[92m", "\033[93m", "\033[96m", "\033[0m"

def load():
    if not os.path.exists(F): return []
    with open(F) as f:
        return [line.strip().split("|") for line in f if line.strip()]

def save(t):
    with open(F, "w") as f:
        for i in t: f.write("|".join(i) + "\n")

def show(t):
    if not t: print("No tasks\n"); return
    for i, v in enumerate(t, 1):
        name, status, due, pr = v
        col = R if pr=="High" else Y if pr=="Medium" else G
        sym = G+"✓" if status=="Done" else R+"✗"
        print(f"{i}. {name} [{sym}{X}] Due:{due} Priority:{col}{pr}{X}")
    print()

def main():
    t = load()
    while True:
        print(C+"1.View 2.Add 3.Done 4.Delete 5.Sort 6.Exit"+X)
        c = input("Choose: ")

        if c=="1": show(t)

        elif c=="2":
            name = input("Task: ")
            due = input("Due (DD-MM-YYYY): ")
            pr = input("Priority (High/Medium/Low): ").capitalize()
            t.append([name,"Pending",due,pr])
            save(t)

        elif c=="3":
            show(t)
            try: t[int(input("No: "))-1][1]="Done"; save(t)
            except: print(R+"Invalid\n"+X)

        elif c=="4":
            show(t)
            try: t.pop(int(input("No: "))-1); save(t)
            except: print(R+"Invalid\n"+X)

        elif c=="5":
            try:
                t.sort(key=lambda x: datetime.strptime(x[2], "%d-%m-%Y"))
                print(Y+"Sorted!\n"+X)
            except: print(R+"Date format error\n"+X)

        elif c=="6": break
        else: print(R+"Invalid choice\n"+X)

if __name__=="__main__":
    main()
