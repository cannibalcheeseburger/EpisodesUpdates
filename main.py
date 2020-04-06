import datetime
from texttable import Texttable
import AddNew
import UpdateCurrent
import display
import os

def main():
    while(True):
        choose = int(input("1.Add Series\n2.Display Cached Series List\n3.Update List\n0.Quit\nEnter your choice(0-3): "))
        os.system("clear")
        if choose == 1:
            AddNew.add_series()
            input("Press anything to proceed:")
        elif choose == 2:
            display.display_series()
            input("Press anything to proceed:")
        elif choose == 3:
            UpdateCurrent.update_series()
            input("Press anything to proceed:")
        elif choose == 0:
            return 
        else:
            input("Invalid choice\nPress anything to proceed:")
        os.system('clear')

if __name__ == "__main__":
    main()   