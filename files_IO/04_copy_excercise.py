"""
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
"""


def copy(*args):
    with open(args[0]) as old_file:
        data = old_file.read()
        with open(args[1], "w") as new_file:
            new_file.write(data)


"""
udemy solution

def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)

"""
