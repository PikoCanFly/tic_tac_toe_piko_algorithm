from beautifultable import BeautifulTable
import random
import time
# import warnings
#
#
#
# warnings.simplefilter(action='ignore', category=FutureWarning)
table = BeautifulTable()
def make_table():



    table.rows.append([" ", " ", " "])
    table.rows.append([" ", " ", " "])
    table.rows.append([" ", " ", " "])
    table.columns.header= ["A", "B", "C"]
    table.rows.header = ["1", "2", "3"]


make_table()

def computer_turn(table = table):
    diag1 = [table.rows[0]['A'], table.rows[1]['B'], table.rows[2]['C']]
    diag2 = [table.rows[0]["C"], table.rows[1]["B"], table.rows[2]['A']]
    columns = ["A", "B", "C"]
    row = ""
    column = ""
    coordinates = ""

    for n in range(3):
        if diag1.count('O') == 2 and diag1.count(' ') > 0:
            coordinates = random.choice(["A0", "B1", "C2"])

        elif diag2.count('O') == 2 and diag2.count(' ') > 0:
            coordinates = random.choice(["C0", "B1", "A2"])
        else:
            for n in range(3):
                if table.rows[n].value.count('O') == 2 and table.rows[n].value.count(' ') > 0:
                    row = str(n)
                    break

            for c in columns:
                if table.columns[c].value.count('O') == 2 and table.columns[c].value.count(' ') > 0:
                    column = c
                    break
        if row == "" and column == "" and coordinates == "":
            if diag1.count('X')==2 and diag1.count(" ")>0:
                coordinates = random.choice(["A0", "B1", "C2"])

            elif diag2.count('X') == 2 and diag2.count(" ")>0:
                coordinates = random.choice(["C0", "B1", "A2"])
            if coordinates == "" and row=="":
                for n in range(3):
                    if table.rows[n].value.count('X')==2 and table.rows[n].value.count(' ')>0:
                        row = str(n)
                        break
            if coordinates == "" and column =="":
                for c in columns:
                    if table.columns[c].value.count('X')==2 and table.columns[c].value.count(' ')>0 :
                        column = c
                        break



        if coordinates != "":
            c = coordinates[0]
            r=coordinates[1]
        else:
            r = row
            c=column
            if c == "":
                c= random.choice(["A", "B", "C"])
            if r == "":
                r = random.randint(0,2)


    return f"{c}{r}"




def tic_tac_toe():
    print("\nLet's play Tic-Tac-Toe.\n"
          "I'll be 'O' and you'll be 'X'")
    time.sleep(0.5)
    # print('\n' * 10)  # prints 80 line breaks


    print("To begin tell me where you'd like to place your 'X'.\n"
          "For example, let's say you want to put it in the first cell. In that case,"
          "you'd type 'A1'. Simple! Right? 🤔\n")
    table = BeautifulTable()

    table.rows.append([" ", " ", " "])
    table.rows.append([" ", " ", " "])
    table.rows.append([" ", " ", " "])
    table.columns.header = ["A", "B", "C"]
    table.rows.header = ["1", "2", "3"]
    print(table)

def game_over(table):
    diag1 = [table.rows[0]['A'], table.rows[1]['B'], table.rows[2]['C']]
    diag2 = [table.rows[0]["C"], table.rows[1]["B"], table.rows[2]['A']]
    over = False
    for n in range(3):
        if table.columns[n].value.count('X') == 3 or table.rows[n].value.count('X') == 3 or diag1.count('X') == 3 \
                or diag2.count('X') == 3:
            over = True
            # print('Looks like you are the winner!')
        elif table.columns[n].value.count(' ') == 0 and table.rows[n].value.count(' ') == 0 and diag1.count(' ') == 0\
                and diag2.count(' ') == 0:
            # print("Looks like it's a tie.")
            over = True
        elif table.columns[n].value.count('O') == 3 or table.rows[n].value.count('O') == 3 or diag1.count(
                'O') == 3 or diag2.count('O') == 3:
            # print("Looks like I win!")
            over = True

    return over

def game_again():

        print(" \n\n GG ☺")
        time.sleep(0.5)
        again = input("Would you like to play again?[Y/N]").upper()
        if again == "Y":
            print("Great!")
            print('\n' * 5)

            return True
        else:
            print("That was fun! Bye bye!")
            return False




game_on=True
com_t = False
col_choices = ["A","B","C"]
row_choices = ["1","2","3"]




def main_game():
    while game_on:
        u_input = input("It's your turn. Tell me where you want to put your x.\n").upper()

        if u_input[0] not in col_choices or u_input[1] not in row_choices:
            print("Error --- [Invalid coordinates]\n"
                  "Please use this format column key i.e. : 'A', followed by row key i.e. '2'. Make sure your choices exist")
            time.sleep(0.5)
            print(table)

        else:
            try:
                column = u_input[0]
                row = int(u_input[1]) -1
            except:
                print("Enter valid coordinates.")


            else:
                if table.rows[row][column] == " ":
                    table.rows[row][column] = 'X'

                else:
                    print("Looks like slot is taken.")
                    print("try again\n", table)
                    continue
            game_over(table=table)

            comp_choice = computer_turn(table=table)

            column = comp_choice[0]
            row = int(comp_choice[1])

            if table.rows[row][column] != " " and game_over(table=table)!=True:
                comp_try_again = True
                while comp_try_again:
                    comp_choice = computer_turn()
                    column = comp_choice[0]
                    row = int(comp_choice[1])
                    if table.rows[row][column] == " ":
                        table.rows[row][column] = "O"
                        comp_try_again = False
                    else:
                        comp_try_again = True
                    print(table)
            else:
                table.rows[row][column] ='O'
                print(table)




            game_over(table=table)

            if game_over(table=table) == True:
                print(table)
                again = game_again()
                if again == True:
                    table.rows[0]=[" ", " ", " "]
                    table.rows[1]=[" ", " ", " "]
                    table.rows[2]=[" ", " ", " "]
                    print(table)


                else:
                    break



tic_tac_toe()
time.sleep(0.5)
main_game()