tac_toe_mod = [[i for i in range(3)]for j in range(3)] 
print(tac_toe_mod[2][0])

# for i in tac_toe_mod :
#     for j in i :
#         for n in range(1,10) :
#             # tac_toe_mod[i][j] = n 
for j in range(len(tac_toe_mod)):
    print(tac_toe_mod[j])

# def is_Won():
#     for j in range(len(tac_toe_mod)):
#         for i in range(len(tac_toe_mod[j])):
#             if tac_toe_mod[j][0] == tac_toe_mod[j][1] == tac_toe_mod[j][2] :
#                 Won = True
#             elif tac_toe_mod[0][0] == tac_toe_mod[1][1] == tac_toe_mod[2][2] :
#                     Won = True
            