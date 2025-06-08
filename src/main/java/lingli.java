// 输入是一个有序数组，如（1,3,8,9,2983,19203,20312,94888），
// 给定一个数字K，请找到一个位置，当K插入数组后，数组仍然是有序的，算法输出只需要返回位置，不需要返回整个数组。

public class lingli {

    private int index(int[] input, int k) {
        int low = 0;
        int high = input.length -1;
        int mid = (low + high ) / 2;

        while (low < high){
            if (input[mid] > k){
                // zuobian
                mid = (low + mid) / 2;
                high

            }else if (input[mid] < k) {
                // youbian
                mid = (high + mid) / 2;

            }
            else if (input[mid] == k){


            }

        }
    }
}
