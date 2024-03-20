import time

books = {}

books["Classic"] = {1:{"Title":"To Kill a Mockingbird","Author":"Harper Lee","Issued":False}, 2:{"Title":"1984","Author":"George Orwell","Issued":False}, 3:{"Title":"The Great Gatsby","Author":"F. Scott Fitzgerald","Issued":False}, 4:{"Title":"The Catcher in the Rye","Author":"J.D. Salinger","Issued":False}, 5:{"Title":"Pride and Prejudice","Author":"Jane Austen","Issued":False}}

books["Historic"] = {1:{"Title":"The Histories","Author":"Herodotus","Issued":False}, 2:{"Title":"The Guns of August","Author":"Barbara W. Tuchman","Issued":False}, 3:{"Title":"The Rise and Fall of the Third Reich","Author":"William L. Shirer","Issued":False}, 4:{"Title":"A People's History of the United States","Author":"Howard Zinn","Issued":False}, 5:{"Title":"The Decline and Fall of the Roman Empire","Author":"Edward Gibbon","Issued":False}}

books["Thriller"] = {1:{"Title":"Gone Girl","Author":"Gillian Flynn","Issued":False}, 2:{"Title":"The Girl with the Dragon Tattoo","Author":"Stieg Larsson","Issued":False}, 3:{"Title":"The Silence of the Lambs","Author":"Thomas Harris","Issued":False}, 4:{"Title":"The Da Vinci Code","Author":"Dan Brown","Issued":False}, 5:{"Title":"The Bourne Identity","Author":"Robert Ludlum","Issued":False}}

books["Science Fiction"] = {1:{"Title":"Dune","Author":"Frank Herbert","Issued":False}, 2:{"Title":"Neuromancer","Author":"William Gibson","Issued":False}, 3:{"Title":"Foundation","Author":"Isaac Asimov","Issued":False}, 4:{"Title":"Snow Crash","Author":"Neal Stephenson","Issued":False}, 5:{"Title":"The Hitchhiker's Guide to the Galaxy","Author":"Douglas Adams","Issued":False}}

books["Mystery"] = {1:{"Title":"And Then There Were None","Author":"Agatha Christie","Issued":False}, 2:{"Title":"The Murder of Roger Ackroyd","Author":"Agatha Christie","Issued":False}, 3:{"Title":"The Hound of the Baskervilles","Author":"Arthur Conan Doyle","Issued":False}, 4:{"Title":"The Big Sleep","Author":"Raymond Chandler","Issued":False}, 5:{"Title":"In the Woods","Author":"Tana French","Issued":False}}

books["Psychological Thriller"] = {1:{"Title":"The Girl on the Train","Author":"Paula Hawkins","Issued":False}, 2:{"Title":"The Silent Patient","Author":"Alex Michaelides","Issued":False}, 3:{"Title":"Before I Go to Sleep","Author":"S.J. Watson","Issued":False}, 4:{"Title":"Sharp Objects","Author":"Gillian Flynn","Issued":False}, 5:{"Title":"The Talented Mr. Ripley","Author":"Patricia Highsmith","Issued":False}}


while True:
    print("A Library Management System")
    print("\n")

    #displaying the list of genres
    print("Available genres:")
    i = 1
    for genre in books:
        print("{}.{}".format(i, genre))
        i += 1

    #choosing the genre
    while True:
        genre_no = int(input("Enter the genre number: "))
        chosen_genre = ""
        
        j = 1
        for genre in books:
            if j == genre_no:
                chosen_genre = genre
                break
            j += 1

        if chosen_genre == "":
            print("Invalid input") 
        else:
            break


    print("\n\n\n")


    #displaying the list of books
    print("Sr.no\t\tBook title - Author\n")

    for i in books[chosen_genre]:
        title = books[chosen_genre][i]["Title"]
        author = books[chosen_genre][i]["Author"]
        print("{}\t\t{} - {}".format(i,title,author))


    print("\n")


    #issuing
    book_no = int(input("Enter Sr.no of the book you want to issue:"))
    issue_status = books[chosen_genre][book_no]["Issued"]
    if issue_status == False:
        print("Successfully issued!")
        print("Enjoy reading and don't forget to bring it back next week :)")
        books[chosen_genre][book_no]["Issued"] = True
    else:
        print("Oops! The book you're looking for has already been issued.")
        print("Try picking another one :)")
    
    time.sleep(5)
    print("\n\n")
