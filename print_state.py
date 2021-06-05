def print_state(state):
    s=state.copy()
    temp=s[7:13]
    temp.reverse()
    print('player -->', ' ', s[13],temp)
    print('computer --> ', '', s[0:6],s[6])
  