package main

import (
	"fmt"
	"math"

	. "leetcode/dependcy"
)

//给定一个二叉树，找出其最大深度。
//
// 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
//
// 说明: 叶子节点是指没有子节点的节点。
//
// 示例：
//给定二叉树 [3,9,20,null,null,15,7]，
//
//     3
//   / \
//  9  20
//    /  \
//   15   7
//
// 返回它的最大深度 3 。
// Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1105 👎 0

//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

var result = 0
var depth = 0

func maxDepth(root *TreeNode) int {
	var r int
	travel(root)
	r = result
	result = 0
	depth = 0
	return r
}

func maxDepth1(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return int(math.Max(float64(maxDepth1(root.Left)), float64(maxDepth1(root.Right))) + 1)
}

func travel(root *TreeNode) {
	if root == nil {
		result = int(math.Max(float64(result), float64(depth)))
		return
	}
	depth++
	travel(root.Left)
	travel(root.Right)
	depth--
}

func main() {
	r := TreeNode{Val: 1}
	rr := TreeNode{Val: 3}
	r.Left = nil
	r.Right = &rr

	d := maxDepth(&r)
	fmt.Println(d)

	fmt.Printf("分解的解法：%v \n", maxDepth1(&r))

}
