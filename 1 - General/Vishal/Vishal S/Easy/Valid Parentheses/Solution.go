func isValid(s string) bool {
    stk := []string{}
    for _, x_rune := range s{
        x := string(x_rune)
        if x == "(" || x == "{" || x =="[" {
            stk = append(stk, x)
        } else{
            l := len(stk)
            if l > 0 && ((x == ")" && stk[l-1]=="(") || (x == "]" && stk[l-1]=="[") || (x == "}" && stk[l-1]=="{")) {
                stk = stk[0:l-1]
            }else{
                return false
            }
        }
    }
    return len(stk) == 0
}