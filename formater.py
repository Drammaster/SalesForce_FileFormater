#User inputs the name of their file
filename = input("Please enter the name of the file you wish to format:")
file_object = open(filename, "r")

new_file = open("formated.csv", "w+")

banned = [0, 1, 2, 3, 4, 5, 7]
counter = 0

#File gets processed into a dictionary
for i in file_object:
    if counter not in banned:
        split_line = i.split(",")
        if split_line[0] != 'Date':
            date_split = split_line[0].split("/")
            split_line[0] = date_split[2] + "/" + date_split[1] + "/" + date_split[0]
        split_line.remove(split_line[3])
        new_file.write(split_line[0] + "," + split_line[1] + "," + split_line[2] + "," + split_line[3] + "," + split_line[4] + "," + split_line[5])
    counter += 1

file_object.close()
new_file.close()
#User inputs the name of his/her new formated file
