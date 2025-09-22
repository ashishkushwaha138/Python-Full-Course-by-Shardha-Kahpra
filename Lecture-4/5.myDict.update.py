student = {
    "name" :"ashish",
    "subjects" : "python",
    "marks" : 93.3
    
}
print(student)
print(type(student))
new_dict ={"city" : "Delhi"}
student.update(new_dict)  #alternate student.update({"city" : "Delhi"})
print(student)