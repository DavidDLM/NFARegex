import postfix
from thompson import compile, paintGraph

regex = input("Regular expression: ")
ptf = postfix.shunting_yard(regex)
print("Postfix value: " + ptf)

result, transitionsList, edgeDict = compile(ptf)
paintGraph(result, transitionsList, edgeDict)
