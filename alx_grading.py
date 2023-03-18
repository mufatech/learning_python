print("Welcome to ALX Grading System")
username = input("Enter your name: \n")
score1 = int(input("Enter your scores for the month 1: \n"))
score2 = int(input("Enter your scores for the month 2: \n"))
score3 = int(input("Enter your scores for the month 3: \n"))
sum = (score1 + score2 + score3)
print("The sum is ", sum)
average = int(sum/3)
print("The average is ", average)
avg_scores = int(input("Enter your average scores: \n"))
if avg_scores > 1 and avg_scores < 50:
  print("Very poor, Go back home and learn how to cook")
elif avg_scores > 51 and avg_scores < 79:
  print("You are a failure you can never make it in ALX")
elif avg_scores > 80 and avg_scores < 120:
  print("You are doing well keep it up")
elif avg_scores > 121 and avg_scores < 175:
  reply = input("I hope you are not copying from github?, Yes or No: \n"
                )  #reply = input("Yes or No \n")
  if reply == 'Yes':
    print("Repent and learn")
    if reply == 'No':
      print("You are doing well")
elif avg_scores > 176 and avg_scores < 200:
  print("ALX is coming to investigate you")
