import random
import math
import os
 


class TresenRaya:
    def __init__(self):
        self.plano = ['-' for _ in range(9)]
        if random.randint(0, 1) == 1:
            self.Jugador_persona = 'X'
            self.Jugador_bot = "O"
        else:
            self.Jugador_persona = "O"
            self.Jugador_bot = "X"

    def Ver_plano(self):
        print("")
        for i in range(3):
            print("  ",self.plano[0+(i*3)]," | ",self.plano[1+(i*3)]," | ",self.plano[2+(i*3)])
            print("")
            
    def esllenoelplano(self,estado):
        return not "-" in estado

    def Jugadorganador(self,estado,jugador):
        if estado[0]==estado[1]==estado[2] == jugador: return True
        if estado[3]==estado[4]==estado[5] == jugador: return True
        if estado[6]==estado[7]==estado[8] == jugador: return True
        if estado[0]==estado[3]==estado[6] == jugador: return True
        if estado[1]==estado[4]==estado[7] == jugador: return True
        if estado[2]==estado[5]==estado[8] == jugador: return True
        if estado[0]==estado[4]==estado[8] == jugador: return True
        if estado[2]==estado[4]==estado[6] == jugador: return True

        return False

    def comprobarGanador(self):
        if self.Jugadorganador(self.plano,self.Jugador_persona):
            os.system("cls")
            print(f"   Player {self.Jugador_persona}gano el juego!!!")
            return True
            
        if self.Jugadorganador(self.plano,self.Jugador_bot):
            os.system("cls")
            print(f"   Player {self.Jugador_bot} gano el juego!!!")
            return True

        if self.esllenoelplano(self.plano):
            os.system("cls")
            print("   Empataron!")
            return True
        return False

    def start(self):
        bot = JuegaComputadora(self.Jugador_bot)
        persona = Jugador_persona(self.Jugador_persona)
        while True:
            os.system("cls")
            print(f"   Jugador{self.Jugador_persona}tu turno")
            self.Ver_plano()
            
            
            square = persona.persona_move(self.plano)
            self.plano[square] = self.Jugador_persona
            if self.comprobarGanador():
                break
            
            
            square = bot.maquina_move(self.plano)
            self.plano[square] = self.Jugador_bot
            if self.comprobarGanador():
                break

        
        print()
        self.Ver_plano()

class Jugador_persona:
    def __init__(self,letter):
        self.letter = letter
    
    def persona_move(self,estado):
       
        while True:
            square =  int(input("Enter the square to fix spot(1-9): "))
            print()
            if estado[square-1] == "-":
                break
        return square-1

class JuegaComputadora(TresenRaya):
    def __init__(self,letter):
        self.Jugador_bot = letter
        self.Jugador_persona = "X" if letter == "O" else "O"

    def jugadores(self,estado):
        n = len(estado)
        x = 0
        o = 0
        for i in range(9):
            if(estado[i] == "X"):
                x = x+1
            if(estado[i] == "O"):
                o = o+1
        
        if(self.Jugador_persona == "X"):
            return "X" if x==o else "O"
        if(self.Jugador_persona == "O"):
            return "O" if x==o else "X"
    
    def actions(self,estado):
        return [i for i, x in enumerate(estado) if x == "-"]
    
    def result(self,estado,action):
        newState = estado.copy()
        jugador = self.jugadores(estado)
        newState[action] = jugador
        return newState
    
    def terminal(self,estado):
        if(self.Jugadorganador(estado,"X")):
            return True
        if(self.Jugadorganador(estado,"O")):
            return True
        return False

    def minimax(self, estado, jugador):
        max_player = self.Jugador_persona 
        other_player = 'O' if jugador == 'X' else 'X'

     
        if self.terminal(estado):
            return {'position': None, 'score': 1 * (len(self.actions(estado)) + 1) if other_player == max_player else -1 * (
                        len(self.actions(estado)) + 1)}
        elif self.esllenoelplano(estado):
            return {'position': None, 'score': 0}

        if jugador == max_player:
            best = {'position': None, 'score': -math.inf}  
        else:
            best = {'position': None, 'score': math.inf}  
        for possible_move in self.actions(estado):
            newState = self.result(estado,possible_move)
            sim_score = self.minimax(newState, other_player)  

            sim_score['position'] = possible_move  

            if jugador == max_player: 
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

    def maquina_move(self,estado):
        square = self.minimax(estado,self.Jugador_bot)['position']
        return square


tres_en_raya = TresenRaya()
tres_en_raya.start()