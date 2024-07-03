func plusOne(digits []int) []int {
    result := []int{}
    carry := true
    slices.Reverse(digits)
    for _,val := range digits {
        if carry {
            val += 1
            carry = (val == 10)
        }
        result = append(result, val%10)
    }
    if carry {
        result = append(result, 1)
    }
    slices.Reverse(result)
    return result
}