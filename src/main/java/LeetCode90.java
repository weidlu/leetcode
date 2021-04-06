import org.apache.commons.lang3.StringUtils;

import java.util.*;
import java.util.stream.Collectors;

public class LeetCode90 {

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<Integer> numList = new ArrayList<>();
        for (int num : nums) {
            numList.add(num);
        }

        Set<List<Integer>> sets = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            int last = nums.length;
            while (last > i) {
                sets.add(numList.subList(i, last));
                last--;
            }
        }
        sets.add(new ArrayList<>());

        return new ArrayList<>(sets);
    }

    public static void main(String[] args) {
        LeetCode90 leetCode90 = new LeetCode90();

        int []input = {1,2,3};

        List<List<Integer>> lists = leetCode90.subsetsWithDup(input);
        for (List<Integer> list : lists) {
            System.out.println(StringUtils.join(list, "|"));
        }
    }
}
