package main

type NumArray struct {
	PreSum []int
}

func Constructor(nums []int) NumArray {
	// num   -2, 0, 3, -5, 2, -1
	// pre 0 -2 -2  1  -4 -2  -3
	n := new(NumArray)
	n.PreSum = make([]int, len(nums)+1, len(nums)+1)
	n.PreSum = append(n.PreSum, 0)
	for i, v := range nums {
		n.PreSum[i+1] = v + n.PreSum[i]
	}
	return *n
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.PreSum[right+1] - this.PreSum[left]
}

func main() {
	Constructor([]int{-2, 0, 3, -5, 2, -1})

}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(left,right);
 */
