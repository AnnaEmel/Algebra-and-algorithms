import Jama.Matrix;

public class Algorithm {
    public static Matrix multiplication(Matrix A, Matrix B) {


        int N = A.getRowDimension();
        if ( N > 2){
            Matrix F = multiply(A, B, N);
            return F;
        }
        else {
            Matrix F = A.times(B);
            return F;
        }
    }

    private static Matrix multiply(Matrix A, Matrix B, int n) {
        Matrix A11 = A.getMatrix(0, n / 2, 0, n / 2);
        Matrix A12 = A.getMatrix(0, n / 2, n / 2, n);
        Matrix A21 = A.getMatrix(n / 2, n, 0, n / 2);
        Matrix A22 = A.getMatrix(n / 2, n, n / 2, n);

        Matrix B11 = B.getMatrix(0, n / 2, 0, n / 2);
        Matrix B12 = B.getMatrix(0, n / 2, n / 2, n);
        Matrix B21 = B.getMatrix(n / 2, n, 0, n / 2);
        Matrix B22 = B.getMatrix(n / 2, n, n / 2, n);

        Matrix S1 = A21.plus(A22);
        Matrix S2 = S1.minus(A11);
        Matrix S3 = A11.minus(A21);
        Matrix S4 = A12.minus(S2);
        Matrix S5 = B12.minus(B11);
        Matrix S6 = B22.minus(S5);
        Matrix S7 = B22.minus(B12);
        Matrix S8 = S6.minus(B21);

        Matrix P1 = multiplication(S2, S6);
        Matrix P2 = multiplication(A11, B11);
        Matrix P3 = multiplication(A12, B21);
        Matrix P4 = multiplication(S3, S7);
        Matrix P5 = multiplication(S1, S5);
        Matrix P6 = multiplication(S4, B22);
        Matrix P7 = multiplication(A22, S8);

        Matrix T1 = P1.plus(P2);
        Matrix T2 = T1.plus(P4);

        Matrix D11 = P2.plus(P3);
        Matrix D12 = T1.plus(P5).plus(P6);
        Matrix D21 = T2.minus(P7);
        Matrix D22 = T2.plus(P5);

        Matrix F = new Matrix(n, n);
        F.setMatrix(0, n /2-1, 0, n /2-1, D11);
        F.setMatrix(0, n /2-1, n /2, n -1, D12);
        F.setMatrix(n /2, n -1, 0, n /2-1, D21);
        F.setMatrix(n /2, n -1, n /2, n -1, D22);
        return F;
    }
}
