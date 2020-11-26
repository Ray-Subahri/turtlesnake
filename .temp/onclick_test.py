
# import package 
import turtle 
  
  
# method to action 
def fxn(x,y): 
      
    # some motion 
    turtle.right(90) 
    turtle.forward(100) 
  
# turtle speed to slowest 
turtle.speed(1) 
  
# motion 
turtle.fd(100) 
  
# allow user to click  
# for some action 
turtle.onclick(fxn)


turtle.done()