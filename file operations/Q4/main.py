import grading
import csv

stud_count=0

li=[]

topper=""
top_avg=0

p_cnt=0
f_cnt=0

with open(r"C:\Users\daler\Desktop\Projects\DaleLuis Persistent training\file operations\Q4\students.csv", "r") as f:
    reader =csv.DictReader(f)
    # for row in reader:
    #     print(row)
      
    for row in reader:
        no=int(row["roll_no"])
        name=row["name"]
        sub1=int(row["maths"])
        sub2=int(row["physics"])
        sub3=int(row["chemistry"])
        
        stud_count+=1
        
        t1=sub1+sub2+sub3
        avg=round(t1/3,2)
        grade=grading.grade(avg)
        di={"roll_no": no, "name":name,"maths":sub1,"physics":sub2,"chemistry":sub3,"total":t1,"average":avg,"grade":grade}
        li.append(di)
        

    for i in li:
        if top_avg<i['average']:
            top_avg=i['average']
            topper=i['name']
            
        if i['grade'] == 'F':
            f_cnt+=1
        else:
            p_cnt+=1
    
print(f"Processed {stud_count} students --> students_result.csv")
print(f"Class Topper : {topper} (avg {top_avg})")
print(f"Passed : {p_cnt} | Failed : {f_cnt}")

fields=["roll_no", "name","maths","physics","chemistry","total","average","grade"]

with open(r"C:\Users\daler\Desktop\Projects\DaleLuis Persistent training\file operations\Q4\students_result.csv", "w",newline="") as f:
    writer = csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    writer.writerows(li)
        
    