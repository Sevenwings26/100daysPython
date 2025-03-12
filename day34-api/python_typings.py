# Typing in python and Type Hint

# age: int
# name: str
# height: float
# is_human: bool

def police_check(age: int) -> bool:
    """
    A function to check if a person is old enough to be in the police force."
    """
    if age > 18:
        can_join = True
    else:
        can_join = False