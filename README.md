# Robot-Simulator
The application is a simulation of a toy robot moving on a square tabletop, of
dimensions 5 units x 5 units.
There are no other obstructions on the table surface.
The robot is free to roam around the surface of the table and is prevented
from falling to destruction. Any movement that would result in the robot falling from
the table is prevented.

### Code execution
Before executing the code install the dependencies mentioned in requirements.txt. Code can be executed in two ways depending on the input format.
1) For input directly in the command line type the following in cmd, you will be prompted to enter the commands
   ```sh
   python robot.py

2) For executing inputs from a file use the following command. "test_case_1.txt" is the default text file included and can be used to write new chain of commands.
   ```sh
   python robot.py --file test_case_1.txt

3) Use the following command to execute the test cases. Use the function signature 'test_custom_commands' in the 'test.py' to write additional test cases.
   ```sh
   pytest test.py

  ### Features and Functionality
  1) Have added a new command "Exit" which can be used to exit out of the command line input. Having this "Exit" option allows use to use the "Report" command 
     multiple times in the chain to see where the Robot is currently.
  2) Have added functionality to handle both upper and lower cases in the commands.
  3) Have added additional checks for the "PLACE" command which includes number checking, null value checking, and handles uneven spaces within the command. For e.g.
     "PLACE 0,0,NORTH", "PLACE  0, 0, NORTH", and "Place, 0,0,North" will be handled in a similar way.
  4) Inputs can be provided from both command line and text file.

      | Function   | Description  |
      |-----------|-----------|
      | place | Places the robot within the constraints |
      | move | Moves the robot in the facing direction by 1 unit |
      | left | Turns the robot to the left |
      | right | Turns the robot to the right |
     | report | Reports the current coordinates if the robot is placed |
     | execute_command | Checks if the command is valid and executes |

   ### Examples
   The following inputs in the command line will produce the output "Robot is currently at coordinate (3,3) facing NORTH."
   ```sh
   PLACE 1,2,EAST
   MOVE
   MOVE
   LEFT
   MOVE
   REPORT

