from resource import resource_allocation

print("#######\n" +                                                         
"#     # #####  ###### #####    ##   ##### #  ####  #    #  ####\n"+  
"#     # #    # #      #    #  #  #    #   # #    # ##   # #\n"+      
"#     # #    # #####  #    # #    #   #   # #    # # #  #  ####\n"+  
"#     # #####  #      #####  ######   #   # #    # #  # #      #\n"+ 
"#     # #      #      #   #  #    #   #   # #    # #   ## #    #\n"+ 
"####### #      ###### #    # #    #   #   #  ####  #    #  ####\n"+  
"                                   \n" +                                                               
"######\n" +                                                   
"#     # ######  ####  ######   ##   #####   ####  #    #\n" + 
"#     # #      #      #       #  #  #    # #    # #    #\n" + 
"######  #####   ####  #####  #    # #    # #      ######\n" + 
"#   #   #           # #      ###### #####  #      #    #\n" + 
"#    #  #      #    # #      #    # #   #  #    # #    #\n" + 
"#     # ######  ####  ###### #    # #    #  ####  #    #\n")
print("Welcome to Operations Researcher's helper!")
print("INFO: this helper allows you to solve\nResource Allocation Problem (alias: capital budgeting), use command: R\n\
Workforce size problem, use command: W\nTo end the program, use command: Q\nTo Print info again, use command: I")

while True:
    print()
    x = input("please enter command: ")
    print()
    if x == "Q":
        print("Bye~")
        break
    if x == "I":
        print("INFO: this helper allows you to solve\nResource Allocation Problem (alias: capital budgeting), use command: R\n\
Workforce size problem, use command: W\nTo end the program, use command: Q\nTo Print info again, use command: I")
    if x == "R":
        resource_allocation()

