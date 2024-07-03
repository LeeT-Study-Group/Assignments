func findWords(words []string) []string {    
    result := []string{}
    for idx, val := range words {
        val = strings.ToLower(val)
        row_number := findRow(string(val[0]))
        possible := true
        for i:= 1; i<len(val); i+=1 {
            if findRow(string(val[i])) != row_number {
                possible = false
                break
            }
        }
        if possible {
            result = append(result, words[idx])
        }

    }
    return result
}

func findRow(char string) int {
    keyboard := [3]string{
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
    }
    for idx, row := range keyboard {
        for i:=0; i<len(row); i+=1 {
            if string(row[i]) == char{
                return idx
            }
        }
    }
    return -1
}