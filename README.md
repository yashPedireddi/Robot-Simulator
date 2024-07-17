# Robot-Simulator
Robot simulator

### Code execution
Code can be executed in two ways depending on the input format
1) For input directly in the command line type the following in cmd, you will prompted to enter the commands
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

