# Thompson function
# https://userpages.umbc.edu/~squire/cs451_l6.html
'''
The thompson function takes a regular expression as input
and returns the start state of the resulting NFA.
It uses a stack to keep track of sub-expressions,
and constructs the NFA incrementally as it processes each
symbolacter of the input string

'''
from graphviz import Digraph
from machine import *
import matplotlib.pyplot as plt

EPSILON = 'ε'


def compile(regex):
    transitionsList = []
    splitTransitionsList = []
    vertexStack = []
    # Edge dictionary represents transitions to other states
    edgeDict = {}
    stateCount = 0
    startingState = None
    finalState = None
    finalStateList = []
    symbolList = []
    error = False
    for symbol in regex:
        # Left parenthesis management
        if symbol == "(":
            vertexStack.append(startingState)
            startingState = None
            finalState = None
        # Right (end) parenthesis management
        elif symbol == ")":
            finalState = vertexStack.pop()
            if not vertexStack:
                startingState = None
            else:
                startingState = vertexStack[-1]

        # Kleene star, 4 nodes, 4 transitions
        # From q1 to qfinal, Epsilon
        elif symbol == '*':
            try:
                '''
                # Kleene star guide/template:

                new_start = State(stateCount)
                new_end = State(stateCount)
                end_state.add_transition(EPSILON, start_state)
                end_state.add_transition(EPSILON, new_end)
                new_start.add_transition(EPSILON, start_state)
                new_start.add_transition(EPSILON, new_end)
                start_state = new_start
                end_state = new_end

                '''
                # Save states in variables
                automata = vertexStack.pop()
                new_start = State(stateCount)
                stateCount = stateCount + 1
                new_end = State(stateCount)
                stateCount = stateCount + 1

                # Add transitions (Kleene Star: 4 transitions)
                # Also add transitions to transition list
                newTransition = Transitions(
                    new_start, automata.getInitialMachineState(), EPSILON)
                transitionsList.append(newTransition)
                splitTransitionsList.append(
                    [new_start, EPSILON, automata.getInitialMachineState()])

                newTransition2 = Transitions(new_start, new_end, EPSILON)
                transitionsList.append(newTransition2)
                splitTransitionsList.append(
                    [new_start, EPSILON, new_end])

                newTransition3 = Transitions(
                    automata.getFinalMachineState(), automata.getInitialMachineState(), EPSILON)
                transitionsList.append(newTransition3)
                splitTransitionsList.append(
                    [automata.getFinalMachineState(), EPSILON, automata.getInitialMachineState()])

                newTransition4 = Transitions(
                    automata.getFinalMachineState(), new_end, EPSILON)
                transitionsList.append(newTransition4)
                splitTransitionsList.append(
                    [automata.getFinalMachineState(), EPSILON, new_end])

                startingState = new_start
                finalState = new_end
                result = Machine(startingState, finalState)
                vertexStack.append(result)
            except:
                error = True
                print("\nKleene Star error.")

        elif symbol == '|':
            try:
                '''
                # OR guide/template:

                new_start = State()
                new_end = State()
                new_start.add_transition(EPSILON, start_state)
                new_start.add_transition(EPSILON, end_state)
                start_state = new_start
                end_state = new_end

                '''
                # Save states in variables
                # Two automatas: from, to
                aTo = vertexStack.pop()
                aFrom = vertexStack.pop()
                new_start = State(stateCount)
                stateCount = stateCount + 1
                new_end = State(stateCount)
                stateCount = stateCount + 1

                # Add transitions (OR: 4 transitions)
                # Also add transitions to transition list
                newTransition3 = Transitions(
                    new_start, aFrom.getInitialMachineState(), EPSILON)
                transitionsList.append(newTransition3)
                splitTransitionsList.append(
                    [new_start, EPSILON, aFrom.getInitialMachineState()])

                newTransition4 = Transitions(
                    new_start, aTo.getInitialMachineState(), EPSILON)
                transitionsList.append(newTransition4)
                splitTransitionsList.append(
                    [new_start, EPSILON, aTo.getInitialMachineState()])

                newTransition5 = Transitions(
                    aFrom.getFinalMachineState(), new_end, EPSILON)
                transitionsList.append(newTransition5)
                splitTransitionsList.append(
                    [aFrom.getFinalMachineState(), EPSILON, new_end])

                newTransition6 = Transitions(
                    aTo.getFinalMachineState(), new_end, EPSILON)
                transitionsList.append(newTransition6)
                splitTransitionsList.append(
                    [aTo.getFinalMachineState(), EPSILON, new_end])

                startingState = new_start
                finalState = new_end
                result = Machine(startingState, finalState)
                vertexStack.append(result)
            except:
                print("\nOR error.")

        elif symbol == '.':
            try:
                '''
                # Concatenation guide/template:

                new_start = State()
                new_end = State()
                new_start.add_transition(EPSILON, start_state)
                new_start.add_transition(EPSILON, end_state)
                start_state = new_start
                end_state = new_end

                ---------------------------------

                e2 = stack.pop()
                e1 = stack.pop()
                e1.accept = False
                e1.edges[None] = [e2]
                stack.append(e1)
                stack.append(e2)s

                '''
                # Save states in variables
                # Two automatas: from, to
                aTo = vertexStack.pop()
                aFrom = vertexStack.pop()
                new_start = aTo.getInitialMachineState()
                new_end = aFrom.getFinalMachineState()
                for transition in transitionsList:
                    if transition.getInitialTransitionState() == new_start:
                        transition.setInitialTransitionState(new_end)
                startingState = new_start
                finalState = new_end
                result = Machine(startingState, finalState)
                vertexStack.append(result)
            except:
                error = True
                print("\nConcatenation error.")

        elif symbol == '+':
            try:
                '''
                # Union guide/template:

                new_start = State()
                new_end = State()
                new_start.add_transition(EPSILON, start_state)
                new_start.add_transition(EPSILON, end_state)
                start_state = new_start
                end_state = new_end

                '''
                # Save states in variables
                automata = vertexStack.pop()
                new_start = State(stateCount)
                stateCount = stateCount + 1
                new_end = State(stateCount)
                stateCount = stateCount + 1
                # Add transitions (UNION: 3 transitions)
                # Add transition to transition list
                newTransition8 = Transitions(
                    new_start, automata.getInitialMachineState(), EPSILON)
                transitionsList.append(newTransition8)
                splitTransitionsList.append(
                    [new_start, EPSILON, automata.getInitialMachineState()])

                newTransition9 = Transitions(automata.getFinalMachineState(),
                                             automata.getInitialMachineState(), EPSILON)
                transitionsList.append(newTransition9)
                splitTransitionsList.append([automata.getFinalMachineState(), EPSILON,
                                             automata.getInitialMachineState()])

                newTransition10 = Transitions(
                    automata.getFinalMachineState(), new_end, EPSILON)
                transitionsList.append(newTransition10)
                splitTransitionsList.append(
                    [automata.getFinalMachineState(), EPSILON, new_end])

                result = Machine(new_start, new_end)
                vertexStack.append(result)

            except:
                error = True
                print("\nUNION error.")
        elif symbol == '?':
            try:
                '''
                # Concurrence guide/template:

                new_start = State(stateCount)
                new_end = State(stateCount)
                end_state.add_transition(EPSILON, start_state)
                end_state.add_transition(EPSILON, new_end)
                new_start.add_transition(EPSILON, start_state)
                new_start.add_transition(EPSILON, new_end)
                start_state = new_start
                end_state = new_end

                '''
                # Save states in variables
                automata = vertexStack.pop()
                new_start = State(stateCount)
                stateCount = stateCount + 1
                new_end = State(stateCount)
                stateCount = stateCount + 1

                # Add transitions (CONCURRENCE: 3 transitions)
                # Add transition to transition list
                newTransition11 = Transitions(
                    new_start, automata.getInitialMachineState(), EPSILON)
                transitionsList.append(newTransition11)
                splitTransitionsList.append(
                    [new_start, EPSILON, automata.getInitialMachineState()])

                newTransition12 = Transitions(new_start, new_end, EPSILON)
                transitionsList.append(newTransition12)
                splitTransitionsList.append([new_start, EPSILON, new_end])

                newTransition13 = Transitions(
                    automata.getFinalMachineState(), new_end, EPSILON)
                transitionsList.append(newTransition13)
                splitTransitionsList.append(
                    [automata.getFinalMachineState(), EPSILON, new_end])

                startingState = new_start
                finalState = new_end
                result = Machine(startingState, finalState)
                vertexStack.append(result)

            except:
                error = True
                print("\nCONCURRENCE error.")

        else:
            try:
                # Create a new NFA with a single edge for the character
                # Other symbols
                # Save states in variables
                new_start = State(stateCount)
                stateCount = stateCount + 1
                new_end = State(stateCount)
                stateCount = stateCount + 1
                # Add transitions
                # Add transition to transition list
                newTransition7 = Transitions(new_start, new_end, symbol)
                transitionsList.append(newTransition7)
                splitTransitionsList.append(
                    [new_start, symbol, new_end])

                startingState = new_start
                finalState = new_end
                result = Machine(startingState, finalState)
                vertexStack.append(result)
            except:
                error = True
                print("\nSymbol error.")
    '''
    To convert a list to a dictionary using the same values,
    you can use the dict.fromkeys() method. To convert two lists
    into one dictionary, you can use the Python zip() function.
    The dictionary comprehension lets you create a new dictionary
    based on the values of a list.

    '''
    for element in transitionsList:
        if element.getInitialTransitionState() in edgeDict:
            edgeDict[element.getInitialTransitionState()].append(
                (element.getTransitionSymbol(), element.getFinalTransitionState()))
        else:
            edgeDict[element.getInitialTransitionState()] = [(
                element.getTransitionSymbol(), element.getFinalTransitionState())]

        if element.getFinalTransitionState() not in edgeDict:
            edgeDict[element.getFinalTransitionState()] = []

    result = vertexStack.pop()
    return result, splitTransitionsList, edgeDict


def paintGraph(result, splitTransitionsList, edgeDict):
    dot = Digraph(comment='NFA')
    for state in edgeDict:
        dot.node(str(state), shape="circle")
        if state == result.getFinalMachineState():
            dot.node(str(state), shape="doublecircle")
    for transition in splitTransitionsList:
        if transition[1] == EPSILON:
            dot.edge(str(transition[0]), str(transition[2]), label="ε")
        else:
            dot.edge(str(transition[0]), str(
                transition[2]), label=transition[1])
    dot.render('NFAGraph', format='png', view=True)
