

from easygui import *
import sys


while 1:
    msgbox("would u like to shop")

    msg ="Which is ur favourite site"
    title = "shopping sites"
    choices = ["Flipkart", "amazon", "myntra"]
    choice = choicebox(msg, title, choices)
   
     if choices=="Flipkart":
           choices1=["Shirts","Jeans","T-Shirt"]
            choice = choicebox(msg, choices)
    msgbox("you chose: "  + str(choices1),"your result")
      
      if choices1=="Jeans":
                  choices2=["allen solly","LP","gap"]
                  choices1=choicebox(msg,choices)    
    msgbox("you chose: "  + str(choices1),"your result")
            
    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)


