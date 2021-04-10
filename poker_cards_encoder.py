suits = {
    "c": 0,
    "d": 13,
    "h": 26,
    "s": 39
}
faces = {
    "A": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12
}
def encode(cards):
    ans = []
    for card in cards:
        ans.append(suits[card[1]]+faces[card[0]])
        
    return sorted(ans)


def decode(cards):
    ans = []
    for card in sorted(cards):
        pair = divmod(card, 13)
        ans.append(str(list(faces.keys())[list(faces.values()).index(pair[1])])+str(list(suits)[pair[0]]))
    return ans




print(decode([7, 22, 51]))
#  ["8c", "Td", "Ks"])
print(decode([13, 30, 37]))
#  ["Ad", "5h", "Qh"])
print(decode([7, 51, 22]))
#  ["8c", "Td", "Ks"])
print(decode([13, 37, 30]))
#  ["Ad", "5h", "Qh"])




# print(encode(["Td", "8c", "Ks"]))
#  [7, 22, 51])
# print(encode(["Qh", "5h", "Ad"]))
#  [13, 30, 37])
# print(encode(["8c", "Ks", "Td"]))
#  [7, 22, 51])
# print(encode(["Qh", "Ad", "5h"]))
#  [13, 30, 37])





