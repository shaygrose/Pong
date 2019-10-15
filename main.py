from tkinter import *
import os
import random
import time

#paddle1 is RIght, paddle is Left

class Ball:
    def __init__(self, canvas, paddleR, paddleL, color):
        self.canvas = canvas 
        self.id = canvas.create_oval(10,10, 35, 35, fill = color)
        self.canvas.move(self.id, 327, 220) #setting starting position
        self.x = random.choice([-2.5, 2.5])  #how fast the ball will be going
        self.y = -2.5
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.paddleL = paddleL
        self.paddleR = paddleR
        self.leftScore = 0
        self.rightScore = 0
        self.drawPL = None
        self.drawPR = None

    def updateLPaddle(self, val):
        self.canvas.delete(self.drawPL)
        self.drawPL = self.canvas.create_text(170,50, font = ('', 40), text = str(val), fill = 'white')

    def updateRPaddle(self, val):
        self.canvas.delete(self.drawPR)
        self.drawPR = self.canvas.create_text(550,50, font = ('', 40), text = str(val), fill = 'white')

       
    def hit_paddleL(self,pos):
        paddle_pos = self.canvas.coords(self.paddleL.id)
		
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True

            return False

#Checks for collision of paddle and ball for paddle right		   
    def hit_paddleR(self,pos):
		
        paddle_pos = self.canvas.coords(self.paddleR.id)
		
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True	
				
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) #draws ball in position set in init 
       
        if pos[1]<=0:
           self.y = 4
        if pos[3] >= self.canvas_height:
            self.y=-4
        if pos[0]<=0:
            self.rightScore +=1
            self.canvas.move(self.id, 327, 220)
            self.x = 4
            self.updateRPaddle(self.rightScore)
        if pos[2]>=self.canvas_width:
            self.leftScore +=1
            self.canvas.move(self.id,-327,-220)
            self.x = -4
            self.updateLPaddle(self.leftScore)
        if self.hit_paddleL(pos):
            self.x = 4
        if self.hit_paddleR(pos):
            self.x = -4  

class PaddleL:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0,200,20,310, fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        #setting key bindings
        self.canvas.bind_all('w',self.left)
        self.canvas.bind_all('s',self.right)

    def left(self, e):
            self.y = -5
    
    def right(self, e):
            self.y = 5

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=500:
            self.y=0


class PaddleR:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(680,200,710,310, fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        #setting key bindings
        self.canvas.bind_all('<KeyPress-Up>',self.left)
        self.canvas.bind_all('<KeyPress-Down>',self.right)

    def left(self, e):
            self.y = -5
    
    def right(self, e):
            self.y = 5

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=500:
            self.y=0





#setting up screen basics
tk = Tk()
tk.title("Pong")
tk.geometry('+300+100')
tk.resizable(0,0)
canvas = Canvas(tk, width=700, height=500, bd=0, highlightthickness=0) #bd = background drop
canvas.config(bg='black')
canvas.pack()
tk.update()
canvas.create_line(350,0,350,500, fill='white')




#initialize objects
Lpaddle = PaddleL(canvas, 'white')
Rpaddle = PaddleR(canvas, 'white')
ball = Ball(canvas, Rpaddle, Lpaddle, 'blue')


while 1:
    ball.draw()
    Lpaddle.draw()
    Rpaddle.draw()
  
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01) #slight delay between updates



quit()

tk.mainloop()