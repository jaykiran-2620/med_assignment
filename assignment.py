print("Hello world")
b = "jay"
a = b.upper()
print(a)




#1

fruits = [
    ["jack", "apple"],
    ["orange", "kiwi"],
    ["dragon", "grape"],
]
print(fruits[2][0])



#2

coordinates = ((0, 1),(2, 3),(4, 5))
print(coordinates[2][1])



#3

students = [("Alice", 23), ("bob", 21)]
print(students[1][1])



#4

lists = ([10, 20], [30, 40])
print(lists[1][1])


#5

students = [{"name": "jay", "age": 23}, {"name": "john", "age": 24}, {"name": "alice", "age": 30}]
print(students[0]["name"])



#6 


 subject_marks={"math":[25,36,96],"science":[54,65,55],"english":[96,54,21]}
 print(subject_marks["math"][1])



#7


 user_profile={
     "alice":{
         "name":"alice",
         "age":25,
         "skill":"python",
         "language":"english"

     }
 }
 print(user_profile["alice"])



#8  



 billing_history=[
     {"name":"john","amount":250,"method":"cash","status":"paid"},
     {"name":"alice","amount":1230,"method":"cash","status":"pending"},
     {"name":"sunny","amount":654,"method":"upi","status":"paid"}
 ]
 print(billing_history[1]["status"])


#9 


 billing_history=(
     {"name":"john","amount":250,"method":"cash","status":"paid"},
     {"name":"alice","amount":1230,"method":"cash","status":"pending"},
     {"name":"sunny","amount":654,"method":"upi","status":"paid"}
 )
 print(billing_history[1]["amount"])


#10 


 data=[("hyderabad",40),("banglore",42),("chennai",45)]
 print(data[2][-1])


#11



 user_names={
     "john":[25,65,98],
     "don":[45,65,97],
     "sun":[57,32,21]
 }
 print(user_names['sun'][-1])


#12


 price=[
     {"product":"phone","price":12000},
     {"product":"laptop","price":40000}
 ]
 print(price[1]["product"])



#13


 marks=[
     ("maths",[65]),("science",[98]),("english",[54])
 ]
 print(marks[2][1][0])



#14


 task={
     "monday":("reading","sleeping"),"tuesday":("watching","playing"),"wednesday":("writing","swiming"),
     "thursday":("runing"),"friday":("walking"),"saturday":("gym","studying"),"sunday":("read","write")
 }
 print(task["monday"][0])


#15 


 data=[
     {"jay":{"maths":65,"english":54,"science":32}},
     {"john":{"math":31,"english":41,"science":78}}
 ]
 print(data[0]["jay"]["maths"])