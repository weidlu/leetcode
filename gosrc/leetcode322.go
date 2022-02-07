package main

import (
	"fmt"
	"math"
)

var memo = make(map[int]int)

// 带备忘录的递归
func recursion(coins []int, amount int) int {
	if amount == 0 {
		return 0
	}
	if amount < 0 {
		return -1
	}

	v, ok := memo[amount]
	if ok {
		return v
	}

	max := 10000000000
	res := max
	for _, c := range coins {
		r := recursion(coins, amount-c)
		if r < 0 {
			continue
		}
		res = int(math.Min(float64(res), float64(r+1)))
	}

	if res != max {
		memo[amount] = res
	}
	if res == max {
		return -1
	} else {
		return res
	}
}

// dp[0] = 0
// dp[n] = min{dp[n-c] + 1 | c £ coins}
func dp(coins []int, amount int) int {
	dpArray := make([]int, amount+1)
	for i := range dpArray {
		dpArray[i] = amount + 1
	}
	dpArray[0] = 0

	for i := range dpArray {
		for _, coin := range coins {
			if i-coin < 0 {
				continue
			}
			dpArray[i] = int(math.Min(float64(dpArray[i-coin]+1), float64(dpArray[i])))
		}
	}
	if dpArray[amount] == amount+1 {
		return -1
	}
	return dpArray[amount]
}

func main() {
	/*	coins := []int{1, 2, 5}
		amount := 11
		output := dp(coins, amount)
		fmt.Print(output)*/

	/*	coins1 := []int{2}
		amount1 := 3
		output1 := dp(coins1, amount1)
		fmt.Print(output1)*/

	coins2 := []int{2, 5, 10, 1}
	amount2 := 27
	output1 := dp(coins2, amount2)
	fmt.Print(output1)
}
