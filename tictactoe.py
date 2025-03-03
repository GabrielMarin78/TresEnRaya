from random import randrange

def mostrar_tablero(tablero):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("+", 7 * "-", "+", 7 * "-", "+", 7 * "-", "+", sep="")
    print("|", 7 * " ", "|", 7 * " ", "|", 7 * " ", "|", sep="")
    print("|", 3 * " ", tablero[0][0], 3 * " ", "|", 3 * " ", tablero[0][1], 3 * " ", "|", 3 * " ", tablero[0][2], 3 * " ", "|", sep="")
    print("|", 7 * " ", "|", 7 * " ", "|", 7 * " ", "|", sep="") 
    print("+", 7 * "-", "+", 7 * "-", "+", 7 * "-", "+", sep="")
    print("|", 7 * " ", "|", 7 * " ", "|", 7 * " ", "|", sep="")
    print("|", 3 * " ", tablero[1][0], 3 * " ", "|", 3 * " ", tablero[1][1], 3 * " ", "|", 3 * " ", tablero[1][2], 3 * " ", "|", sep="")
    print("|", 7 * " ", "|", 7 * " ", "|", 7 * " ", "|", sep="") 
    print("+", 7 * "-", "+", 7 * "-", "+", 7 * "-", "+", sep="")
    print("|", 7 * " ", "|", 7 * " ", "|", 7 * " ", "|", sep="")
    print("|", 3 * " ", tablero[2][0], 3 * " ", "|", 3 * " ", tablero[2][1], 3 * " ", "|", 3 * " ", tablero[2][2], 3 * " ", "|", sep="")
    print("|", 7 * " ", "|", 7 * " ", "|", 7 * " ", "|", sep="") 
    print("+", 7 * "-", "+", 7 * "-", "+", 7 * "-", "+", sep="")

