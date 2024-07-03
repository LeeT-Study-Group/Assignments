func pivotIndex(nums []int) int {
    nums = append([]int{0},nums...)
    for i:=1;i<len(nums);i++ {
        nums[i] += nums[i-1]
    }
    l := len(nums)-1
    for i:=1;i<len(nums);i++ {
        if nums[l]-nums[i]==nums[i-1] {
            return i-1
        }
    }
    return -1
}