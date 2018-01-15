    
    




x=350
x2=x3=x4=x5=x6=x7=x8=x9=x10=348.5
score=0
energy=40



value=0



y2=610

y=690
y3=y2-80
y4=y2-160
y5=y2-240
y6=y2-320
y7=y2-400
y8=y2-480
y9=y2-560
y10=y-640

speed=PVector(5,5)
speed1=PVector((random(1,5)),(random(3,6.5)))
speed2=PVector((random(1,5)),(random(1,5)))
ball=PVector((random(30,670)),20)
bigenemy=PVector((random(40,650)),20)

def setup():
    size(700,700)

def draw():
    background(155)
    global value
    global x
    global x2
    global x3
    global x4
    global x5
    global x6
    global x7
    global x8
    global x9
    global x10

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
    global speed1
    global ball
    global score
    global energy
    global bigenemy
    fill(value)
    rect(x-15,y-40,30,30)
    print keyCode
    
    #draw the bullets
    y2-=speed.y
    fill(255)
    rect(x2,y2,3,35) 
   
    
    y3-=speed.y
    rect(x3,y3,3,35) 
    
    
    y4-=speed.y
    rect(x4,y4,3,35) 

    y5-=speed.y
    rect(x5,y5,3,35) 

    y6-=speed.y
    rect(x6,y6,3,35) 
    
    y7-=speed.y
    rect(x7,y7,3,35) 
    
    y8-=speed.y
    rect(x8,y8,3,35) 
    
    y9-=speed.y
    rect(x9,y9,3,35) 
    
    y10-=speed.y
    rect(x10,y10,3,35) 

    #the rule of bullets, if they get out of the screen, it will disappear and go back to the original point.
    if y2<= 0:
        y2=y-80
        x2=x-1.5
    if y3 <= 0:
        y3=y-80
        x3=x-1.5
    if y4 <= 0:
        y4=y-80
        x4=x-1.5
    if y5 <= 0:
        y5=y-80
        x5=x-1.5
    if y6 <= 0:
        y6=y-80
        x6=x-1.5
    if y7 <= 0:
        y7=y-80
        x7=x-1.5
    if y8 <= 0:
        y8=y-80  
        x8=x-1.5
    if y9 <= 0:
        y9=y-80   
        x9=x-1.5
    if y10 <= 0:
        y10=y-80  
        x10=x-1.5
    
   
    #your plane's movement.
    if keyPressed is True and keyCode == 37:
        x-=3
        
    if keyPressed is True and keyCode == 39:
        x+=3

   
    #draw the enemy and the movement of ememy annd bigenemy
    fill(128)  
    ellipse(ball.x,ball.y,30,30)
    ball.y+=speed1.y
    fill(0,256,0)
    rect(bigenemy.x,bigenemy.y,120,60)
    bigenemy.y+=speed1.x
    textSize(20)

    text(energy,bigenemy.x+40,bigenemy.y+75)
    
    
    #distance of each bullets to the enemy          
    a=x2-ball.x
    a2=x3-ball.x
    a3=x4-ball.x
    a4=x5-ball.x
    a5=x6-ball.x
    a6=x7-ball.x
    a7=x8-ball.x
    a8=x9-ball.x
    a9=x10-ball.x
    b=y2-ball.y
    b2=y3-ball.y
    b3=y4-ball.y
    b4=y5-ball.y
    b5=y6-ball.y
    b6=y7-ball.y
    b7=y8-ball.y
    b8=y9-ball.y
    b9=y10-ball.y
    distance= sqrt(a**2 + b**2)
    distance1= sqrt(a2**2 + b2**2)
    distance2= sqrt(a3**2 + b3**2)
    distance3= sqrt(a4**2 + b4**2)
    distance4= sqrt(a5**2 + b5**2)
    distance5= sqrt(a6**2 + b6**2)
    distance6= sqrt(a7**2 + b7**2)
    distance7= sqrt(a8**2 + b8**2)
    distance8= sqrt(a9**2 + b9**2)
    
    #decied is it touch the enemy
    if distance<=15:
        ball.y=0
        ball.x=random(20,680)
        speed1.y=random(1,5)
        ball.y+=speed1.y
        score+=1
        
        
    if distance1<=15:
        ball.y=0
        ball.x=random(20,680)
        speed1.y=random(1,5)
        ball.y+=speed1.y
        score+=1
        
        
    if distance2<=15:
        ball.y=0
        ball.x=random(20,680)
        speed1.y=random(1,5)
        ball.y+=speed1.y
        score+=1
       

    if distance3<=15:
        ball.y=0
        ball.x=random(20,680)
        speed1.y=random(1,5)
        ball.y+=speed1.y
        score+=1
       

    if distance4<=15:
        ball.y=0
        ball.x=random(20,680)
        speed1.y=random(1,5)
        ball.y+=speed1.y
        score+=1
        

    if distance5<=15:
        ball.y=0
        ball.x=random(20,680)
        speed1.y=random(1,5)
        ball.y+=speed1.y
        score+=1
       

    if distance6<=15:
        ball.y=0
        ball.x=random(20,680)
        speed1.y=random(1,5)
        ball.y+=speed1.y
        score+=1
        

    if distance7<=15:
        ball.y=0
        ball.x=random(20,680)
        speed1.y=random(1,5)
        ball.y+=speed1.y
        score+=1
        
        
    if distance8<=15:
        ball.y=0
        ball.x=random(20,680)
        speed1.y=random(3,6.5)
        ball.y+=speed1.y
        score+=1
       
    aa=x2-bigenemy.x
    aa2=x3-bigenemy.x
    aa3=x4-bigenemy.x
    aa4=x5-bigenemy.x
    aa5=x6-bigenemy.x
    aa6=x7-bigenemy.x
    aa7=x8-bigenemy.x
    aa8=x9-bigenemy.x
    aa9=x10-bigenemy.x
    bb=y2-bigenemy.y
    bb2=y3-bigenemy.y
    bb3=y4-bigenemy.y
    bb4=y5-bigenemy.y
    bb5=y6-bigenemy.y
    bb6=y7-bigenemy.y
    bb7=y8-bigenemy.y
    bb8=y9-bigenemy.y
    bb9=y10-bigenemy.y
        



    if 0<aa<120 and 50<bb<60 or -30<aa<0 and 50<bb<60:
        energy-=5
        if energy==0:
            bigenemy.y=-30
            bigenemy.x=random(20,580)
            speed1.x=random(1,5)
            bigenemy.y+=speed1.x
            energy=40
            score+=4
        
        
    if 0<aa2<120 and 50<bb2<60 or -30<aa2<0 and 50<bb2<60:
        energy-=5
        if energy==0:
            bigenemy.y=-30
            bigenemy.x=random(20,580)
            speed1.x=random(1,5)
            bigenemy.y+=speed1.x
            energy=40
            score+=4
        
        
    if 0<aa3<120 and 50<bb3<60 or -30<aa3<0 and 50<bb3<60:
        energy-=5
        if energy==0:
            bigenemy.y=-30
            bigenemy.x=random(20,580)
            speed1.x=random(1,5)
            bigenemy.y+=speed1.x
            energy=40
            score+=4
       

    if 0<aa4<120 and 50<bb4<60 or -30<aa4<0 and 50<bb4<60:
        energy-=5
        if energy==0:
            bigenemy.y=-30
            bigenemy.x=random(20,580)
            speed1.x=random(1,5)
            bigenemy.y+=speed1.x
            energy=40
            score+=4
       

    if 0<aa5<120 and 50<bb5<60 or -30<aa5<0 and 50<bb5<60:
        energy-=5
        if energy==0:
            bigenemy.y=-30
            bigenemy.x=random(20,580)
            speed1.x=random(1,5)
            bigenemy.y+=speed1.x
            energy=40
            score+=4
        

    if 0<aa6<120 and 50<bb6<60 or -30<aa6<0 and 50<bb6<60:
        energy-=5
        if energy==0:
            bigenemy.y=-30
            bigenemy.x=random(20,580)
            speed1.x=random(1,5)
            bigenemy.y+=speed1.x
            energy=40
            score+=4
       

    if 0<aa7<120 and 50<bb7<60 or -30<aa7<0 and 50<bb7<60:
        energy-=5
        if energy==0:
            bigenemy.y=-30
            bigenemy.x=random(20,580)
            speed1.x=random(1,5)
            bigenemy.y+=speed1.x
            energy=40
            score+=4
        

    if 0<aa8<120 and 50<bb8<60 or -30<aa8<0 and 50<bb8<60:
        energy-=5
        if energy==0:
            bigenemy.y=-30
            bigenemy.x=random(20,580)
            speed1.x=random(1,5)
            bigenemy.y+=speed1.x
            energy=40
            score+=4
        
        
    if 0<aa9<120 and 50<bb9<60 or -30<aa9<0 and 50<bb9<60:
        energy-=5
        if energy==0:
            bigenemy.y=-30
            bigenemy.x=random(20,580)
            speed1.x=random(1,5)
            bigenemy.y+=speed1.x
            energy=40
            score+=4
        
        
        
        
    #reset the ball
    if ball.y>=715:
        ball.y=0
        ball.x=random(20,680)
        speed1.y=random(3,6.5)
        ball.y+=speed1.y 
    if bigenemy.y>=730:
        bigenemy.y=0
        bigenemy.x=random(20,620)
        speed1.x=random(1,5)
        ball.y+=speed1.y
        energy=40
        
   
   #if the enemy touch you plane, you lose
    c=abs(x-ball.x)
    d=abs(y-25-ball.y)
    dis=sqrt(c**2 + d**2)
    e=x-15-bigenemy.x
    f=abs(y-40-bigenemy.y)
    if dis<30 or 0<e<120 and f<60 or -30<e<0 and f<60:
        fill(70)
        textSize(60)
        text("You lose!",width/2-100,height/2)
        speed1.y=0
        speed.y=0
        speed1.x=0
            
        
    # score 
    fill(70)   
    textSize(40)
    text(score,50,70)
    
    if keyPressed is True and keyCode==16:
        score=0
        speed.y=5
        speed1.y=random(3,6.5)
        speed1.x=random(1,5)
        ball.x=random(20,680)
        ball.y=-30
        bigenemy.x=random(20,620)
        bigenemy.y=-70
        energy=40
           
