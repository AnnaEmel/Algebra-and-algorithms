import java.util.Scanner;
import Jama.Matrix;



/**
 * Created by Anna on 14.11.2016.
 */
public class Start {
    public static Matrix[] read() {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter N");
        int N = in.nextInt();
        int[][] arr = new int[2 * N][N];

        System.out.print("Enter matrix");
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                arr[i][j] = in.nextInt();
            }
        }
        in.close();

        Matrix A = new Matrix(N, N);
        Matrix B = new Matrix(N, N);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                A.set(i, j, arr[i][j]);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                B.set(i, j, arr[i][j]);
            }
        }

        return new Matrix[]{A, B};
    }
}
