try:
    age = int(input("I will recommend a type of movie depending on your age. Please enter your age: ")) 

    if age <= 13: 
        movie = input("What kind of movie do you like? I could recommend a movie of that type. Animation, Adventure, Family, Fantasy, Comedy: ").lower().strip("")
            
        if movie == "animation": 
            print("I recommend you Toy Story")
        elif movie == "adventure":  
            print("I recommend you The Gonnies")
        elif movie == "family": 
            print("I recommend you Paddington 2")
        elif movie == "fantasy": 
            print("I recommend you Harry Potter and the Sorcerer's Stone")
        elif movie == "comedy": 
            print("I recommend you Home Alone")
        else:
            print("That option is not available for your age.")

    else: 
        movie = input("What kind of movie do you like? I could recommend a movie of that type. Action, Drama, Science Fiction, Thriller, Romance: ").lower().strip("")

        if movie == "action": 
            print("I recommend you Mad Max: Fury Road")
        elif movie == "drama": 
            print("I recommend you The Pursuit of Happyness")
        elif movie == "scienceFiction": 
            print("I recommend you Interstellar")
        elif movie == "thriller": 
            print("I recommend you Gone Girl")
        elif movie == "romance": 
            print("I recommend you Pride & Prejudice")  
        else:
            print("That option is not available for your age.")  
except:
    print("It's not possible calculate your age, The ERROR is ValueError")            