import random

a = []
urn = []

class box:
  def __init__(self,num=0, left = None, right = None):
    self.num = num
    self.ball_count = 0
    self.right = right
    self.left = left
  def donate_ball(self):
    self.right.ball_count += 1
    self.left.ball_count += 1

def initiate():
  a.append(box(num = 1))
  for i in range(1,10):
    a.append(box(num=i+1, left = a[i-1]))
    a[i-1].right = a[i]
  a[0].left = a[9]
  a[9].right = a[0]
  for i in range(10):
    urn.append([])

def distribute():
  for i in range(100):
    a[random.randrange(0,10)].donate_ball()

def reset():
  for i in range(10):
    a[i].ball_count = 0

def cov(x,y):
  mean_x = sum(x) / len(x)
  mean_y = sum(y) / len(y)

  c = sum((a - mean_x) * (b - mean_y) for (a,b) in zip(x,y)) / len(x)
  return c
  

def mainloop():
  initiate()
  for i in range(1000):
    distribute()
    for i in range(10):
      urn[i].append(a[i].ball_count)
    reset()

mainloop()
m = []
for i in range(10):
  print("\n")
  for j in range(10):
    print(cov(urn[i],urn[j]),end="")
    print("  ")
#print(urn)
