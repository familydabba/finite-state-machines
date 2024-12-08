class DFA:
    def __init__(self, Q, Sigma, Delta, qO, F):
        self.Q = Q      # set of states
        self.Sigma = Sigma      # set of symbols
        self.Delta = Delta      # transition functions as a dict
        self.qO = qO        # initial state
        self.F = F      # set of final states

    def run(self, word):
        q = self.qO     # fetching the initial state
        while( word != "" ):
            q = self.Delta[(q, word[0])]    # fetching the next state
            word = word[1:]     # trimming the first character
        return q in self.F      # checking if q is one of the final states

def runDFA():
    print("This is a simple implementation of DFA (Deterministic Finite Automata)")
    print("----------------------------------------------------------------------")
    print("THe condition it checks for is if 'all A appear before B' in a string ")
    D_ab = DFA({1, 2, 3}, {"a", "b"}, {(0, "a"): 0, (0, "b"): 1, (1, "b"): 1, (1, "a"): 2, (2, "a"): 2, (2, "b"): 2}, 0, {0, 1})
    while(True):
        inp = input("Enter the string you wish to check (enter q to exit): ").rstrip().lower()
        if inp == 'q':
            break

        res = D_ab.run(inp)
        print(res)
        print("----")



if __name__ == "__main__":
    runDFA()
