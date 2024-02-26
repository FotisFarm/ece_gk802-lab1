import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = input("Please provide a url: ")  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    
    server = response.headers.get("Server")
    
    if server:
        print(f"The server is {server}")
    else:
        print("No server header.")
    
    cookies = response.headers.get("Set-Cookie")
    
    if cookies:
        print(f"The cookies are {cookies}")
    else:
        print("No \'Set-Cookie\' header.") 
           
    
    


#req = requests.get(url)

#headers = req.headers
#print(str(req.headers))

