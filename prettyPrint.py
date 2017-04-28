__license__ = 'Marc VILLAIN (c) 2017'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prettyPrint.py 2017-04-28'

"""
Pretty print of a binary tree
2017
@author: Marc VILLAIN
"""

"""
NOTE
----------------------
Ce fichier est distribué dans un cadre de tests mais ne remplace en aucun cas vos propres vérifications.
L'auteur ne sera pas tenu responsable en cas de dysfonctionnement de ce code.
L'auteur ne sera en aucun cas mis en cause en cas d'abus d'utilisation ou de partage de ce code.

UTILISATION
----------------------
> Placer le fichier prettyPrint.py dans un dossier placé à côté de votre fichier de test
> Ajoutez cette ligne au début de votre fichier de test: 'from [VOTRE DOSSIER] import prettyPrint'
> Affichez votre BinTree de la manière suivante: 'prettyPrint.printTree(B)'

EXEMPLE DE CODE
----------------------
from [VOTRE DOSSIER] import prettyPrint

B = BinTree(1, BinTree(2, None, None), BinTree(3, None, None))
prettyPrint.printTree(B)

>>>>
 1
/ \
2 3


----------------------
Have fun ! :)
"""

class BinTree:

    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def printTree(B):
    printTreeInterval([B], 1, maxLevel(B))

def printTreeInterval(L, level, maxLevel):
    lenL = len(L)

    if lenL == 0 or areAllElementsNone(L):
        return

    floor = maxLevel - level
    endgeLines = 2**(max(floor - 1, 0))
    firstSpaces = 2**(floor) - 1
    betweenSpaces = 2**(floor + 1) - 1

    printWhiteSpaces(firstSpaces)

    L2 = []
    for B in L:
        if B != None:
            print(B.key, end='')
            L2.append(B.left)
            L2.append(B.right)
        else:
            L2.append(None)
            L2.append(None)
            print(' ', end='')

        printWhiteSpaces(betweenSpaces)

    print()

    for i in range(1, endgeLines + 1):
        for j in range(lenL):
            printWhiteSpaces(firstSpaces - i)

            if L[j] == None:
                printWhiteSpaces(endgeLines + endgeLines + i + 1)
                continue

            if L[j].left != None:
                print('/', end='')
            else:
                printWhiteSpaces(1)

            printWhiteSpaces(i + i - 1)

            if L[j].right != None:
                print('\\', end='')
            else:
                printWhiteSpaces(1)

            printWhiteSpaces(endgeLines + endgeLines - i)

        print()

    printTreeInterval(L2, level + 1, maxLevel)

def printWhiteSpaces(count):
    for i in range(count):
        print(' ', end='')

def maxLevel(B):
    if B == None:
        return 0

    return max(maxLevel(B.left), maxLevel(B.right)) + 1

def areAllElementsNone(L):
    for B in L:
        if B != None:
            return False
    return True