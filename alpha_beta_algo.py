def alpha_beta (node, alpha, beta, max_mini) :
    if  node.leaf ==1 :
        return node.cost

    if max_mini =='max':
        temp  = float('-inf')
        for  child in node.children :
			if child.mini_max == 'min':
                child.cost=alphabeta(child, alpha, beta, 'min')
            	temp  = max(temp, child.cost)
			else:
                child.cost=alphabeta(child, alpha, beta, 'max')
				temp  = max(temp,child.cost)
				
            alpha  = max(alpha, temp)
            if alpha >= beta :
                child.pruned=1
                break  #beta cutoff 
        return temp

    elif max_min =='min':
        temp  = float('inf')
        for child in node.children :
			if child.mini_max == 'max':
                child.cost = alphabeta(child,alpha, beta, 'max')
            	temp  = min(temp,child.cost)
			else:
                child.cost = alphabeta(child,alpha, beta, 'min')
				temp  = min(temp, child.cost)
            beta   = min(beta, temp)
            if beta <= alpha :
                child.pruned=1
                break  #alpha cutoff
        return temp
