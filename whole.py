import save
current_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

load = int(input("do you want to load game ? (yes = press 1, no = press 0)  \n"))
stealing = 1
turn = ""
if load == 1:
    current_state, stealing = save.load()
    turn = 'min'

else:
    stealing = int(
        input("do you want stealing mode ? (yes = press 1, no = press 0)  \n"))
    turn = input(
        "do you want to start ? (yes = enter 'min', no = enter 'max')  \n")


class node:
    def __init__(self, state, turn):

        self.is_leaf = 0
        self.cost = 0
        self.min_max = turn
        self.children = []
        self.state = state
        self.pruned = 0
        self.move_made_me = 0


def create_tree(root, depth):

    if depth == 0:
        root.is_leaf = 1
        root.cost = cost_fun(root.state)
        return root
    if root.min_max == 'max':
        places = range(0, 6)
    else:
        places = range(7, 13)

    for place in places:
        valid_move, returned_state, turn = make_move(place, root.state)
        if valid_move == 0:
            continue
        child_Node = node(returned_state, turn)
        child_Node.move_made_me = place
        temp = create_tree(child_Node, depth-1)
        root.children.append(temp)
    return root


def get_move(state):
    s = state.copy()
    root = node(s, 'max')
    create_tree(root, 4)
    alpha_beta(root, float('-inf'), float('inf'), 'max')
    temp = []
    for child in root.children:
        if child.cost == root.cost:
            temp.append(child)
    if len(temp) > 1:
        for i in temp:
            if i.pruned == 0:
                return i.move_made_me
    else:
        return temp[0].move_made_me


def cost_fun(state):
    temp1 = state[0:5]
    temp2 = state[7:12]
    cost = -1*sum([x1 - x2 for (x1, x2) in zip(temp1, temp2)])
    return cost


def is_end(state):
    s = state.copy()
    sum_max = 0
    sum_min = 0
    who_win = 'computer winned'
    for i in range(0, 6):
        sum_max += s[i]
        sum_min += s[i+7]
    if sum_max == 0:
        ended = 1
        if s[6] > 48-s[6]:
            who_win = 'computer winned'
        elif s[6] < 48-s[6]:
            who_win = 'player winned'
        else:
            who_win = 'Draw'
    elif sum_min == 0:
        ended = 1
        if s[13] > 48-s[13]:
            who_win = 'player winned'
        elif s[13] < 48-s[13]:
            who_win = 'compuuter winned'
        else:
            who_win = 'Draw'
    else:
        ended = 0
    return ended, who_win


def make_move(selected_place, current_state):

    num_of_stones = current_state[selected_place]
    if num_of_stones == 0 or selected_place not in range(0, 13):
        valid_move = 0
    else:
        valid_move = 1
    if selected_place in range(0, 6):
        turn = 'min'
    elif selected_place in range(7, 13):
        turn = 'max'

    returned_state = current_state.copy()
    returned_state[selected_place] = 0
    place_to_add_stone = selected_place+1

    while True:
        if num_of_stones == 0:
            break
        if stealing == 1 and num_of_stones == 1 and selected_place in range(0, 6) and place_to_add_stone in range(0, 6) and returned_state[place_to_add_stone] == 0:
            returned_state[6] += returned_state[12-place_to_add_stone]+1
            returned_state[12-place_to_add_stone] = 0
            break
        if stealing == 1 and num_of_stones == 1 and selected_place in range(7, 13) and place_to_add_stone in range(7, 13) and returned_state[place_to_add_stone] == 0:
            returned_state[13] += returned_state[12-place_to_add_stone]+1
            returned_state[12-place_to_add_stone] = 0
            break
        if num_of_stones == 1 and selected_place in range(0, 6) and place_to_add_stone == 6:
            turn = 'max'
        if num_of_stones == 1 and selected_place in range(7, 13) and place_to_add_stone == 13:
            turn = 'min'
        if not(((selected_place in range(0, 6)) and (place_to_add_stone == 13)) or ((selected_place in range(7, 13)) and (place_to_add_stone == 6))):
            returned_state[place_to_add_stone] += 1
            num_of_stones -= 1
        place_to_add_stone += 1
        place_to_add_stone = place_to_add_stone % 14
    return valid_move, returned_state, turn


def alpha_beta(node, alpha, beta, max_min):
    if node.is_leaf == 1:
        return node.cost

    if max_min == 'max':
        temp = float('-inf')
        for child in node.children:
            if child.min_max == 'min':
                child.cost = alpha_beta(child, alpha, beta, 'min')
                temp = max(temp, child.cost)
            else:
                child.cost = alpha_beta(child, alpha, beta, 'max')
                temp = max(temp, child.cost)
            alpha = max(alpha, temp)
            if alpha >= beta:
                node.pruned = 1
                break  # beta cutoff
        node.cost = temp
        return temp

    elif max_min == 'min':
        temp = float('inf')
        for child in node.children:
            if child.min_max == 'max':
                child.cost = alpha_beta(child, alpha, beta, 'max')
                temp = min(temp, child.cost)
            else:
                child.cost = alpha_beta(child, alpha, beta, 'min')
                temp = min(temp, child.cost)
            beta = min(beta, temp)
            if beta <= alpha:
                node.pruned = 1
                break  # alpha cutoff
        node.cost = temp
        return temp


def alpha_beta(node, alpha, beta, max_min):
    if node.is_leaf == 1:
        return node.cost

    if max_min == 'max':
        temp = float('-inf')
        for child in node.children:
            if child.min_max == 'min':
                child.cost = alpha_beta(child, alpha, beta, 'min')
                temp = max(temp, child.cost)
            else:
                child.cost = alpha_beta(child, alpha, beta, 'max')
                temp = max(temp, child.cost)
            alpha = max(alpha, temp)
            if alpha >= beta:
                node.pruned = 1
                break  # beta cutoff
        node.cost = temp
        return temp

    elif max_min == 'min':
        temp = float('inf')
        for child in node.children:
            if child.min_max == 'max':
                child.cost = alpha_beta(child, alpha, beta, 'max')
                temp = min(temp, child.cost)
            else:
                child.cost = alpha_beta(child, alpha, beta, 'min')
                temp = min(temp, child.cost)
            beta = min(beta, temp)
            if beta <= alpha:
                node.pruned = 1
                break  # alpha cutoff
        node.cost = temp
        return temp


def print_state(state):
    s = state.copy()
    temp = s[7:13]
    temp.reverse()
    print('player -->', ' ', s[13], temp)
    print('computer --> ', '', s[0:6], s[6])


# print state at the begining
print_state(current_state)


while True:
    ended, who_win = is_end(current_state)
    if ended == 1:
        print('game ended\n and the result is -->', who_win)
        break
    if turn == 'min':
        user_move = int(
            input('it is your turn Enter a number from 1 to 6 or 0 to save and exit\n'))+6
        if user_move == 6:
            save.save(current_state, stealing)
            break

        valid_move, returned_state, next_turn = make_move(
            user_move, current_state)
        while valid_move == 0:
            user_move = int(
                input('this is not a valid move try again,  Enter a number from 1 to 6\n'))+6
            if user_move == 6:
                save.save(current_state, stealing)
                break
            valid_move, returned_state, next_turn = make_move(
                user_move, current_state)
        current_state = returned_state
        turn = next_turn
        print('this is your play')
        print_state(current_state)
        print("_________________________")
    else:
        print('this is my move')
        suggested_move = get_move(current_state)
        valid_move, returned_state, next_turn = make_move(
            suggested_move, current_state)
        current_state = returned_state
        turn = next_turn
        print_state(current_state)
        print("_________________________")
