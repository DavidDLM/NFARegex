import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

/**
 * @author Mario de Leon
 * Este programa se realizo en Teoria de la Computacion como proyecto 1,
 * por lo que va a tener codigo de la entrega del proyecto 1:
 * https://github.com/Javier19-cmd/Proyecto-1-TeoCompu
 * 
 */
public class NFA {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        regex regex = new regex(); // Regex instance
        String r = "";
        System.out.println("Regular expression: ");
        r = input.nextLine(); // Read regex
        String post_value = regex.evaluate(r); // Evaluate regex -> postfix
        System.out.println("Postfix value: " + post_value);
        
	}

}
