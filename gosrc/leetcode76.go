package main

import "fmt"

func minWindow(s string, t string) string {
	var MAXINT = 10000000000
	need := make(map[string]int)
	window := make(map[string]int)
	for _, v := range t {
		need[string(v)]++
	}
	left, right, valid := 0, 0, 0
	var start int
	length := MAXINT

	for right < len(s) {
		indexS := string(s[right])
		// 窗口扩张
		right++
		if need[indexS] > 0 {
			window[indexS]++
			if window[indexS] == need[indexS] {
				// 如果这个目标字符已经达到了要求的数量
				valid++
			}
		}
		for len(need) == valid {
			// 窗口收缩
			if right-left < length {
				start = left
				length = right - left
			}
			d := string(s[left])
			left++
			// 上一个左边界的值是需要的
			if need[d] > 0 {
				// 并且窗口内包含的值和期望的值在上一个状态是相等的（换句话说 左边收缩后，窗口内的值就减少了）
				if window[d] == need[d] {
					// 那么valid就要减1
					valid--
					window[d]--
				}
			}
		}
	}
	if length == MAXINT || start == 0 {
		return ""
	} else {
		return s[start-1 : start+length]
	}
}

// 输入：s = "ADOBECODEBANC", t = "ABC"
//输出："BANC"
func main() {
	s := "ADOBECODEBANC"
	t := "ABC"

	window := minWindow(s, t)
	fmt.Println(window)
}
