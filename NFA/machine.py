# Machine class
class Machine:
    def __init__(this, initialState, finalState):
        this.initialState = initialState
        this.finalState = finalState

    def getFinalMachineState(this):
        return this.finalState

    def getInitialMachineState(this):
        return this.initialState

    def display():
        return


# State class
class State:

    def __init__(this, state_id):
        this.state_id = state_id

    def __repr__(this):
        return str(this.state_id)


# Transitions class
class Transitions:
    def __init__(this, initialState, finalState, symbol):
        this.initialState = initialState
        this.finalState = finalState
        this.symbol = symbol

    def getInitialTransitionState(this):
        return this.initialState

    def setInitialTransitionState(this, initialState):
        this.initialState = initialState

    def getFinalTransitionState(this):
        return this.finalState

    def setFinalTransitionState(this, finalState):
        this.finalState = finalState

    def getTransitionSymbol(this):
        return this.symbol
