import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[] arr = new int[2];
        arr[0] = input.nextInt();
        arr[1] = input.nextInt();
        int[][] arr1 = new int[arr[0]][arr[1]];
        int[][] arr2 = new int[arr[0]][arr[1]];
        for (int i = 0; i < arr[0]; i++) {
            for (int j = 0; j < arr[1]; j++) {
                arr1[i][j] = input.nextInt();
            }
        }
        for (int i = 0; i < arr[0]; i++) {
            for (int j = 0; j < arr[1]; j++) {
                arr2[i][j] = input.nextInt();
            }
        }
        for (int i = 0; i < arr[0]; i++) {
            for (int j = 0; j < arr[1]; j++) {
                System.out.print(arr1[i][j] + arr2[i][j] + " ");
            }
            System.out.println();
        }
    }
}