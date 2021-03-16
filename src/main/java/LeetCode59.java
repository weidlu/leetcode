

/**
 * @author weidlu
 * 螺旋矩阵II
 */
public class LeetCode59 {

    private static final int[][] DIRECTIONS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public int[][] generateMatrix(int n) {
        int row = 0;
        int col = 0;
        int[][] matrix = new int[n][n];
        int directIndex = 0;
        for (int i = 0; i < n*n; i++) {
            matrix[row][col] = i + 1;
            int newRow = DIRECTIONS[directIndex][0] + row;
            int newCol = DIRECTIONS[directIndex][1] + col;
            if (newRow < 0 || newRow >= n || newCol < 0 || newCol >= n || matrix[newRow][newCol] != 0) {
                directIndex = (directIndex + 1) % 4;
            }
            row = DIRECTIONS[directIndex][0] + row;
            col = DIRECTIONS[directIndex][1] + col;
        }
        return matrix;
    }
}
