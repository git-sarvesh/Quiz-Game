print('welcome to my computer quiz!')

playing=input('do you want to play?    ')

if playing !='yes':
    quit()
print("okey! let's play:) ")
score=0
answer=input('does a computer needs core?     ')
if answer==('yes'):
   print('correct:)')
   score+=1
else:
    print('incorect')

answer=input('how many sences do hmans have?     ')
if answer==('six'):
   
   print('correct:)')
   score+=1

else:

    print('incorect')
answer=input('when was computer invented?     ')
if answer==('2400BCE'):
   
   print('correct:)')
   score+=1

else:

    print('incorect')
    
answer=input('do you like bicks?   ')
if answer==('yes'):
   
   print('correct:)')
   score+=1

else:
    print('incorect')


print('you got  ' + str(score) + 'questions correct')
print('you got  ' + str((score/4)*100) + '%')