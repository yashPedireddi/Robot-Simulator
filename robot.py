import sys
import argparse
from typing import Union

class Robot:
    def __init__(self):
        """
        Initializing coordinates to None and placed status to False.
        Initializing possible directions robot can face
        """
        self.x = None
        self.y = None
        self.facing = None
        self.directions = ["north", "east", "south", "west"]
        self.placed = False

    def place(self, x: int, y: int, facing: str) -> None:
        """
        Checking the coordinates and facing constraints, initializing the coordinates, and updating placed status
        """
        if 0 <= x < 5 and 0 <= y < 5 and facing.lower() in self.directions:
            self.x = x
            self.y = y
            self.facing = facing.strip().lower()
            self.placed = True

    def move(self) -> None:
        """
        Checking the placed status and moving the robot by 1 unit in the current direction.
        """

        if not self.placed:
            return
        if self.facing == "north" and self.y < 4:
            self.y += 1
        elif self.facing == "east" and self.x < 4:
            self.x += 1
        elif self.facing == "south" and self.y > 0:
            self.y -= 1
        elif self.facing == "west" and self.x > 0:
            self.x -= 1

    def left(self) -> None:
        if not self.placed:
            return
        self.facing = self.directions[(self.directions.index(self.facing) - 1) % 4]
    
    def right(self) -> None:
        if not self.placed:
            return
        self.facing = self.directions[(self.directions.index(self.facing) + 1) % 4]

    def report(self) ->str:
        if self.placed:
            return f"Robot is currently at coordinate ({self.x},{self.y}) facing {self.facing.upper()}."
        else:
            return "Robot not placed on the table."
        
    def execute_command(self, command: str) -> Union[str, None]:
        """
        Execute a command to control the robot.
        This method parses the input command string and handles various cases,
        including the PLACE command with checks for numeric values, presence of
        necessary parameters, and handling of uneven spaces.
        """
        parts = command.strip().split(",")

        if len(parts) ==3 and parts[0].strip().split(" ")[0].lower() == "place" :
            x, y, facing = parts[0].strip().split(" ")[1], parts[1].strip(), parts[2].strip()
            if not x or not y or not facing:
                return "Invalid command." 
            if  not x.isdigit() or not y.isdigit():
                return "Invalid command."
            self.place(int(x), int(y), facing)
        elif parts[0].strip().lower() == "move":
            self.move()
        elif parts[0].strip().lower() == "left":
            self.left()
        elif parts[0].strip().lower() == "right":
            self.right()
        elif parts[0].strip().lower() == "report":
            return self.report()
        else:
            return "Invalid command."
        
if __name__ == "__main__":

    robot = Robot()
    
    parser = argparse.ArgumentParser(description="Mars Rover Robot")
    parser.add_argument('--file', type=argparse.FileType('r'), help="Input file containing commands on separate lines")
    args = parser.parse_args()

    if args.file:
        commands = args.file.readlines()
        for command in commands:
            if command.lower() == "exit":
                break
            output = robot.execute_command(command.strip().lower())
            if output:
                print(output)
    
    else :
        print("Enter commands (type 'EXIT' to stop):")
        while True:
            line = input().strip().lower()

            # UNCOMMENT/COMMENT BELOW 2 LINES OF CODE TO INTRODUCE/REMOVE EXIT COMMAND AND KEEP RUNNING THE PROCESS EVEN AFTER EXECUTING REPORT COMMAND
            if line.lower() == "exit":
                break
            # COMMENT/UNCOMMENT BELOW 4 LINE AND UNCOMMENT ABOVE 2 TO INTRODUCE/REMOVE EXIT COMMAND
            # if line.lower() == "report":
            #     output = robot.execute_command(line)
            #     print(output)
            #     break
            output = robot.execute_command(line)
            if output:
                print(output)

    