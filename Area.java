package yb222ce_assigin1;
import java.util.Scanner;
public class Area {
	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		System.out.print("Enter Radius: ");
		double radius = scan.nextDouble();
		final double PI = 3.14159;
		double area = Math.pow(radius, 2) * PI;

		System.out.println("Corresponding area is: " + (int) (area * 10 + 0.5) / 10.0);

		scan.close();
	}
}
