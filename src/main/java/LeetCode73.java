import java.util.*;

/**
 * 矩阵置零
 */

public class LeetCode73 {

    public void setZeroes(int[][] matrix) {

        List<Map.Entry<Integer, Integer>> indexList = new ArrayList<>();

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0){
                    Map.Entry<Integer, Integer> entry = new AbstractMap.SimpleEntry<>(i, j);
                    indexList.add(entry);
                }
            }
        }

        for (Map.Entry<Integer, Integer> entry : indexList) {
            effect(matrix, entry.getKey(), entry.getValue());
        }
    }


    private void effect(int[][] matrix, int i, int j) {
        for (int k = 0; k < matrix[0].length; k++) {
            matrix[i][k] = 0;
        }
        for (int k = 0; k < matrix.length; k++) {
            matrix[k][j] = 0;
        }
    }

    public static void main(String[] args) {
        int[][] input = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
        LeetCode73 leetCode73 = new LeetCode73();
        leetCode73.setZeroes(input);
        System.out.println(Arrays.toString(input[0]));
        System.out.println(Arrays.toString(input[1]));
        System.out.println(Arrays.toString(input[2]));
    }
}
