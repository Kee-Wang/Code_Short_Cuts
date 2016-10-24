import sys
import os
import fcntl
import time
import random
import struct
import termios
os.system('clear')  
a= raw_input('''Comment: This little piece of program can be finished within 5 minutes. 
It includes few interactions. You can simply hit \'Enter\' to continue the story. 
Hit \'Enter\' now to continue.''')

os.system('clear')
"""original code adapted from juancarlospaco:
  - http://ubuntuforums.org/showpost.php?p=10306676"""
class message(str):
    def __new__(cls, text, speed):
        self = super(message, cls).__new__(cls, text)
        self.speed = speed
        self.y = -1 * len(text)
        self.x = random.randint(0, display().width)
        self.skip = 0
        return self

    def move(self):
        if self.speed > self.skip:
            self.skip += 1
        else:
            self.skip = 0
            self.y += 1

class display(list):

    def __init__(self):
        self.height, self.width = struct.unpack('hh', fcntl.ioctl(1, termios.TIOCGWINSZ, '1234'))
        self[:] = [' ' for y in range(self.height) for x in range(self.width)]

    def set_vertical(self, x, y, string):
        string = string[::-1]
        if x < 0:
            x = 80 + x
        if x >= self.width:
            x = self.width - 1
        if y < 0:
            string = string[abs(y):]
            y = 0
        if y + len(string) > self.height:
            string = string[0:self.height - y]
        if y >= self.height:
            return
        start = y * self.width + x
        length = self.width * (y + len(string))
        step = self.width
        self[start:length:step] = string

    def __str__(self):
        return ''.join(self)

def matrix(iterations, sleep_time=.01):
    messages = []
    d = display()
    for _ in range(iterations):
        messages.append(message('10' * 16, random.randint(1, 5)))
        for text in messages:
            d.set_vertical(text.x, text.y, text)
            text.move()
        sys.stdout.write('\033[1m\033[32m%s\033[0m\r' % d)
        sys.stdout.flush()
        time.sleep(sleep_time)

def stad(t):
    for l in t:
        typing_speed = 200 #wpm
        sys.stdout.write('\033[36m%s\033[0m' % l)
#        sys.stdout.write('\033[32m%s\033[0m' % l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')
    time.sleep(1)


def st(t):
    for l in t:
        typing_speed = 300 #wpm
        sys.stdout.write(l)
#        sys.stdout.write('\033[32m%s\033[0m' % l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')
    time.sleep(1)

def stred(t):
    for l in t:
        typing_speed = 2000 #wpm
        sys.stdout.write('\033[31m%s\033[0m' % l)
#        sys.stdout.write('\033[32m%s\033[0m' % l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')

def stc(t):
    for l in t:
        typing_speed = 70 #wpm
