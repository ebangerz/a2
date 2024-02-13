# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Ethan Ngo
# ngoet4@uci.edu
# 34741355

from pathlib import Path
from Profile import Profile
from Profile import Post

RECURSIVE = []
class cd:
    def __init__(self) -> None:
        pass
    


    def command_open(directory):
        p = Path(directory)
        with open(p, 'r') as file:
            file_words = file.read()
        return file_words, p

    def command_e(directory, input = str, content = str):
        path = Path(directory)
        x = Profile()
        y = Post()
        x.load_profile(str(path))
        
        if input == '-usr':
            x.username = content
        elif input == '-pwd':
            x.password = content
        elif input == '-bio':
            x.bio = content
        elif input == '-addpost':
            y.set_entry(content)
            y.timestamp = Post.get_time(y)
            x.add_post(y)
        elif input == '-delpost':
            x.del_post(int(content))
        x.save_profile(path)
        
    def command_p(directory, input = str, id = None):
        path = Path(directory)
        x = Profile()
        x.load_profile(str(path))

        if input == '-posts':
            print(x.get_posts())
        elif input == '-usr':
            print(x.username)
        elif input == '-pwd':
            print(x.password)
        elif input == '-bio':
            print(x.bio)
        elif input == '-post':
            posts = list(x.get_posts())
            for i in range(len(posts)):
                if i == id:
                    print(posts[i])
    def read(directory):
        p = Path(directory)
        if p.exists() and p.stat().st_size == 0:
            print('EMPTY')
        else:
            try:
                with open(p, 'r') as file:
                    content = file.read()
                    print(content)
            except FileExistsError:
                print("File not found.")
            except:
                print('ERROR')

    def L(directory):
        for current in directory.iterdir():
            if current.is_file():
                print(current)
            elif current.is_dir():
                print(current)

    def option_rextra(directory):
        for current in directory.iterdir():
            RECURSIVE.append(current)
            if current.is_dir():
                cd.option_rextra(current)
        return RECURSIVE


    def option_r(directory):
        for current in directory.iterdir():
            print(current)
            if current.is_dir():
                cd.option_r(current)

    def option_f(directory):
        for current in directory.iterdir():
            if current.is_file():
                print(current)


    def option_s(directory, name):
        for current in directory.iterdir():
            if current.is_file() and name == current.name:
                print(current)

    def option_e(directory, extension):
        for current in directory.iterdir():
            if current.is_file() and (current.suffix.lower() == f'.{extension.lower()}'):
                print(current)
            if current.is_dir():
                cd.option_e(current, extension)

    def delete(directory):
        p = Path(directory)
        if p.exists():
            p.unlink()
            print(f'{p} DELETED')
        else:
            print('ERROR')


    def create(directory, name):
        p = Path(directory)
        file_path = p / f'{name}.dsu'
        file_path.touch()
        return file_path

    
    def get_directory(input):
        directory = []

        for x in range(len(input)):
            if input[x][0] == '-':
                break
            else:
                try:
                    directory.append(input[x+1])
                except IndexError:
                    break
        if directory[-1][0] == '-':
            directory.pop()
        path = " ".join(directory)
        return path
    
    def create_p(directory):
        file_path = Path(directory)
        usr = input("Enter your username: ")
        passw = input("Enter your password: ")
        bio = input("Enter a bio (optional): ")
        profile = Profile(dsuserver = None, username = usr, password = passw)
        profile.bio = bio
        profile.save_profile(file_path)


    def retrieve(user_list: list, command: str):
        contents = []
        c_index = user_list.index(command)

        for words in range(c_index + 1, len(user_list)):
            if user_list[words][-1] == '"':
                contents.append(user_list[words])
                break
            elif user_list[words].find('"') > -1:
                contents.append(user_list[words])
            else:
                contents.append(user_list[words])
        return contents


        

