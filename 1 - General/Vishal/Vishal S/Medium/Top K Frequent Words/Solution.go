func topKFrequent(words []string, k int) []string {
    counter_1 := map[string]int{}
    for _,val := range words {
        if _, exist := counter_1[val]; !exist {
            counter_1[val] = 0
        } 
        counter_1[val]++
    }
    counter_2 := make(map[int][]string)
    for x := range counter_1 {
        if _,exist := counter_2[counter_1[x]]; !exist {
            counter_2[counter_1[x]] = []string{}
        } 
        counter_2[counter_1[x]] = append(counter_2[counter_1[x]], x)
    }
    values := []int{}
    for count := range counter_2 {
        values = append(values, count)
        str := counter_2[count]
        sort.Strings(str)
        counter_2[count] = str
    }
    sort.Slice(values, func(i,j int)bool{ return values[i] > values[j] })
    result := []string{}
    for _,x := range values {
        if len(counter_2[x]) <= k {
            k-=len(counter_2[x])
            result = append(result, counter_2[x]...)
        }else{
            result = append(result, counter_2[x][:k]...)
            k = 0
        }
        if k==0{
            break
        }
    }
    return result
}