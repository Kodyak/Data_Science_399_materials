# my library of useful python functions

### for KNN

def top_k(table, features, target_row_id, k, metric):

    all_distances = []
    
    for i in range(0,len(table)):
        if(i != target_row_id):
            distance = metric( table.loc[i, features],table.loc[target_row_id, features] )
            all_distances.append( (i,distance) )
            
    all_distances.sort(key=lambda x: x[1]) # sorts by distance (increasing)
    
    return [all_distances[i] for i in range(0,k)] # culls smallest k


def knn_voting(table, target_column, topk_rows):

    # Get row ids from topk
    row_ids = []
    for i in range(0,len(topk_rows)):
        row_ids.append(topk_rows[i][0])
    
    # Get votes
    votes = table[target_column][row_ids]
    
    # compute majority indirectly using average
    if sum(votes) > len(votes)/2:
        return 1
    else:
        return 0

    # floating point alternative
    # return round(sum(votes)/len(votes))