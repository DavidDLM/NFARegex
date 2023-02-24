import java.lang.reflect.Array;
import java.util.*;

public class transitions{
	// Global variables in transitions
	int from, to; // From es el estado de inicio y To es el estado de fin.
	char symbol; // Simbolo de la transicion.
    transitions(int from, int to, char symbol){
    	this.from=from;
        this.to=to;
        this.symbol=symbol;
     // Enlazando los estados para armar el AFN.
        //this.from.agregarEstadoSiguiente(to);
        //this.to.agregarEstadoAnterior(from);
    }
    
}