from flask import Flask

app = Flask(__name__)

b = []

def init():
  global b
  b = [['-','-','-'],['-','-','-'],['-','-','-']]

init()
 

def rb(b):
  out= ""
  for i in b:
    for j in i:
      out+=j
    out+="\n"
  return out

@app.route("/")
def root():
  return rb(b)

@app.route("/<player>/<x>/<y>")
def boardz(player,x,y):
  try:
    if len(player) != 1: 
      return "Bad exploit is bad."
    b[int(x)][int(y)] = player
    return rb(b)
  except:
    return "Bad exploit is bad."

@app.route("/cb")
def cb():
  global b
  b = [['-','-','-'],['-','-','-'],['-','-','-']]
  return rb(b)


app.run(port=1759,debug=True);
