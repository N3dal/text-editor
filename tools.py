
from os import system
from os import name as OS_NAME


class Tools:

    @staticmethod
    def clear():
        """wipe terminal screen."""
        if OS_NAME == "posix":
            # for *nix machines.
            system("clear")

        elif OS_NAME == "windows":
            system("cls")

        else:
            # for any os in the world.
            # system("your-command")
            pass

        return None
