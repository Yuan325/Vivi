import webbrowser
import wikipedia

# code retrieved and modified from https://www.geeksforgeeks.org/build-a-virtual-assistant-using-python/

def Take_query(): 
    if "open geeksforgeeks" in query: 
        speak("Opening GeeksforGeeks ") 
          
        # in the open method we just to give the link 
        # of the website and it automatically open  
        # it in your default browser 
        webbrowser.open("www.geeksforgeeks.com") 
        continue
      
    elif "open google" in query: 
        speak("Opening Google ") 
        webbrowser.open("www.google.com") 
        continue
      
    elif "from wikipedia" in query: 
          
        # if any one wants to have a information 
        # from wikipedia 
        speak("Checking the wikipedia ") 
        query = query.replace("wikipedia", "") 
          
        # it will give the summary of 4 lines from  
        # wikipedia we can increase and decrease  
        # it also. 
        result = wikipedia.summary(query, sentences=4) 
        speak("According to wikipedia") 
        speak(result)
