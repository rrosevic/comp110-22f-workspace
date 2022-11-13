"""Examples of a class and objects."""

class Profile:
    handle: str
    followers: int
    is_private: bool

#   can initialize attributes from within the constructor 
#   or when you set up the class
# make params optional
    def __init__(self, handle: str):
        # self is assigned a reference to the object of class 
        # special return type, returns the profile object
        """Constructor initializes attributes!"""
        self.handle = handle
        self.followers = 0
        self.is_privat = False

    def tweet(self, msg: str) -> None:
        # Methods tell you capabilities of objects.
        """An example of a method."""
        print(f"@{self.handle} tweets {msg}")


my_profile: Profile = Profile("rrosevic")
# type profile
my_profile.tweet("Hello, world.")

# two objects can have the same values and can be changed later
    # another_profile: Profile = Profile("krisjordan")
    # another_profile.handle = "theverge"