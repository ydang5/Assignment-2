def get_humidity_rating (humidity):

# humidity_input = int(input("please enter humidity"))
#
# humidity = humidity_input

    if humidity < 30:
        print("Dry")
    elif humidity > 60:
        print("High Humidity")
    else:
        print("Ok")
