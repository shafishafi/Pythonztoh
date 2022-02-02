lottery = "Hello coders"
# 'h' or 'e' or 'l' or 'l' or ' o' or 'c' or 'd'

print(lottery[0])
print("Choose correct character of the word '",lottery,"'to win the lotery")
inputs = input(" ").lower()

if inputs == lottery[0] or inputs ==lottery[1] or inputs == lottery[4] or inputs == lottery[6] or inputs == lottery[8]:
 print("congratulation , you are a winner")
else:
 print("sorry, you didn't win a lottery , try next time")
