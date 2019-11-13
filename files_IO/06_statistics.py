"""
statistics('story.txt')
{'lines': 172, 'words': 2145, 'characters': 11227}
"""


def statistics(file_name):
    with open(file_name) as file:
        data = file.read()
        file.seek(0)
        lines = file.readlines()

    results = dict()
    results['lines'] = len(lines)
    results['words'] = len(data.split())
    results['characters'] = len(data)
    return results


"""
udemy solution

def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }
"""
