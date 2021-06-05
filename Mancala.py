

class Mancala():
    """docstring for Mancala"""
    def __init__(self, Initial_State = None,is_Stealing = True, turn = 'max'):
        super(Mancala, self).__init__()
        self.state = []
        if Initial_State is None:
            self.state = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
        else:
            self.state = Initial_State

        self.Stealing = is_Stealing
        self.turn = turn
        self.valid_move = True

    def print(self):
        print('Game_state is : ', self.state )
        print('Next turn is : ', self.turn)

    def move(self,selected_place):
        num_of_stones = self.state[selected_place]
        if num_of_stones==0 or selected_place not in range(0,13) :
            self.valid_move = False

        self.turn = 'min' if selected_place in range(0,6) else 'max'

        next_state = self.state.copy()
        next_state[selected_place] = 0
        place_to_add_stone = selected_place + 1
        
        Capture_pit = 6 if self.turn == 'min' else 13
        Other_Capture_pit = 13 if self.turn == 'min' else 6
        while True:
            if num_of_stones == 0 : break
            
            if num_of_stones == 1 :

                if self.Stealing == True and next_state[place_to_add_stone] == 0 and self.state[12-place_to_add_stone] != 0 :                    
                    next_state[Capture_pit] += next_state[12 - place_to_add_stone] + 1
                    next_state[12 - place_to_add_stone] = 0
                    break
                
                if place_to_add_stone == Capture_pit and self.turn == 'min':
                    self.turn = 'max'
                if place_to_add_stone == Capture_pit and self.turn == 'max':
                    self.turn = 'min'
            
            if place_to_add_stone != Other_Capture_pit:
                next_state[place_to_add_stone] += 1
                num_of_stones -= 1


            place_to_add_stone = (place_to_add_stone + 1) % 14

        return Mancala(next_state, self.Stealing, self.turn)
