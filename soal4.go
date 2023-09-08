package main

import "fmt"

func sorting(aaa []int) []int {
	aab := len(aaa)

	for aba := 0; aba < aab-1; aba++ {
		for baa := 0; baa < aab-aba-1; baa++ {
			if aaa[baa] < aaa[baa+1] {
				aaa[baa], aaa[baa+1] = aaa[baa+1], aaa[baa]
			}
		}
	}
	return aaa
}

func main() {
	bbb := sorting([]int{1, 10, 2, 5, 4})
	fmt.Println(bbb)
}
