# Template for Processing sketches.
x=350
y=690
value=0
y2=y-80
y3=y-160
y4=y-240
y5=y-320
y6=y-400
y7=y-480
y8=y-560
y9=y-640
y10=y-720
speed=PVector(5,5)


def setup():
    size(700,700)

def draw():
    background(155)
    global value
    global x
    global y
    global y2
    global y3
    global y4
    global y5
    global y6
    global y7
    global y8
    global y9
    global y10
    global speed
    fill(value)
    triangle(x-20,y,x,y-40,x+20,y)
    print keyCode
    
    y2-=speed.y
    fill(255)
    rect(x-15,y2,7,35) 
    rect(x+8,y2,7,35)
    
    y3-=speed.y
    rect(x-15,y3,7,35) 
    rect(x+8,y3,7,35)
    
    y4-=speed.y
    rect(x-15,y4,7,35) 
    rect(x+8,y4,7,35)
    
    y5-=speed.y
    rect(x-15,y5,7,35) 
    rect(x+8,y5,7,35)
    
    y6-=speed.y
    rect(x-15,y6,7,35) 
    rect(x+8,y6,7,35)
    
    y7-=speed.y
    rect(x-15,y7,7,35) 
    rect(x+8,y7,7,35)
    
    y8-=speed.y
    rect(x-15,y8,7,35) 
    rect(x+8,y8,7,35)
    
    y9-=speed.y
    rect(x-15,y9,7,35) 
    rect(x+8,y9,7,35)
    
    y10-=speed.y
    rect(x-15,y10,7,35) 
    rect(x+8,y10,7,35)
    
    if y2<= 0:
        y2=y-80
    if y3 <= 0:
        y3=y-80
    if y4 <= 0:
        y4=y-80
    if y5 <= 0:
        y5=y-80
    if y6 <= 0:
        y6=y-80
    if y7 <= 0:
        y7=y-80
    if y8 <= 0:
        y8=y-80  
    if y9 <= 0:
        y9=y-80   
    if y10 <= 0:
        y10=y-80  
    
    if keyPressed is True and keyCode == 37:
        x-=3
        
    if keyPressed is True and keyCode == 39:
        x+=3

    if keyPressed is True and keyCode == 40:
        y+=3
        
    if keyPressed is True and keyCode == 38:
        y-=3 
    

           
