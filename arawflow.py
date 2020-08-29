import sys

def cont():
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass

def outro():
    print('\nBlog post is now live! Visit arawseekers.github.io\n')
    sys.exit()


def proc6():
    print('\nIn Terminal:')
    print('\t- press Ctrl + c (This will stop site rendering. Also makes the terminal usable again.)')
    print('\t- enter \'hugo\' (This creates the website files and puts them all in the folder docs/ )')
    print(
        '\t- enter \'arawpush\' (This command pushes the website files to the GitHub server that currently hosts our '
        'blog.)')
    print('\nNOTE: The terminal may prompt you to ask for username & password. Refer to Bitwarden for credentials.\n')
    cont()
    outro()


def decision3():
    done = str(input('Done? (y/n) '))
    if done == 'y':
        proc6()
    elif done == 'n':
        decision1()
    else:
        print('Pls. answer only with y or n')
        decision3()

def proc5():
    print('\nIn browser URL bar:')
    print('\tenter \'localhost:1313\'\nThis is the blog\'s preview. View changes here as you edit the post in Atom.\n')
    cont()
    decision3()


def proc4():
    print('\nIn Terminal:')
    print('\tenter \'hugo server\'\n')
    print('NOTE: \'hugo server\' command renders the site for preview in browser. As long as this is running in the '
          'terminal, changes made (and saved) in Atom are reflected instantly in the preview.\n')
    cont()
    proc5()


def proc3():
    print('\nOpen xyz.md in Atom and edit entry as you wish.')
    print('NOTE: Blog posts are in the folder \'content/posts/\'\n')
    cont()
    proc4()


def proc2():
    print('\nIn Terminal:')
    print('\tenter \'hugo new content/posts/xyz.md\'\n')
    print('NOTE: \'hugo new\' will create a blank blog post in the folder \'content/posts\' with the title \'xyz\'. '
          'Make sure to keep the \'.md\' file extension.\n')
    cont()
    proc3()


def decision2():
    edit_post = str(input('Edit existing post? (y/n) '))
    if edit_post == 'y':
        proc3()
    elif edit_post == 'n':
        print('Done for today!')
        sys.exit()
    else:
        print('Pls. answer only with y or n')
        decision2()


def decision1():
    new_post = input('New blog post? (y/n) ')
    if new_post == 'y':
        proc2()
    elif new_post == 'n':
        decision2()
    else:
        print('Pls. answer only with y or n')
        decision1()

def proc1():
    print('\nIn Terminal:')
    print('\tenter \'arawseekers\'\n')
    print('NOTE: The \'arawseekers\' command will get you this folder:\n\t isyaferrer/Sites/arawseekers/\n')
    cont()
    decision1()


def intro():
    print("Hi Isya!\nThis program will guide you to posting at our Araw Seekers blog.")
    print('To start, open the ff. programs:\n\tTerminal\n\tAtom (or any text editor)\n\tFirefox (or any browser)\n')
    cont()
    proc1()

intro()
