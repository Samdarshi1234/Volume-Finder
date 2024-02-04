import os 
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def find_volume(name):
    name = name.lower()
    if(name=="cuboid"):
        l = int(input("Enter the length of the cuboid : "))
        b = int(input("Enter the breadth of the cuboid : "))
        h = int(input("Enter the height of the cuboid"))
        cr_volume = l*b*h
        print("The volume of the cuboid is : ", cr_volume)
    elif(name=="cube"):
        s = int(input("Enter the edge length of the cube : "))
        cs_volume = s**3
        print("The volume of the cube is : ", cs_volume)
    elif(name=="cylinder"):
        pi1 = 22/7
        r1 = int(input("Enter the radius of the cylinder : "))
        h1 = int(input("Enter the height of the cylinder : "))
        cy_volume = pi1*r1**2*h1
        rounded_cy_volume = round(cy_volume, 2)
        print("The volume of the cylinder is : ", rounded_cy_volume)
    elif(name=="cone"):
        pi2 = 22/7
        r2 = int(input("Enter the radius of the cone : "))
        h2 = int(input("Enter the altitudinal height of the cone : "))
        co_volume = 1/3 * r2**2 * pi2 * h2
        rounded_co_volume = round(co_volume, 2)
        print("The volume of the cone is : ", rounded_co_volume)
    elif(name=="sphere"):
        pi3 = 22/7
        r3 = int(input("Enter the radius of the sphere : "))
        sphere_volume = 4/3 * pi3 * r3**3
        rounded_sphere_volume = round(sphere_volume, 2)
        print("The volume of the sphere is : ",rounded_sphere_volume)
    else:
        print("Sorry ! This shape is not available.")
while True :
    print("Calculate Solid Shape Volume")
    shape_name = input("Enter the name of the shape : ")
    find_volume(shape_name)
    user_input = input("Do you want to continue ? Yes or no : ").lower()
    clear_terminal()
    if(user_input=="yes"):
        continue
    clear_terminal()
else:
    print("Exiting! Good Bye")