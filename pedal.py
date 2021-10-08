from turtle import Turtle

class pedal(Turtle):  
   
    def __init__(self,pos):
        super().__init__()
        #self.pedal= Turtle()
        self.pedal_construct(pos)
  
    def pedal_construct(self,position):
          
          self.color("white")
          self.shape("square")
          self.penup()
          self.shapesize(stretch_wid=5,stretch_len=1)
          self.goto(position)

    def move_up(self):
      new_y = self.ycor()+20
      if new_y>250:
        new_y=250
        self.goto(self.xcor(),new_y)
      else:
         self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor()-20
        if new_y<-250:
          new_y= -250
          self.goto(self.xcor(),new_y)
        else:
           self.goto(self.xcor(),new_y)




