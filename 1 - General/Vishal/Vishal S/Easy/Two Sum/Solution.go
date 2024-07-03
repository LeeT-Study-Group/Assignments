func twoSum(nums []int, target int) []int {
    storage := make(map[int]int)
    for idx, num := range(nums){
        val, present := storage[target-num]
        if present {
            return []int{idx, val}
        }
        storage[num] = idx
    }
    return []int{}
}