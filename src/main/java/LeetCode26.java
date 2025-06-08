import java.lang.reflect.Proxy;
import java.util.Arrays;

public class LeetCode26 {

    public int removeDuplicates(int[] nums) {
        if ()
        if (nums.length == 0) {
            return 0;
        }
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }

    public static void main(String[] args) {
        //        int[] input = {1, 1, 2};
        //        LeetCode26 leetCode26 = new LeetCode26();
        //        int i = leetCode26.removeDuplicates(input);
        //        int[] ints = Arrays.copyOf(input, i);
        //        System.out.println(Arrays.toString(ints));

        Integer i = 100;
        Integer i1 = new Integer(100);
        System.out.println(i == i1);
    }

}
