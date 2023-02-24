import java.util.*;
import java.util.stream.*;


public class automata {
	
	ArrayList<transitions> transitions = new ArrayList<>(); // Arraylist de transiciones
    ArrayList<Integer> node = new ArrayList<>(); // Array list de nodos
    int finalState;
    char symbol;
    
    // Método para obtener el estado final.
    /**public Estado getEstadoFinal() {
        return this.a;
    }*/
    
    void setNodeSize(int nodes) {
        for(int n = 0; n < nodes; n++) {
        	node.add(n);
        }
    }
    int getNodesSize() {
        return node.size();
    }
    void setFinalState(int fin) {
    	finalState = fin;
    }
    int getFinalState() { // Método para obtener el estado final.
        return finalState;
    }
    void setTransition(int from, int to, char symbol) {
        transitions transition = new transitions(from, to, symbol);
        transitions.add(transition);
    }
    
    void printStates() {
        for(int n = 0; n < transitions.size(); n++) {
            transitions t = transitions.get(n);
            System.out.println("State " + t.from + " ---> State " + t.to + " : Symbol - " + t.symbol);
        }
        System.out.println("The final state is State " + getFinalState());
    }
    // Método para obtener el símbolo en una transición.
    public char getSymbol() {
        return this.symbol;
    }
    // Método para obtener la transición anterior.
    public automata getBeforeTransicion() {
        return this;
    }

    // Método para obtener la transición siguiente.
    public automata getNextTransition() {
        return this;
    }

    
    // Funcion Arraylist para manejar simbolos y adjuntarlos a un arraylist de los mismos
    ArrayList<Character> inputSymbols(ArrayList<Integer> node) {
        ArrayList<Character> symbols=new ArrayList<>();
        // Método para obtener las transiciones de un estado.
        for (int n = 0; n < node.size(); n++) {
            int fromTransition = node.get(n); // Get n for transition in n node
            for (int ct = 0; ct < transitions.size(); ct++) {
                transitions currentTransition = transitions.get(ct); // Get currentTransition
                if (currentTransition.from == fromTransition) {
                	if (currentTransition.symbol != 'ε') { // If not e closure, append
                		symbols.add(currentTransition.symbol);
                	}else {}
                }
            }
        }
        return symbols;
    }
    
    // Funcion arraylist con lista de objetos, para despues mapear
    // https://stackoverflow.com/questions/53984363/intstream-rangeclosed-unable-to-return-value-other-than-int
    ArrayList<Integer> mappingList(ArrayList<Integer> list){
    	//var s = IntStream.rangeClosed(1, list.size()).mapToObj(String::valueOf).collect(Collectors.toList());
        // .map(String::valueOf) // Stream<String>
    	// Arrays.stream(numbers) creates an IntStream under the hood and the map operation on an IntStream requires an IntUnaryOperator (i.e a function int -> int).
    	var s = IntStream.range(0, list.size()).filter(i -> ((i < list.size() - 1 && !list.get(i).equals(list.get(i + 1))) || i == list.size() - 1)).mapToObj(i -> list.get(i)).collect(Collectors.toCollection(ArrayList::new));
        return s;
    }
    
    // Funcion Arraylist para manejar epsilon y adjuntarlo a nuestro mapa segun lo visitado
    void epsilonClosure(int n, ArrayList<Integer> map, boolean visited[]){
    	map.add(n);
        for (int tr = 0; tr < transitions.size(); tr++) {
            transitions currentTransition = transitions.get(tr); // Get the current transition
            if (currentTransition.from == n) {
            	if (currentTransition.symbol == 'ε'){ // If epsilon from then to = current.to
            		int to = currentTransition.to;
                    if (!visited[to]) {
                        visited[to] = true; // Visited = true, funcion recursiva
                        epsilonClosure(to, map, visited);
                    }
            	}    
            }
        }
    }
    
    // Arraylist de epsilon closures y nodos visitados
    ArrayList<Integer> epsilon(ArrayList<Integer> nodes){
    	ArrayList<Integer> finalMap = new ArrayList<>(); // Arraylist con los resultados por visitados
    	boolean visited[] = new boolean[getNodesSize()]; // List de visitados con True/False segun la cuenta de NodesSize
        for (int n = 0; n < nodes.size(); n++) { // For get n in the arraylist Nodes, call epsilonClosure to identify epsilons
        	epsilonClosure(nodes.get(n), finalMap, visited);
        }
        Collections.sort(finalMap); // Sort final map
        finalMap = mappingList(finalMap); // Funcion arraylist con lista de objetos, para despues mapear
        return finalMap;
    }
    
    
    // Arraylist para manejar transiciones
    ArrayList<Integer> replaceAndMove(ArrayList<Integer> transitionList, char symbol){
        ArrayList<Integer> finalTransitionSymbols=new ArrayList<>();
        for (int n = 0; n < transitionList.size(); n++) {
            int transition = transitionList.get(n); // Get transition
            for (int tr = 0; tr < transitions.size(); tr++) {
                transitions currentTransition = transitions.get(tr); // Get current transition
                if (currentTransition.from == transition) {
                	if(currentTransition.symbol == symbol){
                		finalTransitionSymbols.add(currentTransition.to); // Add current transition and symbol to final
                	}       
                }
            }
        }
        Collections.sort(finalTransitionSymbols);
        return finalTransitionSymbols;
    }
    /**
    public String toString() { // Método para poder ver las transiciones.
        return this.from.toString() + " -- " + this.symbol + " --> " + this.to.toString();
    }
    public void replaceElement(int from, int to, char symbol) {
        this.from = from;
        this.a = a;
        this.simbolo = simbolo;
    }*/
    
    // Concatenation with explicit "."
    automata concatenation(automata auto1, automata auto2){
    	int tr;
    	transitions newTransition;
    	automata automata1 = new automata();
    	automata1.setNodeSize(auto1.getNodesSize() + auto2.getNodesSize()); // Concat
        // Set transition
        for(tr = 0; tr < auto1.transitions.size(); tr++) {
        	newTransition = auto1.transitions.get(tr); // Get transition
        	automata1.setTransition(newTransition.from, newTransition.to, newTransition.symbol);
        }
        automata1.setTransition(auto1.getFinalState(), auto1.getNodesSize(), 'ε'); // Set epsilon as transition
        // Automata 2
        int tr2;
        for(tr2 = 0; tr2 < auto2.transitions.size(); tr2++) {
        	newTransition = auto2.transitions.get(tr2);
        	automata1.setTransition(newTransition.from + auto1.getNodesSize(), newTransition.to + auto1.getNodesSize(), newTransition.symbol); // Set symbol as transition
        }
        automata1.setFinalState(auto1.getNodesSize() + auto2.getNodesSize() - 1);
        return automata1;
    }
    
}