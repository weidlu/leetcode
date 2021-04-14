import java.util.Arrays;

public class LeetCode179 {
    public String largestNumber(int[] nums) {
        String[] str = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            str[i] = String.valueOf(nums[i]);
        }
        Arrays.sort(str, (o1, o2) -> {
            if (o1.charAt(0) != o2.charAt(0)) {
                return o2.charAt(0) - o1.charAt(0);
            }
            return (o2 + o1).compareTo(o1 + o2);
        });
        if (str[0].charAt(0) == '0') {
            return "0";
        }
        return String.join("", str);
    }

}
