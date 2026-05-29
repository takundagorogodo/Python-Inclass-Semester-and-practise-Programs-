student_data ={
      "Ram":{"rollno":30,"age":30,"course":"python","dept":"cse"}
      ,"Mohan":{"rollno":89,"age":323,"course":"java","dept":"eee"}
}

print(student_data)
print(student_data["Mohan"])
print(student_data["Mohan"]["rollno"])

student_data["Mohan"]["phone_no"] = 2345
print(student_data["Mohan"])
#del print(student_data["Mohan"]["phone_no"])
print(student_data["Mohan"].pop("phone_no"))
print(student_data["Mohan"])

travell_data = {
      "Harare":["mbare" ,"chitungwiza","dzivarasekwa","madokero","borrowdale"],
      "Mutare":["hobhouse" ,"penhalonga","florida","dangamvura","Chikanga"]
} 

print(travell_data)
print(travell_data["Mutare"])

student_data =[
      {
            "Name":"tapiwa",
            "rollno":30,
            "age":30,
            "course":["c++","python"]
            
      }
      ,{
            "Name":"moses",
             "rollno":89,
             "age":323,
             "course":"java"
             
      }
]

def add_new_student(name,rollno,age,course_opted):
      new_student = {}
      new_student["Name"] = name
      new_student["rollno"] = rollno
      new_student["age"] = age
      new_student["course"] = course_opted
      student_data.append(new_student)

add_new_student("Shyam",22,17,"C++")
add_new_student("ashbell",25,19,"physics")
print(student_data)
print(student_data[1])