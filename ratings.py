"""Restaurant rating lister."""


# put your"""Restaurant rating lister."""

def restaurant_rating(file):
    rating_text= open(file)

# need to split text into list

    restaurant_dict= {}
    
    for line in rating_text:
        lin = line.rstrip()
        line = lin.split(":")
        #print(line)

        restaurant = line[0]
        rating = int(line[1])    
        
        restaurant_dict[restaurant] = rating 
        sorted_rest_ratings= {}
    # print(restaurant_dict)

    sorted_rest_ratings = sorted(restaurant_dict.items())


    print(f"{(sorted_rest_ratings[0])} is rated {(sorted_rest_ratings[1])}.")
  
        #restaurant_rating= {}

    # line.sort()
        # print(line)
#sort each line
# we take each restaurant name and rate
# "restaurant nam is rated "rate"
#['Jellied Eel Shop', '3'] each item index [0] we just gonna sort
#  for word in word_count:
 #       print(word, word_count[word]) 



restaurant_rating("scores.txt")
