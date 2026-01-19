
package main

import (
    "fmt"
)


type Car struct {
    Brand string 
    Year int 
}

func main() {
    car1 := Car{Brand: "BMW", Year: 2023}
    fmt.Println(car1.Brand)
    fmt.Println(car1.Year)
}