def hacer_jugada(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    try:
        global total_movimientos, signo
        signo = "O"
        mostrar_tablero(tablero)
        movimiento = int(input("\nIngresa tu movimiento: "))
        if movimiento == 1:
            if board[0][0] != "X" and board[0][0] != "O":
                board[0][0] = signo
                print("\nHas jugado en la posición 1")
                total_movimientos += 1
                mostrar_tablero(board)
            else:
                print("\nLa posición 1 ya está ocupada")
                hacer_jugada(board)
        elif movimiento == 2:
            if board[0][1] != "X" and board[0][1]:
                board[0][1] = signo
                print("\nHas jugado en la posición 2")
                total_movimientos += 1
                mostrar_tablero(board)
            else:
                print("\nLa posición 2 ya está ocupada")
                hacer_jugada(board)
        elif movimiento == 3:
            if board[0][2] != "X" and board[0][2]!= "O":
                board[0][2] = signo
                print("\nHas jugado en la posición 3")
                total_movimientos += 1
                mostrar_tablero(board)
            else:
                print("\nLa posición 3 ya está ocupada")
                hacer_jugada(board)
        elif movimiento == 4:
            if board[1][0] != "X" and board[1][0]!= "O":
                board[1][0] = signo
                print("\nHas jugado en la posición 4")
                total_movimientos += 1
                mostrar_tablero(board)
            else:
                print("\nLa posición 4 ya está ocupada")
                hacer_jugada(board)
        elif movimiento == 5: # Jugada inicial de la computadora por defecto
            print("\nLa posición 5 ya está ocupada")
            hacer_jugada(board)
        elif movimiento == 6:
            if board[1][2] != "X" and board[1][2]!= "O":
                board[1][2] = signo
                print("\nHas jugado en la posición 6")
                total_movimientos += 1
                mostrar_tablero(board)
            else:
                print("\nLa posición 6 ya está ocupada")
                hacer_jugada(board)
        elif movimiento == 7:
            if board[2][0] != "X" and board[2][0] != "O":
                board[2][0] = signo
                print("\nHas jugado en la posición 7")
                total_movimientos += 1
                mostrar_tablero(board)
            else:
                print("\nLa posición 7 ya está ocupada")
                hacer_jugada(board)
        elif movimiento == 8:
            if board[2][1]!= "X" and board[2][1]!= "O":
                board[2][1] = signo
                print("\nHas jugado en la posición 8")
                total_movimientos += 1
                mostrar_tablero(board)
            else:
                print("\nLa posición 8 ya está ocupada")
                hacer_jugada(board)
        elif movimiento == 9:
            if board[2][2]!= "X" and board[2][2]!= "O":
                board[2][2] = signo
                print("\nHas jugado en la posición 9")
                total_movimientos += 1
                mostrar_tablero(board)
            else:
                print("\nLa posición 9 ya está ocupada")
                hacer_jugada(board)
        else:
            print("\nDebes ingresar un número del 1 al 9\n")
            hacer_jugada(board)
    except ValueError:
        print("\nDebes ingresar un número del 1 al 9\n")
        hacer_jugada(board)

def victory_for(board, signo):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if tablero[0][0] == tablero[1][1] and tablero[0][0] == tablero[2][2]:
        if signo == "O":
            print("Has ganado!")
        else:
            mostrar_tablero(tablero)
            print("Ha ganado la computadora!")
        return True
    elif tablero[0][2] == tablero[1][1] and tablero[0][2] == tablero[2][0]:
        if signo == "O":
            print("Has ganado!")
        else:
            mostrar_tablero(tablero)
            print("Ha ganado la computadora!")
        return True
    else:
        for i in range(3):
            if tablero[i][0] == tablero[i][1] and tablero[i][0] == tablero[i][2]:
                if signo == "O":
                    print("Has ganado!")
                else:
                    mostrar_tablero(tablero)
                    print("Ha ganado la computadora!")
                return True
            elif tablero[0][i] == tablero[1][i] and tablero[0][i] == tablero[2][i]:
                if signo == "O":
                    print("Has ganado!")
                else:
                    mostrar_tablero(tablero)
                    print("Ha ganado la computadora!")
                return True
        
def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    global total_movimientos
    global signo
    signo = "X"
    movimiento = randrange(1, 10)
    if movimiento == 1:
        if board[0][0] != "X" and board[0][0]!= "O":
            board[0][0] = signo
            print("\nLa computadora ha jugado en la posición 1")
            total_movimientos += 1
        else:
            draw_move(board)
    elif movimiento == 2:
        if board[0][1] != "X" and board[0][1]!= "O":
            board[0][1] = signo
            print("\nLa computadora ha jugado en la posición 2")
            total_movimientos += 1
        else:
            draw_move(board)
    elif movimiento == 3:
        if board[0][2] != "X" and board[0][2]!= "O":
            board[0][2] = signo
            print("\nLa computadora ha jugado en la posición 3")
            total_movimientos += 1
        else:
            draw_move(board)
    elif movimiento == 4:
        if board[1][0] != "X" and board[1][0]!= "O":
            board[1][0] = signo
            print("\nLa computadora ha jugado en la posición 4")
            total_movimientos += 1
        else:
            draw_move(board)
    elif movimiento == 5: # Jugada inicial de la computadora por defecto
        draw_move(board)
    elif movimiento == 6:
        if board[1][2] != "X" and board[1][2]!= "O":
            board[1][2] = signo
            print("\nLa computadora ha jugado en la posición 6")
            total_movimientos += 1
        else:
            draw_move(board)
    elif movimiento == 7:
        if board[2][0] != "X" and board[2][0]!= "O":
            board[2][0] = signo
            print("\nLa computadora ha jugado en la posición 7")
            total_movimientos += 1
        else:
            draw_move(board)
    elif movimiento == 8:
        if board[2][1] != "X" and board[2][1]!= "O":
            board[2][1] = signo
            print("\nLa computadora ha jugado en la posición 8")
            total_movimientos += 1
        else:
            draw_move(board)
    elif movimiento == 9:
        if board[2][2] != "X" and board[2][2]!= "O":
            board[2][2] = signo
            print("\nLa computadora ha jugado en la posición 9")
            total_movimientos += 1
        else:
            draw_move(board)
    
print("\n", 33*"*", sep="")
print("*** Bienvenido a TRES EN RAYA ***")
print(33*"*", "\n")
tablero = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
total_movimientos = 1
signo = ""

while True:
    hacer_jugada(tablero)
    if total_movimientos > 4:
        if victory_for(tablero, signo):
            break
        elif total_movimientos == 9:
            print("\nEmpate!")
            break
        
    draw_move(tablero)
    if total_movimientos > 4:
        if victory_for(tablero, signo):
            break
        elif total_movimientos == 9:
            mostrar_tablero(tablero)
            print("\nEmpate!")
            break
