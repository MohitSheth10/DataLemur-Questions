def min_attendees(answers):
  total=0
  newanswers=sorted(set(answers))
  for value in newanswers:
    no1=answers.count(value)       # how many people gave this answer
    group_size=value+1             # each person with this answer is in a group of value+1 people
    groups=no1//group_size
    if no1%group_size!=0:
      groups=groups+1              # a partly filled group still counts as a full group
    total=total+groups*group_size
  return total
answers=[2, 1, 1]
#Test cases:
#[2, 1, 1] Expected 5
#[0, 0, 1] Expected 4
#[4, 4, 3, 3, 4, 1] Expected 11
print(min_attendees(answers))
