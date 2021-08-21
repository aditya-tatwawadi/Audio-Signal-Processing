"""
Aditya Tatwawadi - Summmer 2021 - Westminster School - John Locke

Application to take a song in a .mid file, convert it into Parson's Code
and display a photo of possible song suggestions

n.b. 
- Generally only successful for Classical music with a single melody line in isolation (Though does work for most songs on musipedia).
- .mid file should be very accurate (ideally taken from musipedia).

Some test songs & their corresponding Parson's codes:

Fur Elise              | DUDUDUDDDUUU      | Giscard Rasquin & Ludwig van Beethoven
Eine kleine Nachtmusik | DUDUDUUUDDUDUDDUD | Wolfgang Amadeus Mozart
Jana Gana Mana         | UURRRRR           | Rabindranath Tagore
"""

#Import general dependency
import time

#Import Pillow to show screenshot (will need to be done with HomeBrew)
from PIL import Image


def show_suggestions():
    music_suggestions = Image.open("musipedia_recommendations.png")
    music_suggestions.show()

if __name__ == "__main__":
    
    #Import file written to compute Parson's Code  
    import compute

    #Delay needed to read txt file
    time.sleep(1)

    #Import file written to scrape Musipedia
    import webscrape
    time.sleep(1)
    show_suggestions()