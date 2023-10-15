

tablero=[[0,0,0],
         [0,0,0],
         [0,0,0]]
turno = 1

def reiniciar():
    global tablero
    global turno
    tablero=[[0,0,0],
         [0,0,0],
         [0,0,0]]
    turno = 1


def dib_cruz(surface,x,y,ancho,altura):
    pygame.draw.line(surface, (0,0,0), (x,y), (x+ancho,y+altura),width=10)
    pygame.draw.line(surface, (0,0,0), (x+ancho,y), (x,y+altura),width=10)


def dib_tablero():
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, (0,0,0), (i*200, j*200, 200, 200),width=1)


def logica():
    x,y=pygame.mouse.get_pos()
    x=x//200
    y=y//200
    global turno
    global tablero
    if(pygame.mouse.get_pressed()[0]==True):
        print(x,"  ,  ",y," turno: ",turno)
        print(tablero)
        if(tablero[x][y]==0):
            turno=turno+1
            if(turno%2==0):
                tablero[x][y]=1
            else:
                tablero[x][y]=-1
    

def dibujar_piezas():
    global tablero
    for i in range(3):
        for j in range(3):
            if(tablero[i][j]==1):
                dib_cruz(screen,i*200,j*200,200,200)
               # pygame.draw.rect(screen, (50,150,50), (i*200, j*200, 200, 200))
            elif(tablero[i][j]==-1):
                
                pygame.draw.circle(screen, (0,50,100), (i*200+100, j*200+100), 100,width =10)
               # pygame.draw.rect(screen, (0,50,100), (i*200, j*200, 200, 200))

def resultado(screen):
    
    global turno
    if turno<=10:
        if(tablero[0][0]==tablero[1][1]==tablero[2][2]==1 or 
           tablero[1][1]==tablero[2][0]==tablero[0][2]==1 or
           tablero[0][0]==tablero[0][1]==tablero[0][2]==1 or
           tablero[1][0]==tablero[1][1]==tablero[1][2]==1 or
           tablero[2][0]==tablero[2][1]==tablero[2][2]==1 or
           tablero[0][0]==tablero[1][0]==tablero[2][0]==1 or
           tablero[0][1]==tablero[1][1]==tablero[2][1]==1 or
           tablero[0][2]==tablero[1][2]==tablero[2][2]==1):
            text_surface = my_font.render('Ganador CRUZ', False, (0, 0, 0))
            screen.blit(text_surface, (240,250))
            return 1
            #turno+=1
        elif(tablero[0][0]==tablero[1][1]==tablero[2][2]==-1 or 
           tablero[1][1]==tablero[2][0]==tablero[0][2]==-1 or
           tablero[0][0]==tablero[0][1]==tablero[0][2]==-1 or
           tablero[1][0]==tablero[1][1]==tablero[1][2]==-1 or
           tablero[2][0]==tablero[2][1]==tablero[2][2]==-1 or
           tablero[0][0]==tablero[1][0]==tablero[2][0]==-1 or
           tablero[0][1]==tablero[1][1]==tablero[2][1]==-1 or
           tablero[0][2]==tablero[1][2]==tablero[2][2]==-1):
            text_surface = my_font.render('Ganador CIRCULO', False, (0, 0, 0))
            screen.blit(text_surface, (240,250))
            return 1
            #turno+=1
        else:
            return 0
    else:
        text_surface = my_font.render('EMPATE', False, (0, 0, 0))
        screen.blit(text_surface, (240,250))
        return 2

import pygame
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)


# Inicializar la ventana principal
screen = pygame.display.set_mode([600, 600])


# Correr el programa hasta que se desee parar
running = True
while running:
    # el usuario seleciono el boton de salida?
    for event in pygame.event.get():
        #print(event)
        
        if event.type == pygame.QUIT:
            running = False

    # Llenar el teclado de blanco
    screen.fill((255, 255, 255))

    # Dibujar el tablero
    
    if(resultado(screen)==0):
        logica()
    dibujar_piezas()
    dib_tablero()
    resultado(screen)
   
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()