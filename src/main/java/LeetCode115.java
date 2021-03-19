/**
 * @author weidlu
 * 不同的子序列
 */
public class LeetCode115 {

    int [][]memo;

    public int numDistinct(String s, String t) {
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        memo = new int[s.length()][t.length()];

        for (int i = 0; i < memo.length; i++) {
            for (int j = 0; j < memo[0].length; j++) {
                memo[i][j] = -1;
            }
        }

        return numDistinct(sChars, s.length() - 1, tChars, t.length() - 1);
    }


    public int numDistinct(char[] s, int i, char[] t, int j) {
        if (j < 0 ){
            return 1;
        }
        if (i < 0) {
            return 0;
        }
        if (memo[i][j] != -1){
            return memo[i][j];
        }
        if (s[i] == t[j]){
            memo[i][j] = numDistinct(s, i - 1, t, j - 1) + numDistinct(s, i - 1, t, j);
        }else {
            return numDistinct(s, i - 1, t, j);
        }
        return memo[i][j];
    }

    public static void main(String[] args) {
        LeetCode115 leetCode115 = new LeetCode115();
        String source = "bagbag";
        String target = "bag";
        System.out.println(leetCode115.numDistinct(source, target));
    }

}
