func parseBoolExpr(expression string) bool {
    if len(expression)==1{
        return (expression[0]=='t')
    }
    stack := []rune{}
    operations := []rune{}
    for i:=0;i<len(expression);i++{
        curr := rune(expression[i])
        if curr=='t' || curr == 'f' || curr == ',' {
            stack = append(stack,curr)
        } else if curr == '&' || curr == '|' || curr == '!' {
            operations = append(operations, curr)
        } else if curr == '(' {
            stack = append(stack,curr)
        } else if curr == ')' {
            l := len(operations)
            oper := operations[l-1]
            operations = operations[:l-1]
            idx := len(stack)-1
            if stack[idx] != 'f' && stack[idx] != 't'{
                idx--
            }
            result := stack[idx]
            for idx >=0 && stack[idx] != '(' {
                if stack[idx] == 't' || stack[idx] == 'f' {
                    if oper == '&'{
                        if (result == 't' && stack[idx] == 't'){result='t'} else {result='f'}
                    }else if oper=='|' {
                        if (result == 't' || stack[idx] == 't'){result='t'} else {result='f'}
                    }else if oper == '!' {
                        if (result=='f'){result='t'} else {result='f'}
                    }
                }
                idx--
            }
            stack = stack[:idx]
            stack = append(stack,result)
            stack = append(stack,',')
        }  
    }
    return stack[0]=='t'
}