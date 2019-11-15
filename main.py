import time
is_thinking = input("Is Fish Thinking? ")
if is_thinking.lower() == "yes":
    for i in range(3):
        if i == 0:
            print("""
                    
                |\   \\\\__     o
            | \_/    o \    o 
            > _   (( <_  oo  
            | / \__+___/      
            |/     |/
            
            thinking...         
            """)
            time.sleep(3)
        elif i == 1:
            print("""
                    
                    |\   \\\\__     o
                | \_/    o \    o 
                > _   (( <_  oo  
                | / \__+___/      
                |/     |/
                
            thinking...         
            """)
            time.sleep(3)
        elif i == 2:
            print("""
                                    
                                    |\   \\\\__     o
                                | \_/    o \    o 
                                > _   (( <_  oo  
                                | / \__+___/      
                                |/     |/
                                
            thinking...         
            """)
            time.sleep(3)
    print("fish has thought")
else:
    print("...")
    time.sleep(2)
    print("""


           .'|_.-
         .'  '  /_
      .-"    -.   '>
   .- -. -.    '. /    /|_
  .-.--.-.       ' >  /  /
 (o( o( o )       \_."  <
  '-'-''-'            ) <
(       _.-'-.   ._\.  _\
 '----"/--.__.-) _-  \|


 fish is dumb
    """)
