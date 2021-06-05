def make_move(selected_place,current_state):
    num_of_stones=current_state[selected_place]
    if num_of_stones==0 or selected_place not in range(0,13) :
        valid_move=0
    else:
        valid_move=1
    if selected_place in range(0,6):
        turn = 'min'
    elif selected_place in range(7,13):
        turn = 'max'

    returned_state=current_state.copy()
    returned_state[selected_place]=0
    place_to_add_stone=selected_place+1

    while True:
        if num_of_stones==0:
            break
        if stealing==1 and num_of_stones==1 and selected_place in range(0,6) and place_to_add_stone in range(0,6) and returned_state[place_to_add_stone]==0:
            returned_state[6]+=returned_state[12-place_to_add_stone]+1
            returned_state[12-place_to_add_stone]=0
            break
        if stealing==1 and num_of_stones==1 and selected_place in range(7,13) and place_to_add_stone in range(7,13) and returned_state[place_to_add_stone]==0:
            returned_state[13]+=returned_state[12-place_to_add_stone]+1
            returned_state[12-place_to_add_stone]=0
            break
        if num_of_stones==1 and selected_place in range(0,6) and place_to_add_stone==6:
            turn = 'max'
        if num_of_stones==1 and selected_place in range(7,13) and place_to_add_stone==13:
            turn = 'min'
        if not(((selected_place in range(0,6)) and (place_to_add_stone==13)) or((selected_place in range(7,13)) and (place_to_add_stone==6))):
            returned_state[place_to_add_stone]+=1
            num_of_stones-=1
        place_to_add_stone+=1
        place_to_add_stone=place_to_add_stone%14
    return valid_move, returned_state, turn
        

'''
state=[4,4,4,4,4,400,0,4,4,4,4,4,4,0]
stealing = int(input("do you want stealing mode ? (yes = press 1, no = press 0)  \n"))
make_move(5,state)
x,y,z=make_move(5,state)
'''
