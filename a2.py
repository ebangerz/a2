# a2.py
from pathlib import Path
from Profile import Post
from ui import cd
# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Ethan Ngo
# ngoet4@uci.edu
# 34741355

def main():
    direc = " "
    words = " "

    while True:
        user_input = input()
        user_input_list = user_input.split()
        myPath = Path(cd.get_directory(user_input_list))

        if user_input[0] == 'L':
            if '-r' in user_input:
                if '-f' in user_input:
                    for x in cd.option_rextra(myPath):
                        if x.is_file():
                            print(x)
                elif '-s' in user_input:
                    for x in cd.option_rextra(myPath):
                        if user_input_list[-1] in x.name:
                            print(x)
                elif '-e' in user_input:
                    for x in cd.option_rextra(myPath):
                        if x.is_file() and f'.{user_input_list[-1].lower()}' == x.suffix.lower():
                            print(x)
                else:
                    cd.option_r(myPath)
            elif '-f' in user_input:
                cd.option_f(myPath)
            elif '-s' in user_input:
                cd.option_s(myPath, user_input_list[-1])
            elif '-e' in user_input:
                cd.option_e(myPath, user_input_list[-1])
            else:
                cd.L(myPath)

        elif user_input[0] == 'D':
            if myPath.suffix.lower() != ".dsu":
                print('ERROR')
            else:
                cd.delete(myPath)
        elif user_input[0] == 'R':
            if myPath.suffix.lower() != ".dsu":
                print('ERROR')
            else:
                cd.read(myPath)

        elif user_input[0] == 'C':
            fyepath = cd.create(myPath, user_input_list[-1])
            print(fyepath)
            user_profile = cd.create_p(fyepath)
            print(user_profile)
            direc = f'{myPath}/{user_input_list[-1]}.dsu'
        elif user_input[0] == 'O':
            if myPath.exists() and myPath.suffix.lower() == ".dsu":
                print("File loaded")
                words, direc = cd.command_open(myPath)
            else:
                file = cd.create(myPath, user_input_list[-1])
                print(file)
        elif user_input[0] == 'P':
            for inputs in range(len(user_input_list)):
                if user_input_list[inputs] == '-all':
                    print(words)
                elif user_input_list[inputs] == '-posts':
                    cd.command_p(direc, user_input_list[inputs])
                elif user_input_list[inputs] == '-usr':
                    cd.command_p(direc, user_input_list[inputs])
                elif user_input_list[inputs] == '-pwd':
                    cd.command_p(direc, user_input_list[inputs])
                elif user_input_list[inputs] == '-bio':
                    cd.command_p(direc, user_input_list[inputs])
                elif user_input_list[inputs] == '-post':
                    material = int(user_input_list[inputs + 1])
                    cd.command_p(direc, user_input_list[inputs], material)
                
                


        elif user_input[0] == 'E':
            for inputs in range(len(user_input_list)):
                if user_input_list[inputs] == '-usr':
                    material = cd.retrieve(user_input_list, user_input_list[inputs])
                    material = " ".join(material)
                    cd.command_e(direc, user_input_list[inputs], material)
                elif user_input_list[inputs] == '-pwd':
                    material = cd.retrieve(user_input_list, user_input_list[inputs])
                    material = " ".join(material)
                    cd.command_e(direc, user_input_list[inputs], material)
                elif user_input_list[inputs] == '-bio':
                    material = cd.retrieve(user_input_list, user_input_list[inputs])
                    material = " ".join(material)
                    cd.command_e(direc, user_input_list[inputs], material)
                elif user_input_list[inputs] == '-addpost':
                    material = cd.retrieve(user_input_list, user_input_list[inputs])
                    material = " ".join(material)
                    cd.command_e(direc, user_input_list[inputs], material)
                elif user_input_list[inputs] == '-delpost':
                    material = int(user_input_list[inputs + 1])
                    cd.command_e(direc, user_input_list[inputs], material)
                





        elif user_input[0] == 'Q':
            break

if __name__ == '__main__':
    main()