print('Hello, Django girls!')
if 3>2:
    print('It works!')
if 5>2:
    print('5 is indeed greater than 2')
else:
    ('5 is not greater than 2')
name ='Hannah'
if name =='Faye':
    print ('Hey Faye!')
elif name =='Hannah':
    print ('Hey Hannah!')
else:
    print ('Hey you!')
# change the volume
volume=57
if volume <20:
    print ('Its kinda quiet')
elif 20<= volume <40:
    print ('Its nice for background music')
elif 40<= volume <60:
    print ('Perfect, I can hear all the details')
elif 60<= volume <80:
    print ('Nice for parties')
elif 80<= volume <100:
    print ('A bit loud')
else:
    print ('My ears are hurting! :(')

#def hi(name):
#    if name =='Faye':
    #     print ('Hey Faye!')
    # elif name =='Hannah':
    #     print ('Hey Hannah!')
    # else:
    #     print ('Hey you!')

#hi('Fran')

# def hi (name):
#     print ('Hi' + name + '!')
#
# hi('Sheila')

def hi(name):
    print ('Hi ' +name+ '!')
girls =['Rachel','Sophie','Ola','Claire','Hannah','You']
for name in girls:
    hi(name)
    print('Next girl')
