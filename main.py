from modules import weather,calculator,converter

Input = input("How can i help you(type h for help): ")
if( Input == "h"):
    print("Available feature ")
    print("1. Weather check : syntax => weather <city>")
    print("2. Calculator : syntax => ")
    print("3. Take notes : syntax => note add/delete/edit <notes Name>,")
    print("4. Converter : syntax => convert <quantity1> to <quantity2>")
    print("5. Reminder : syntax => reminder <Event> <time> ")

InputList = Input.split() 
if InputList[0] == "weather":
    weather.get_weather(InputList[1])

elif InputList[0] == "calculator":
    calculator.calci()


elif InputList[0] == "convert":
    converter.get_converting()

elif InputList[0] == "notes":
    print("abc")
    # if(InputList[1] == "add"):
    #     # adding stuff
    # if(InputList[1] == "delete"):
    #     # delete stuff
    # if(InputList[1] == "edit"):
    #     # editing stuff


elif InputList[0] == "reminder":
    print("abc")
    # reminder stuff
else :
    print("Please use some valid command (press h for help)")
