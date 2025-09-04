# Text-Based Maze Navigator

""""
though process:
question explicitly requires nested dicts and not lists or sets

the maze will be 4 levels at most, each containing 3 rooms at most with the treasure being on the 4th level.

the descriptions print what other rooms are accessible from this room by getting values from dict, as well as objects in the room itself
I will build each level from separate dicts to reduce confusion
then use if-elif statements to dictate logic for directions of motion  R L F B
we ended up embedding the directions within the maze dict as well, just need to do something special for Backwards movement
The maze map will be constructed from the bottom up !
"""

L_0 = {"Starting Point":{"R":"Front Entrance","L":"Back Entrance","F":"Garden"}}

L_1= {
    "Front Entrance":{"R":"Living Room","L":"Bedroom","F":"Corridor"},
    "Back Entrance":{"R":"Dressing Room","L":"Guest Hall"},
    "Garden":{"R":"Garage","L":"Storage","F":"Pool"}
        }

L_2 = {"Living Room":"There is a tv and a couch, no other doors",
          "Bedroom":" 2 queen beds and a mirror, nothing more...",
          "Corridor":{"R":"Kids Room","L":"Bathroom"},
          "Dressing Room":"Just hangers and shelves full of clothes",
          "Guest Hall":"A large kitchen and 2 great dining tables",
          "Garage":"A few parked cars",
          "Storage room" :"Old power tools and gardening equipment",
          "Swimming Pool":"You are very far off, of course it isn't underwater!"
          }

L_3 = {
        "Kids Room":{"R":"Secret Door"},
        "Bathroom":"an ordinary bathroom...what did you expect"
        }

L_4 = {"Secret Door":"T Found"}

Maze = [L_0,L_1,L_2,L_3,L_4]



def check_room(cur_R :str = "Starting Point"):
    cur_P = ""
    print(cur_R)
    for level in Maze:
        if cur_P == "T Found":
            return cur_P, True
        if cur_R in list(level):
            cur_L= level
            index = Maze.index(cur_L)
            cur_P = cur_L[cur_R]
            
            print(cur_P)

            choice = input("Enter choice (R, L, F): ")
            if choice == "R":
                cur_R = cur_L[cur_R]["R"]
                print(cur_R)
                index+= 1
                cur_L = Maze[index]
                cur_P = cur_L[cur_R]

            elif choice == "L":
                cur_R = cur_L[cur_R]["L"]
                print(cur_R)
                index += 1
                cur_L = Maze[index]
                cur_P = cur_L[cur_R]

            elif choice == "F":
                cur_R = cur_L[cur_R]["F"]
                print(cur_R)
                index += 1
                cur_L = Maze[index]
                cur_P = cur_L[cur_R]
            
            elif choice == "B":
                cur_P = list(cur_L)         
    return cur_P,False


while True:
    _, success = check_room()
    if success:
        break
