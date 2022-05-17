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

        sorted_restaurant = sorted(restaurant_dict)

    # print(sorted_restaurant)

    for word in sorted_restaurant:
        if word in restaurant_dict:
            rest_s = word
            
            rate_s = restaurant_dict[word]
            print(f"{rest_s} is rated {rate_s}")

    for restaurant in restaurant_dict:
        user_rest_choice = input("Pick a restaurant: ")
        user_rest_rate = int(input("Give it a rating from 1 to 5: "))
        
        if user_rest_choice not in restaurant_dict:
            restaurant_dict[user_rest_choice] = user_rest_rate
            # Not sure how to make this work
  
    


restaurant_rating("scores.txt")
