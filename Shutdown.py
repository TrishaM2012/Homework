def shutdown(user_input):
    if user_input == "Yes":
        print("Shutdown activated")
    elif user_input == "No":
        print("Shutdown aborted")
    else:
        print("Sorry?")
response = input("Do you want to shut down? (Yes/No): ")

shutdown(response)