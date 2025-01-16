import random
def choose_option():

    options = ("piedra", "papel", "tijeras")

    while True:
        user_option = input("Usuario elige una opcion: ")
        if user_option in options:
            break
        else:
            print("elija una opcion valida porfavor")
    

    computer_option = random.choice(options)

    print(f"movimiento del usuario => {user_option}")
    print(f"movimiento de la computadora => {computer_option}")

    return user_option, computer_option


def game_rules(u_option,c_option,u_wins,c_wins):
  
    if u_option == c_option:
        print('empate!!')
    elif u_option == "piedra":
        if c_option == "tijeras":
            print('piedra gana a tijera')
            print('punto para el usuario')
            u_wins += 1
        else:
            print('papel gana a piedra')
            print("punto para la computadora!")
            c_wins += 1
    elif u_option == "papel":
        if c_option == "piedra":
            print("papel gana a piedra")
            print('punto para el usuario')
            u_wins += 1
        else:
            print('piedra ganan a tijeras')
            print("punto para la computadora")
            c_wins += 1
    elif u_option == "tijeras":
        if c_option == "papel":
            print("tijeras ganan a papel")
            print("punto para el usuario!")
            u_wins += 1
        else:
            print('papel gana a piedra')
            print("punto para la computadora")
            c_wins += 1

    return u_wins, c_wins

def run_game():

    computer_wins = 0
    user_wins = 0

    while True:
    
        u_option, c_option = choose_option()

        user_wins, computer_wins = game_rules(u_option,c_option,user_wins,computer_wins)


        if user_wins == 2:
            print("El usuario gana el juego")
            break
        elif computer_wins == 2:
            print("la computdora gana el juego")
            break
    



if __name__ == '__main__':
    

    run_game()