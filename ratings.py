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

        sorted_restaurant = sorted(restaurant_dict.items())

    # print(sorted_restaurant)

    # when you sort a dictionary it becomes a list of tupules(key, value) that you have to unpack
    for rest, rate in sorted_restaurant:
        # rest is the key and rate is the value
        print(f"{rest} is rated {rate}")
            
    # # could also not split restaurant_dict into items(tupules) and iterate through the sorted keys instead
    # for word in sorted_restaurant:
    #     if word in restaurant_dict:
    #         rest_s = word
            
    #         rate_s = restaurant_dict[word]
    #         print(f"{rest_s} is rated {rate_s}")

    # for restaurant in restaurant_dict:
    #     user_rest_choice = input("Pick a restaurant: ")
    #     user_rest_rate = int(input("Give it a rating from 1 to 5: "))
        
    #     if user_rest_choice not in restaurant_dict:
    #         restaurant_dict[user_rest_choice] = user_rest_rate
            # Not sure how to make this work

    
        # sorted_rest_ratings = sorted(restaurant_dict.items())

    # print(sorted_rest_ratings)


     



        #     print(f"{rest} is rated {rate}")
        
    # print(restaurant_dict)

        # 

    # print(sorted_rest_ratings)
        
        # for i, item in sorted_rest_ratings:
        #     rest_s = item[i][0]
        #     rate_s = item[1]


        # print(f"{rest_s} is rated {rate_s}.")
  
    


restaurant_rating("scores.txt")
