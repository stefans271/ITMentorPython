from methods import load_file, save_file

data=load_file("data/user.json")
print(data)
save_file("data/user.json",data)
data.append({"name":"test test"})
save_file("data/user.json",data)

#w-write
#with open("data/user.json","w")as file:
    #json.dump(data,file, indent=4)
