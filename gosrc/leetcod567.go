package main

import "fmt"

// 滑动窗口算法框架
func checkInclusion(s1 string, s2 string) bool {
	need, window := make(map[string]int), make(map[string]int)
	for i := 0; i < len(s1); i++ { // 使用range遍历得到是rune,使用t[i]得到的是byte
		need[string(s1[i])]++ // map[key]访问哈希表中键对应的值。如果key不存在，自动创建这个key,并把map[key]赋值为0
	}
	left, right, valid := 0, 0, 0
	for right < len(s2) {
		b := string(s2[right])
		right++
		// 窗口更新
		if need[b] > 0 {
			window[b]++
			if window[b] == need[b] {
				valid++
			}
		}
		for right-left >= len(s1) {
			if valid == len(need) {
				return true
			}
			lb := string(s2[left])
			left++
			if need[lb] > 0 {
				if need[lb] == window[lb] {
					valid--
					window[lb]--
				}
			}
		}

	}
	return false
}

func main() {
	s1 := "hello"
	s2 := "ooolleoooleh"
	b := checkInclusion(s1, s2)
	fmt.Println(b)
}
