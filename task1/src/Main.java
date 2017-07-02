import Jama.Matrix;

public class Main {
    public static void main(String[] args) {
        Matrix[] read = Start.read();
        Matrix A = read[0];
        Matrix B = read[1];
        Matrix C = Algorithm.multiplication(A, B);

        int N = C.getColumnDimension();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.printf("%3.2f", C.get(i, j));
            }
            System.out.println("\n");
        }
    }
}
