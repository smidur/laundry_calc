import re
import time

author_text = """
# ##################################################################################
# #  ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗██████╗     ██████╗ ██╗   ██╗ #
# # ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝ #
# # ██║     ██████╔╝█████╗  ███████║   ██║   █████╗  ██║  ██║    ██████╔╝ ╚████╔╝  #
# # ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝   #
# # ╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗██████╔╝    ██████╔╝   ██║    #
# #  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝     ╚═════╝    ╚═╝    #
# #                                                                                #
# # ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗    ██╗   ██╗                    #
# # ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║    ██║   ██║                    #
# # ██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║    ██║   ██║                    #
# # ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║    ╚██╗ ██╔╝                    #
# # ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║     ╚████╔╝██╗                  #
# # ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═══╝ ╚═╝                  #
# ##################################################################################
# ############################################
# # ┌─┐ ┬┌─ ┌─┐   ┌─┐  ┌┬┐  ┬  ┌┬┐  ┬ ┬  ┬─┐ #
# # ├─┤ ├┴┐ ├─┤   └─┐  │││  │   ││  │ │  ├┬┘ #
# # ┴ ┴o┴ ┴o┴ ┴o  └─┘  ┴ ┴  ┴  ─┴┘  └─┘  ┴└─ #
# ############################################
#..License: CC BY-ND 4.0 (Creative Commons: Attribution-NoDerivatives 4.0 International)
#....Email: vromabz@gmail.com
#...Github: https://github.com/smidur
#.Telegram: https://t.me/readme321
"""
print(author_text)

quit_cup = """
                                                                           
                      ▒░                             ░░                    
                    █▒░░▒▓▒▓████████████████████▓░░░░ ░██                  
                    █                                 ▓░                  
                    █▓                                █                   
              █████ ▒▒                                █                   
                  ▓ ▒▒                                █                   
           █  ▓     ██  ▓  ░░                         █                   
          ██ █      ▓█         ▓▒▒░░░ ░ ░░░           █                   
          ▓  █      ▒█▒▒▓▒████▒▒▒▒▒▓▓▓▓▓▓▓▓▓███▓█████░▒                   
             ▒▓      █▒████████████████████████████████                    
            ▓   ▒    ▒▓█▒██████████████████████████████                    
              ███  ░ ▒ ░ ░██▓▓▓▓▓███████████▓▓▓▓▓█▓▒▓▓█    ░░              
           ░▒░     ▒ ███  ▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▒▓█         ▒░░        
       ░▒▓▒▒░░░░░░░  ██▓▒▒▓█▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▒█▓          ░░ ▒      
      █   ░░░░░░░░░  ███░▒▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒░▓▒██      ░░░      ▒    
       █▓▒▒░  ░░░░░░  ▓█▓░▓█████████▓▓▓▓▓▓▓███▓█▓█████  ░░░░░      ░██     
          ▓▒▓░          ▒█▓▒░░░▒▓▓▓▓██████▓▓▓▓▓▓███           ░████        
             ███████████  ███████████████████████░▓░▒█████████▒            
                 ▓███▒░▒▒▒         ░░ ░▒▓▒▒░       ██▓░░                   
                       ▒▓████▓▓▓██▓  ██  ░ ░██▓██▒░       ░░░░░░           
                             ▒▒▒▒▓██▓▒▓▓████████    ░░░░                   
                  Чай дохлёбываем и у*бываем! (с)Аннушка\n
"""

quit_text0 = "If you want to quit the app, type 'q' or 'quit'"
quit_text1 = "Чай дохлёбываем и у*бываем! (с)Аннушка\n"
quit_text2 = "Auf wiedersehen, бл*ть! (c)Аннушка\n"


def check_quit(text: str):
    match text:
        case "q":
            print(quit_cup)
            time.sleep(4)
            exit(0)
        case "quit":
            print(quit_cup)
            print(quit_text2)
            time.sleep(4)
            exit(0)


num_pattern = re.compile(r'[0-9]+[,.][0-9]*|[0-9]+')
quit_pattern = re.compile(r'q|quit')

print("Welcome! Let us start!")
print(quit_text0)

while True:
    try:
        vat_str = input('Type the VAT: ')
        check_quit(vat_str)
        vat_re = re.search(num_pattern, vat_str).group()
        vat_re = float(vat_re)
        vat = vat_re / 100.0 + 1.0

        rate_str = input('Type the rate: ')
        check_quit(rate_str)
        rate_re = re.search(num_pattern, rate_str).group()
        rate = float(rate_re)

        print()
        print(f"VAT set as: {vat_str}%")
        print(f"Rate set as: {rate_str} (ILS for 1 USD)")
        print()
        break
    except AttributeError:
        print("You entered incorrect RATE/VAT or mistyped somewhere!")
        print(quit_text0)
        continue

while True:
    try:
        value_str = input("Type the cost from the sheet: ")
        check_quit(value_str)
        value_re = re.search(num_pattern, value_str).group()
        value = float(value_re)

        cost_no_vat = value / vat / rate
        cost_vat = value / rate

        cost_no_vat = round(cost_no_vat, 2)
        cost_vat = round(cost_vat, 2)

        print("{:>20s} | {:.2f}".format("In USD:", cost_vat))
        print("Cost without VAT is: | {:.2f}".format(cost_no_vat))
        print()

    except AttributeError:
        print("You entered incorrect VALUE or mistyped somewhere!")
        print(quit_text0)
        continue
