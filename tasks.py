import webbrowser
# code retrieved and modified from https://www.geeksforgeeks.org/build-a-virtual-assistant-using-python/

def take_query(action, parameter): 
    if (action == "tasks.website"):
        parameter = parameter.get('domain').string_value
        string = "https://www." + parameter + ".com"
        print(string)
        webbrowser.open_new_tab(string)

    elif (action == "tasks.search"):
        parameter = parameter.get('query').string_value
        webbrowser.open_new_tab(parameter)

    else:
        return
