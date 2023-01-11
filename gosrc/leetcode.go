package main

import "fmt"

//给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。
//
//
//
// 示例 1：
//
//
//输入：nums = [1,1,1], k = 2
//输出：2
//
//
// 示例 2：
//
//
//输入：nums = [1,2,3], k = 3
//输出：2
//
//
//
//
// 提示：
//
//
// 1 <= nums.length <= 2 * 10⁴
// -1000 <= nums[i] <= 1000
// -10⁷ <= k <= 10⁷
//
// Related Topics 数组 哈希表 前缀和 👍 1275 👎 0

//leetcode submit region begin(Prohibit modification and deletion)
// 前缀和 时间o(n^2) 空间o(n)
func subarraySum(nums []int, k int) int {
	preSum := make([]int, len(nums)+1)
	for i, v := range nums {
		preSum[i+1] = preSum[i] + v
	}
	count := 0
	for j := 1; j < len(preSum); j++ {
		for i := 0; i < j; i++ {
			// 计算i j 之间的差
			if preSum[j]-preSum[i] == k {
				count++
			}
		}
	}
	return count
}

// 前缀和
func subarraySum1(nums []int, k int) int {
	preSum := make([]int, len(nums)+1)
	set := make(map[int]int)
	set[0] = 1
	for i, v := range nums {
		preSum[i+1] = preSum[i] + v
		set[preSum[i+1]]++
	}
	count := 0
	for j := 1; j < len(preSum); j++ {
		// 计算i j 之间的差 可以通过hash来优化
		set[preSum[j]-k]--
		count += set[preSum[j]-k]
	}
	return count
}

func main() {
	arr := []int{-1, -1, 1}

	// arr1 := []int{1}

	subarraySum1(arr, 0)
	result := subarraySum1(arr, 1)
	fmt.Print(result)

}

//leetcode submit region end(Prohibit modification and deletion)
