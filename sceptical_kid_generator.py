def alan_annoying_kid(sentence):

    didnt = "didn't "
    if didnt in sentence:
        object = "did " + sentence.split(" ")[3]
        end = " it!"
    else: 
        object = "didn't " + sentence.split(" ")[2]
        end = " at all!"
    if object[-2:] == "ed":
        object = object[:-2]
    action = sentence[8:-1]
    reply = f"I don't think you {action} today, I think you {object}{end}"
    return reply


print(alan_annoying_kid("Today I played football."))
                #    Output: "I don't think you played football today, I think you didn't play at all!")
print(alan_annoying_kid("Today I didn't play football."))
                #    Output: "I don't think you didn't play football today, I think you did play it!")
print(alan_annoying_kid("Today I didn't attempt to hardcode this Kata."))
                #    Output: "I don't think you didn't attempt to hardcode this Kata today, I think you did attempt it!")
print(alan_annoying_kid("Today I cleaned the kitchen."))
                #    Output: "I don't think you cleaned the kitchen today, I think you didn't clean at all!")
print(alan_annoying_kid("Today I learned to code like a pro."))
                #    Output: "I don't think you learned to code like a pro today, I think you didn't learn at all!")
