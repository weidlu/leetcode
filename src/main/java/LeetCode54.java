import java.util.ArrayList;
import java.util.List;

public class LeetCode54 {

    private static final int[][] DIRECTIONS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    private static final int VISITED = 1000;

    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();

        int len = matrix.length * matrix[0].length;

        int row = 0;
        int col = 0;
        int directionIndex = 0;

        for (int i = 0; i < len; i++) {
            result.add(matrix[row][col]);
            matrix[row][col] = VISITED;
            int[] direction = DIRECTIONS[directionIndex];
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            if (newRow < 0 || newRow >= matrix.length || newCol < 0 || newCol >= matrix[0].length || matrix[newRow][newCol] == VISITED) {
                directionIndex = (directionIndex + 1) % 4;
            }
            row = row + DIRECTIONS[directionIndex][0];
            col = col + DIRECTIONS[directionIndex][1];
        }

        return result;
    }

    public static void main(String[] args) {
        LeetCode54 leetCode54 = new LeetCode54();
        int[][] input = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        System.out.println(leetCode54.spiralOrder(input));
    }
}
