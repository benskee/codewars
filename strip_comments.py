def solution(string,markers):
    string = string.split("\n")

    for s in range(len(string)):
        for m in markers:
            if m in string[s]:
                for l in range(len(string[s])):
                    if string[s][l] == m:
                        string[s] = string[s][:l].strip()
                        break
    return "\n".join(string)

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", [
                   "#", "!"]))
                #    , "apples, pears\ngrapes\nbananas")
print(solution("a #b\nc\nd $e f g", ["#", "$"]))
# , "a\nc\nd")
