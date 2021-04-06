

public class LeetCode191 {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ret = 0;
        for (int i = 0; i < 32; i++) {
            if ((n & (1 << i)) != 0) {
                ret++;
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        LeetCode191 leetCode191 = new LeetCode191();
        System.out.println(leetCode191.hammingWeight(11));
    }
}
