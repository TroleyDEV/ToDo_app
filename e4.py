import webbrowser

user_term = input("Enter a search tern: ").replace(" ", "+")

webbrowser.open("https://google.com/search?q=" + user_term)
