# Maps

### Syntax 

```golang
// map with initialized values
var mapName map[keyType]valueType = map[keyType]valueType{
    keyType_value1 : valueType_value1,
    keyType_value2 : valueType_value2,
    keyType_value3 : valueType_value3,
}

mapName := make(map[keyType]valueType) // creates an empty map

// access values of maps by using key
mapName[keyType_value1] // has value - valueType_value1
mapName[keyType_value2] = valueType_value4 // value for the key "keyType_value2" has been changed to value - valueType_value4

mapName[keyType_value4] = keyType_value5 // adding new item to map

delete(mapName, keyType_value5) // deleting the key-value pair

value, ok = mapName[keyType_value5]
// returns the value in "value" if exists and true in "ok", and if the key does not exists returns default in "value" and false in "ok"

len(mapName) // gives the number of elements present in the map
```

### Example

```golang
// initializing and declaration of map
var map1 map[string]int = map[string]int{
	"one":   1,
	"two":   2,
	"three": 3,
}
fmt.Println(map1) // accessing the full map

map1["four"] = 4 // adding the new value to the map

fmt.Println(map1["four"]) // accessing one of the item in map
fmt.Println(map1)

delete(map1, "four") // deleting the item from the map if it exists
fmt.Println(map1)

map2 := make(map[string]string) // another way of making a map(empty map)
fmt.Println(map2)

// checking if the key exists or not
map2["a"] = "A"
map2["b"] = "B"
map2["c"] = "C"
valueOfKey, ok := map2["d"]
fmt.Printf("value of map2[\"d\"] - %q and it exists - %t\n", valueOfKey, ok)
valueOfKey, ok = map2["b"]
fmt.Printf("value of map2[\"b\"] - %q and it exists - %t\n", valueOfKey, ok)

fmt.Println(len(map1), len(map2)) // for getting the number of elements of the map
```

### Output

```
map[one:1 three:3 two:2]
4
map[four:4 one:1 three:3 two:2]
map[one:1 three:3 two:2]
map[]
value of map2["d"] - "" and it exists - false
value of map2["b"] - "B" and it exists - true
3 3
```