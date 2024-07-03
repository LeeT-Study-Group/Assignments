package main

import "fmt"

type MinHeap struct {
	store []int
}

func (*MinHeap) add(val int){
	fmt.Println(val)
}

func main(){
	var obj MinHeap = MinHeap{}
	obj.add(12)
}