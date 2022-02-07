import java.util.Scanner;

public class Excepcion {
	
	public static void main(String[] args) {
		
		Scanner cin = new Scanner(System.in);
		int n;
		
		System.out.print("Ingresa un número: ");
		
		//Captura de excepcion
		
		try {			//BLOQUE QUE CONTIENE EL CODIGO QUE PUEDE PRODUCIR UNA EXCEPCION
			
			//Almacena el valor dado
			n = cin.nextInt();
			
			//Lo imprime en pantalla
			System.out.println(n);
			
		} catch(Exception e) {		//BLOQUE QUE CONTIENE EL CODIGO SI SE PRODUCE UN ERROR
			
			//Imprime mensaje
			System.out.println("Valor invalido");
			
		} finally {		//BLOQUE OPCIONAL
			
			System.out.println("Proceso terminado.");
			
		}
	}
}
