"""
This is a simple Choose Your Own Adventure Game

Things we need to program:
1. Player
  - Health
  - Movement
  - Name
  - Appearance/traits (charisma, etc.)
  - Attack power/weapon
2. NPCs
3. Enemies/boss
4. ASCII map
5. Quests
"""


__author__ = "Mr. McGarrah's 7th Period"
__version__ = "0.1"


import os
import entities
from universal_globals import *

def main() -> None:
    experiment = entities.Experimental_Entity(name="Experiment")


import ascii_map

if __name__ == "__main__":
    """ This is excecuted when the file is run from the command line """
    main()