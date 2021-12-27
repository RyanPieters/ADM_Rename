from tika import parser
from pathlib import Path
import re
import os

# Required Variables
directory = Path(__file__).parent
counter = 0
GameIdList = []
GameDupList = []


def checkDuplicate(game_id):
    duplicate = False

    for x in GameIdList:
        if x == game_id and duplicate != True:
            duplicate = True
            break

    if duplicate:
        GameDupList.append(game_id)
        return None
    else:
        GameIdList.append(game_id)
        return game_id


# Main for loop
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        pdf_Name = filename
        raw_data = parser.from_file(pdf_Name)

        raw_data_trimmed = re.sub('\s+', '', raw_data['content'])

        idHit = raw_data_trimmed.find('eidentificatoconcodiceADM:')
        idEnd = raw_data_trimmed[idHit:].find('Presentata') - 26

        gameId = raw_data_trimmed[idHit+26:idHit+idEnd+26]

        gameId = checkDuplicate(gameId)

        if gameId is not None:
            os.rename(filename, gameId + '.pdf')

print('Game IDs found and renamed:')
for x in GameIdList:
    print(x + '\t', end=" ")
print('\nDuplicates found and not renamed:')
for x in GameDupList:
    print(x + '\t', end=" ")