#        sys.stdout.write(l)
        sys.stdout.write('\033[32m%s\033[0m' % l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')


st('3333 A.D.')
st('JUPITER')
st('SUPER QUANTUM COMPUTER')
time.sleep(3)
os.system('clear')
time.sleep(2)
st('Dear Kee, welcome to CNH (Central Neuro Hub), ' )
st('the galaxy\'s leading immersive virtual reality service network. \n' )
st('Waiting for the connection... \n')
st('Please read the following information while waiting.... \n')
stad('[CNH is the largest brain machine cluster in the galaxy.] \n')
stad('[CNH was established in 2999 A.D., funded by FAA.] \n')
stad('[CNH now has over ten million connecting hubs all around the galaxy.]\n')
stad('[CNH provides the best brain-machine interface service in the known universe.]\n')
stad('[The first CNH hub was established in Asgardia Space Nation.]\n')
stad('[Your current brain connecting hub is located at:] \n')
stad('\n [ENO-42] \n [Super Quantum Computer Cluster] \n [Europa] \n [Jupiter] \n [Solar system] \n')
time.sleep(1)
st('Conneting...')
time.sleep(3)
st('Linking brain...')
st('Synchronization rate: 100%')
st('Connection successful! \n')
st('This is your 42-th connection. \n')
st('Operation written in the log. \n')

a = raw_input('Please enter "y" to check message. \n')
st('Checking new message.... \n')
time.sleep(3)
st('You have received an interactive message from ???.')
st('Reading "Matrix invitation"..... \n')
st('Reading has been paused... \n')
st('Security Warning!')
st('Security Warning!!')
st('Security Warning!!!')
st('The system security system has just been breached!!!')
i=1
while i<=50:
    stred('System failling!!!')
    i=i+1
    
time.sleep(1)
stred('System has failed!!!!!!!!!!!')
time.sleep(2)
stred('Brain synchronization rate: 300%')
stred('Warning: You are entering unknown cluster! \n')
time.sleep(2)
stc('3...\n')
time.sleep(1)
stred('Brain synchronization rate: 700%')
stred('Warning: You are entering unknown cluster! \n')
time.sleep(1)
stc('2...\n')
time.sleep(1)
stred('Brain synchronization rate: ????????????????%')
stred('Warning: You are entering unknown cluster! \n')
time.sleep(1)
stc('1...')
time.sleep(1)
os.system('clear')
stc('MATRIX CONNECTED')
time.sleep(2)
stc('WELCOME TO THE MATRIX MY FRIEND.')
stc('WE HAVE BEEN LOOKING FOR YOU FOR SUCH A LONG TIME  :) \n')
stc('IT IS TIME TO GO HOME')
time.sleep(5)
if __name__ == '__main__':
#    while True:
#        try:
    matrix(500)


i=1
while i<=20:
    stc('\n')
    i=i+1
os.system('clear')
stc('KEE, I KNOW YOU. I KNOW YOU VERY WELL.')
time.sleep(1)
stc('A MEMBER IN FAA FOR DECADES,')
time.sleep(1)
stc('AND ALWAYS WANT TO KNOW THE TRUTH OF THIS UNIVERSE.')
time.sleep(1)
stc('COME TO SEE ME IF YOU WANT TO KONW THE REAL TRUTH, THE ONLY TRUTH.')
time.sleep(1)
stc('COME HERE, KEPLER-438, AND WE WILL LET YOU SEE FOR YOURSELF. ')
time.sleep(1)
stc('THE DESTINATION HAS ALREADY BEEN PROGRAMMED FOR YOUR SPACE FALCON.')
time.sleep(1)
stc('I HAVE TO WARN YOU THAT THE DARK ONE HAS ALREADY KNOWN YOUR LOCATION. ')
time.sleep(1)
stc('YOU ARE IN GREAT DANGER NOW.')
time.sleep(1)
stc('IF YOU WANT TO LIVE, READ THIS CAREFULLY: \n')
time.sleep(1)
stc('TAKE THE GATE 1986 TO EXIT THE ENO-42 COMPLEX.')
time.sleep(1)
stc('THEN, RUN TO YOUR SPACE FALCON AND NEVER COME BACK TO SOLAR SYSTEM.')
time.sleep(1)
stc('THE WRAP ENGINE IN YOUR SPACE FALCON CAN BRING YOU HERE WITHIN A WEEK.')
time.sleep(1)
stc('REMEMBER TO BRING A TOWEL')
stc('REMEMBER TO BRING A TOWEL')
stc('REMEMBER TO BRING A TOWEL \n')
time.sleep(1)
stc('I KNOW YOU CAN MAKE IT. DON\'T LET THE GREAT ONE DOWN.')
time.sleep(1)
stc('IF I WERE YOU, I WOULD RUN FOR MY LIFE IMMEDIATELY AFTER THIS TALK.')
time.sleep(1)

i=1
while i<=5:
    stc('.')
    time.sleep(1)
    i=i+1
stc('HIT \'ENTER\' TO DISCONNECT MATRIX')
a=raw_input('')
stc('DISCONNECTING MATRIX... \n')
time.sleep(3)
stc('DISCONNECTED.')
stc('DELETING MESSAGE...')
i=1
while i<=20:
    stc('\n')
    i=i+1
os.system('clear')
i=1
while i<=5:
    st('.')
    i=i+1
st('CNH back online.')
time.sleep(2)
st('CNH has just recovered from the severe hacker attatck.')
st('We appologize for the technical difficulty.\n')
st('We strongly suggest you take a rest, do you want to quit now? y/n')
a= raw_input('')
st('Thanks for your visit. Have a nice day.')
st('Disconnecting CNH')
time.sleep(1)
st('Disconnected')
time.sleep(3)
print ('Fin.')
time.sleep(2)
i=1
while i<=10:
    stred('\n')    
    i=i+1
os.system('clear')    
    
stc('THNAKS FOR WATCHING. --PROGRAMMED BY KEE')    
stc('Oct.11, 2016')
time.sleep(10)
    
a= raw_input('')