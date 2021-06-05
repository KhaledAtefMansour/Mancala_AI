def is_end(state):
    s=state.copy()
    sum_max=0
    sum_min=0
    for i in range(0,6):
        sum_max+=s[i]
        sum_min+=s[i+7]
    if sum_max==0 :
        ended=1
        if s[6]>48-s[6]:
            who_win='computer winned'
        elif s[6]<48-s[6]:
            who_win='player winned'
        else:
            who_win='Draw'
    elif sum_min=0:
        ended=1
        if s[13]>48-s[13]:
            who_win='player winned'
        elif s[13]<48-s[13]:
            who_win='compuuter winned'
        else:
            who_win='Draw' 
    else:
        ended=0
    return ended,who_win 