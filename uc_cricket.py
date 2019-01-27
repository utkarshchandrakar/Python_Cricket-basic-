no_of_over = int(input("enter no. of overs: "))
for overs in range(0, no_of_over):

    if overs==no_of_over :
         break
    print("Enter runs for over ", overs+1)
    print("---------------------------")

    BALLS_IN_OVER = 6
    totalBallsFaced=0
    total=0
    wicket=0

    for _runs in range(1, BALLS_IN_OVER):


      totalBallsFaced += 1
      totalOversFaced = (totalBallsFaced // BALLS_IN_OVER)
      partOverFaced = (totalBallsFaced % BALLS_IN_OVER)

      
      runs = int(input("> "))
      if runs>0 and runs<=6:
       total += runs

      if runs == 0:
        wicket += 1
        print("Batter out...")

      elif runs > 6:
            print("it's not possible")
            break

    if wicket >= 10:
          print("Batters all out")
          endGame = 1
          break


print("\n")
print("total score is:")
print(total)
print("total wicket is:")
print(wicket)