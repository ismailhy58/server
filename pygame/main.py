from numpy import sqrt
import pygame
import pandas as pd 
#import time


#initialize 
pygame.init() 

#variables
screen_width = 800
screen_height = 600
treshold = 150


#screen
screen = pygame.display.set_mode((screen_width,screen_height)) #create screen
running = True


#Title and icon
pygame.display.set_caption("DeviOn")
icon = pygame.image.load('devion.JPG')
pygame.display.set_icon(icon)

#background
background = pygame.image.load('person3.png')

#location information
font = pygame.font.Font('freesansbold.ttf',20)
textX=800-140
textY=10

#person
personImg = pygame.image.load('person3.png')
personX = 360
personY = 250



#door
doorImg = pygame.image.load('door.png')
doorX = 800-64
doorY = 250
warning4Img=pygame.image.load('warning.png')
warning4X = doorX + 32
warning4Y = doorY + 40

#artwork1
artwork1Img = pygame.image.load('artwork1.png')
artwork1X = 64
artwork1Y = 250
warning1Img=pygame.image.load('warning.png')
warning1X = artwork1X + 32
warning1Y = artwork1Y + 32
#artwork2
artwork2Img = pygame.image.load('artwork2.png')
artwork2X = 350
artwork2Y = 64
warning2Img=pygame.image.load('warning.png')
warning2X = artwork2X + 32
warning2Y = artwork2Y + 32

#artwork3
artwork3Img = pygame.image.load('artwork3.png')
artwork3X = 350
artwork3Y = 600 - 64
warning3Img=pygame.image.load('warning.png')
warning3X = artwork3X + 32
warning3Y = artwork3Y + 32

#origin
originImg = pygame.image.load('origin.png')
originX = -16
originY = -16

def show_location(value_x,value_y,x,y):
    location = font.render("X: " + str(value_x) + " Y: " + str(value_y), True, (255,255,255) )
    screen.blit(location,(x,y))

def person(x,y):
    screen.blit(personImg,(x,y))
def artwork1(x,y):
    screen.blit(artwork1Img,(x,y))
def artwork2(x,y):
    screen.blit(artwork2Img,(x,y))
def artwork3(x,y):
    screen.blit(artwork3Img,(x,y))
def door(x,y):
    screen.blit(doorImg,(x,y))
def warning1(x,y):
    screen.blit(warning1Img,(x,y))
def warning2(x,y):
    screen.blit(warning2Img,(x,y))
def warning3(x,y):
    screen.blit(warning3Img,(x,y))
def warning4(x,y):
    screen.blit(warning4Img,(x,y))
def origin(x,y):
    screen.blit(originImg,(x,y))

def distance(x1,x2,y1,y2):
    distance = sqrt((x1-x2)**2+(y1-y2)**2)
    return distance

#Game loop
while running:
    #screen color RGB     
    screen.fill((0,0,0))
    #personX += 0.1         #to right +, to left -
    #personY +=0.1       #to down + , to up - 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #close check
            running=False 
            
    data = pd.read_csv('data.csv')
    personX_pd = data['x_value']
    personY_pd = data['total_1']
    #print("read values array") #debug
    #print(personX_pd.values)   #debug
    #print(personY_pd.values)   #debug
    personX=personX_pd.values[len(personX_pd.values)-1]
    personY=personY_pd.values[len(personY_pd.values)-1]
    #print("last read") #debug
    #print(personX)     #debug
    #print(personY)     #debug
    person(personX, personY)
    show_location(personX,personY,textX,textY)
    origin(originX,originY)
    artwork1(artwork1X,artwork1Y)
    artwork2(artwork2X,artwork2Y)
    artwork3(artwork3X,artwork3Y)
    door(doorX,doorY)
    distance1 = distance(personX,artwork1X,personY,artwork1Y)
    distance2 = distance(personX,artwork2X,personY,artwork2Y)
    distance3 = distance(personX,artwork3X,personY,artwork3Y)
    distance4 =  distance(personX,doorX,personY,doorY) 
    if distance1 < treshold:
        warning1(warning1X,warning1Y)
    if distance2 < treshold:
        warning2(warning2X,warning2Y)
    if distance3 < treshold:
        warning3(warning3X,warning3Y)
    if distance4 < treshold:
        warning4(warning4X,warning4Y)
    
    #time.sleep(1)
    pygame.display.update()