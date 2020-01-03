package main

import (
	"fmt"
	"sort"
)

/*
   给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
   你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素
*/

func twoSum1(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if (nums[i] + nums[j]) == target {
				return []int{
					i,
					j,
				}
			}
		}
	}
	return []int{}
}

type Sortids struct {
	index int
	value int
}

func twoSum2(nums []int, target int) []int {
	var indexs []Sortids
	for k, v := range nums {
		indexs = append(indexs, Sortids{index: k, value: v})
	}

	sort.SliceStable(indexs, func(i, j int) bool {
		return indexs[i].value < indexs[j].value
	})

	head := 0
	tail := len(indexs) - 1
	sumres := nums[indexs[head].index] + nums[indexs[tail].index]
	for sumres != target {
		if sumres < target {
			head += 1
		}
		if sumres > target {
			tail -= 1
		}
		sumres = nums[indexs[head].index] + nums[indexs[tail].index]
	}

	return []int{
		indexs[head].index,
		indexs[tail].index,
	}
}

func twoSum3(nums []int, target int) []int {
	hashmap := make(map[int]int)
	for k, v1 := range nums {
		v2 := target - v1
		if value, ok := hashmap[v2]; ok {
			return []int{value, k}
		}
		hashmap[v1] = k
	}
	return []int{}
}

func main() {
	fmt.Println(twoSum3([]int{3, 2, 4}, 6))
}
