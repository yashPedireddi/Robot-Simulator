import pytest
from robot import Robot

@pytest.fixture
def robot():
    return Robot()

def test_initial_placement(robot):
    robot.execute_command("PLACE 0,0,NORTH")
    assert robot.report() == "Robot is currently at coordinate (0,0) facing NORTH."


def test_invalid_placement(robot):
    robot.execute_command("PLACE 5,5,NORTH")
    assert robot.report() == "Robot not placed on the table."

def test_movement(robot):
    robot.execute_command("PLACE 0,0,NORTH")
    robot.execute_command("MOVE")
    assert robot.report() == "Robot is currently at coordinate (0,1) facing NORTH."

def test_left_rotation(robot):
    robot.execute_command("PLACE 0,0,NORTH")
    robot.execute_command("LEFT")
    assert robot.report() == "Robot is currently at coordinate (0,0) facing WEST."

def test_right_rotation(robot):
    robot.execute_command("PLACE 0,0,NORTH")
    robot.execute_command("RIGHT")
    assert robot.report() == "Robot is currently at coordinate (0,0) facing EAST."

def test_prevent_fall(robot):
    robot.execute_command("PLACE 0,0,SOUTH")
    robot.execute_command("MOVE")
    assert robot.report() == "Robot is currently at coordinate (0,0) facing SOUTH."

def test_ignore_commands_before_place(robot):
    robot.execute_command("MOVE")
    robot.execute_command("LEFT")
    assert robot.report() == "Robot not placed on the table."
    robot.execute_command("PLACE 1,2,EAST")
    robot.execute_command("MOVE")
    assert robot.report() == "Robot is currently at coordinate (2,2) facing EAST."

def test_multiple_commands(robot):
    robot.execute_command("PLACE 1,2,EAST")
    robot.execute_command("MOVE")
    robot.execute_command("MOVE")
    robot.execute_command("LEFT")
    robot.execute_command("MOVE")
    assert robot.report() == "Robot is currently at coordinate (3,3) facing NORTH."

def test_place_command(robot):

  assert  robot.execute_command("PLACE 1,WEST,EAST") == "Invalid command."
  assert  robot.execute_command("PLACE 1,WEST") == "Invalid command."
  assert  robot.execute_command("PLACE") == "Invalid command."
  assert  robot.execute_command("PLACE 1,,") == "Invalid command."

def test_custom_commands(robot):

    robot.execute_command("PLACE 0,4,NORTH")
    robot.execute_command("MOVE")
    robot.execute_command("MOVE")
    robot.execute_command("LEFT")
    robot.execute_command("MOVE")

    assert robot.report() == "Robot is currently at coordinate (0,4) facing WEST."
