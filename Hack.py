import os
import time
import sys


def title():
    print("""
#############################################################
#############################################################
███╗   ███╗██╗██╗     ██╗████████╗███████╗ ██████╗██╗  ██╗
████╗ ████║██║██║     ██║╚══██╔══╝██╔════╝██╔════╝██║  ██║
██╔████╔██║██║██║     ██║   ██║   █████╗  ██║     ███████║
██║╚██╔╝██║██║██║     ██║   ██║   ██╔══╝  ██║     ██╔══██║
██║ ╚═╝ ██║██║███████╗██║   ██║   ███████╗╚██████╗██║  ██║
╚═╝     ╚═╝╚═╝╚══════╝╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝
                                                                 
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗███████╗
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔════╝
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║███████╗
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════██║
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║███████║
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝
#############################################################
#############################################################
""")                                                  

#begin hack
title()
start = input("Would you like to enter system? (Y/N)")
if start.lower().strip() == "y":
    print("Compiling Systems...")
    time.sleep(5)
    os.system("clear")
    floorOne = input("Unauthorized connection to Level 1. There is XXX on this floor please consult the admin if you are not authorized to access this terminal. Please Input the admin password  and press ENTER to continue:")
    if floorOne.lower().strip() == "12345":
        os.system("clear")
        print("Compiling Systems...")
        time.sleep(5)
    else:
        os.system("clear")
        title()
        print ("Connection has been severed. Please consult your admin.")
        sys.exit()
    floorTwo = input("Unauthorized connection to Level 2. There is XXX on this floor please consult the admin if yo are not authorized to access this terminal. Would you like to continue? (Y/N)")   
    if floorTwo.lower().strip() == "y":
        os.system("clear")
        print("Compiling Systems...")
        time.sleep(5)
    else:
        os.system("clear")
        title()
        print ("Connection has been severed. Please consult your admin.")
        sys.exit()
    floorThree = input("Unauthorized connection to Level 3. There is XXX on this floor please consult the admin if yo are not authorized to access this terminal. Would you like to continue? (Y/N)")
    if floorThree.lower().strip() == "y":
        os.system("clear")
        print("Compiling Systems...")
        time.sleep(5)
    else:
        os.system("clear")
        title()
        print ("Connection has been severed. Please consult your admin.")
        sys.exit()
    os.system("clear")
    finalFloor = input("Please input the final password to decrypt the content.")
    if finalFloor.lower().strip() == "password":
        title()
        print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Sapien nec sagittis aliquam malesuada bibendum arcu vitae. Turpis egestas maecenas pharetra convallis posuere morbi. 
        Elit ut aliquam purus sit amet luctus venenatis. At imperdiet dui accumsan sit amet nulla facilisi morbi. 
        Tempor nec feugiat nisl pretium fusce id velit ut tortor. Vitae purus faucibus ornare suspendisse sed nisi lacus sed viverra. 
        Tristique nulla aliquet enim tortor at auctor urna nunc. Maecenas volutpat blandit aliquam etiam erat velit. 
        Vulputate sapien nec sagittis aliquam malesuada bibendum arcu vitae elementum. Sit amet mauris commodo quis imperdiet massa tincidunt.""")
    else:
        print("""eRSpzhEBbzOWMPgQJlOSye45XKa9ITM0IZMHntdBEy5PEqH2T7U2R/9n4mV8KfMrJWz5lp0cICExMiH1+92NBual41n+S4xtITEwIQe+BURzraibk4u6l26xRgTBHP0p06qaE
        T+7eU0BWfXoM+zJReY0nSb0h0oYZfV/lLzjHxQ9gzVIptjPITMzIawhMCFkz8qOhmHtbow44NohMzkhXkaBq+vRutwxqtZjimnHYB3k7eeuFCEzNCH5YSExMSE9ifIhMTMhFmuLOeC7NJ4
        /QuqU1Fw2+O2hQDxKWVw8UrjyRML+SMg/TvOHW8LXwfMx7yExMyFFO0poeihcITMzIUxIrq4hMzkhm4Z4ZyDHU7j1wfo50/gccGAhMTAhphKxcRFtwDE0rRjPz77hqVw2+ylEgS1T6Yf8
        FkNvgMzKbvROiL4hMzQhITExIZ9LbO5HYiz6oWnzh8SG6bFsvKTFYHbQITEyIarr0S2rdlb/qLaS9tuYc6QIs2lGITM5Iab22T0Owc2qznZrWwgcD+khMzQhb87Cjt9Kf23Fn3aR0XvtITEy
        IRVwEhdrE8ncrMWrdT7o5CvV5u5kodtYM8ibPkKwfPEhMTMh+zy26rS3NN/W+xymYEkwe5cjS24+BJjmsD/cM2wjoWePS4ngMSh7WWMvOKW77IdOGL/Ij+z0zUvqQ4eCv263v/aeuxvlra5EZ
        T68iotOcOphybdZ3pAlFKaTPdz0kpvF1/ckiRF7E8QuuEN3ro4hOSH3W16cBwfAEBX1BPnofCExMSHsgrgWRurmLXljriEwIc6E/846JomX499s1V1lcUzh8iSKZ83AXMI1GOvGUBuC62khMTAh
        co54py9D1/pOBeipWqM1g1dkjlXBwlrz7uWL8xkmbwjadOHL132JE2cVphPIbS3sXUx8wbVldkzwP9w/n4X/zQ8UITM0Idkoa5DxdOT9dKdEN0Ekm79+M3prtz4hOSGqq9js7Bu/SubExf3DKXTGs
        KEbNk/OQq9O2+DuGQhkvynuGcGJqkWyPGC4kl59B4DYuuhLe89nYMoy9LkhMTYwIY/H6k7kV8qqITE2MCGRITExIZ4jR3EyNCExMCEFkssaulqIGkgr5bo1etII3lIq1l6F+8W2eMDaQmzEUPO7igiqI
        TM5IV8QM2/pEP2oITM5IQS22Igg40sgMUZE+ZSIqiExNjAhkSExMSGeI0dxyYYVMPr7yKYexKGxaCMGaOfkr/3FnyMo3ovYryjKr8TFJWzb9FLNhdmu3V2fdQdzrCExNjAhjp3qlnCG6FXYlKpqqx
        CqITM0IS+RMISwcCxt2FTwkoTO6cDmc5/oriEzMyHMgekhMTIhL9yvXqU08Xf64yuuVGLz1H77FLoDOOiQBIX2fg==""")
    title()
    
else:
    os.system("clear")
    title()
    print("Please secure all doors when exiting the room.")
    time.sleep(5)