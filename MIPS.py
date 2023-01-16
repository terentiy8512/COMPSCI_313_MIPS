# class MipsState(Enum):
#	IF = "IF"
#	ID = "ID"
#	EX_JUMP = "EX_JUMP"
#	EX_BRANCH = "EX_BRANCH"
#	EX_RTYPE = "EX_RTYPE"
#	EX_NON_RTYPE = "EX_NON_RTYPE"
#	EX_LOADSTORE = "EX_LOADSTORE"
#	MEM_LOAD = "MEM_LOAD"
#	MEM_STORE = "MEM_STORE"
#	REGWR_NON_RTYPE = "REGWR_NON_RTYPE"
#	REGWR_RTYPE = "REGWR_RTYPE"
#	REGWR_LOAD = "REGWR_LOAD"
#	END = "END"

class MipsFSMCore(MipsFSM):
    def updateFSM(self, currentInst, currentState):
        # Input:
        # ======
        # currentInst: current assembly instruction
        # currentState: current FSM state
        #
        # Output:
        # =======
        # Return the next expected state based on current instruction and state
        # For example, the state after Instruction Fetch is MipsState.ID (Instruction decode)
        #
        # Please fill in from below line


        # getting the opcode from instruction
        instruction_array = currentInst.split(" ")
        opcode = instruction_array[0]

        # STATE 0
        nextState = MipsState.IF

        # STATE 1
        if currentState == MipsState.IF:
            nextState = MipsState.ID

        # STATE 2
        if currentState == MipsState.ID:

            # check for Jump instruction
            if opcode in ["j", "jr", "jal"]:
                nextState = MipsState.EX_JUMP

            # check for Branch instruction
            if opcode in ["beq", "bne", "bgt", "bge", "blt", "ble"]:
                nextState = MipsState.EX_BRANCH

            # check for R-type instructions
            if opcode in ["add", "sub", "addu", "subu", "mul", "mult", "div", "and", "or", "slt"]:
                nextState = MipsState.EX_RTYPE

            # check for Non R-Type
            if opcode in ["addi", "addiu", "andi", "or", "sll", "slr", "slti"]:
                nextState = MipsState.EX_NON_RTYPE

            # check for sw or lw
            if opcode in ["lw", "sw", "lui", "la", "li"]:
                nextState = MipsState.EX_LOADSTORE

        # STATE 3

        # Jump completion
        if currentState == MipsState.EX_JUMP:
            nextState = MipsState.END

        # Branch completion
        if currentState == MipsState.EX_BRANCH:
            nextState = MipsState.END

        # R-type execution
        if currentState == MipsState.EX_RTYPE:
            nextState = MipsState.REGWR_RTYPE

        # Non R-type execution
        if currentState == MipsState.EX_NON_RTYPE:
            nextState = MipsState.REGWR_NON_RTYPE

        # differ between lw and sw
        if currentState == MipsState.EX_LOADSTORE:

            if opcode in ["lw", "lui", "la", "li"]:
                nextState = MipsState.MEM_LOAD

            if opcode == "sw":
                nextState = MipsState.MEM_STORE

        # STATE 4

        # R-type completion
        if currentState == MipsState.REGWR_RTYPE:
            nextState = MipsState.END

        # Non R-type completion
        if currentState == MipsState.REGWR_NON_RTYPE:
            nextState = MipsState.END

        # Memory access (store)
        if currentState == MipsState.MEM_STORE:
            nextState = MipsState.END

        # Memory access (load)
        if currentState == MipsState.MEM_LOAD:
            nextState = MipsState.REGWR_LOAD

        # STATE 5
        if currentState == MipsState.REGWR_LOAD:
            nextState = MipsState.END








        return nextState