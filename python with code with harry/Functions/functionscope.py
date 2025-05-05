def sum(a,b):
    global gl_vr
    gl_vr=0
    return (a+b)
print(sum(4,5))

gl_vr=10
print(gl_vr)


def studentInfo(name,age):
    """This method will return information of student"""
    return f"Name : {name}, Age : {age}"
print(studentInfo.__doc__)

print(len.__doc__)