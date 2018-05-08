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



### Creating hashtag dictionary

def count_all_hashes(table):

    ### PSEUDOCODE 
    import re
    # initialize empty list of hashes
    all_hashes = {}  # starts out empty
    
    # use to detect hashtags 
    # hash_pat = r'[#][^\s#\W]+'# any expression starting with '#' 
                                # and not containing a whitespace character '\s' or '#'   
                                # is finding too many patterns... improve
                                # potentially an issue with hash pattern also listing emoji hashes as distinct

    hash_pat = r'[#][^\s#\W]+' 

    # index/loop through rows
    for i in range(0,len(table)):
        
        # get row tweet data and label
        row = table.iloc[i]
        tweets = row['tweet'] # need to know these column names as data
        label = row['label']
        

        # for each row, parse ['tweet'] for # patterns using hash_pat
        # which returns a list of patterns
        # import re required

        hashes = re.findall(hash_pat, tweets) # can wrangle to lowercase but apparently they're already filtered to lowercase

        # add each pattern to all_hashes_test 
        # and increment existing [hater,non-hater] index for each item based on ['counter'] value from row
        for x in hashes:
            if x not in all_hashes:
                all_hashes[x] = [1-label,label] # [non-hater, hater], 
                                                # label = 0 -> non-hater, = 1 -> hater
            else:
                all_hashes[x][label] += 1 # increment - [label]=[0 or 1st index] picks out hater/non by label

    return all_hashes


### Cosine Similarity

# define dot product
def dot_product(v1,v2):
    # check similar type
    if len(v1) != len(v2):
        return("vectors are not compatible lengths")
    else:
        
        products = []
        for i in range(0, len(v1)):
            products.append(v1[i]*v2[i])
        dot_product = sum(products)

        return(dot_product)

# compute cosine similarity
def cosine_similarity(v1,v2):
    
    # check similar type
    if len(v1) != len(v2):
        return("vectors are not compatible lengths")
    else:

        # compute similarity
        return dot_product(v1,v2) / ((dot_product(v1,v1)**.5) * (dot_product(v2,v2)**.5))
