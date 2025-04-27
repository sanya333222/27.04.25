x=30
y=30
g=50
f=25
def setup():
    size(700,500)
def draw():
    global x, y , g , f
    fill(255)
    background(87) 
    ellipse(200,350,g,20)
    ellipse(280,350,g,20)
    g=g+2
    push()
    translate(250,280)
    rotate(radians(30))
    fill(random(0,255), random(0,255), random(0,255))
    rect(0,0,5,70)
    pop()
    push()
    translate(260,270)
    rotate(radians(-15))
    fill(random(0,255), random(0,255), random(0,255))
    rect(0,0,5,75)
    pop()
    fill(255,255,0)
    rect(239,180,50,100)
    fill(255)

    ellipse(280,210,20,20)
    ellipse(250,210,20,20)
    fill(random(0,255), random(0,255), random(0,255))
    ellipse(250,210,10,10)
    ellipse(280,210,10,10)
    #push()
    #translate(240,220)
    #rotate(radians(100))
    #fill(0)
    push()
    translate(240,210)
    rotate(radians(90))
    rect(0,0,5,55)
    pop()
    rect(289,210,55,5)
    push()
    translate(340,210)
    rotate(radians(-30))
    rect(0,0,45,5)
    pop()
    rect(180,210,45,5)
    push()
    translate(180,210)
    rotate(radians(-135))
    rect(0,0,45,5)
    pop()
    fill(255)
    ellipse(380,180,f,25)
    ellipse(160,175,f,25)
    f=f+2
    fill(255,0,0)
    frameRate(2)
    rect(250,230,x,y)
    x=x-1
    y=y-1

    if x<=10 and y<=10:
        noLoop()
