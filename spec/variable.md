```
var count: int;

count = 1;
count <- 1;     // count = 1 과 동일
1 -> count;     // count = 1 과 동일

count -> (value) { publish value + 1; } -> count;  // 무한 루프
count -> (value) { if value < 100 then publish value + 1; } -> count
count -> if value < 100 -> count + 1 -> count
count -> value + 1 -> count;                       // 무한 루프
count -> count + 1 -> count;    // capture 가 필요

var total: int;
range(100) -> total += value
range(100) -> sum() -> total

/*
sum() -> new sum()
sum 은 number나 int 타입을 subscribe 하고 publish 하는 타입

type sum {
    total: number = 0;
}

func consume:begin(self:sum)
{
    self.total = 0;
}

func consume(self:sum, value:number)
{
    self.total = self.total + value;
}

func consume:end(self:sum)
{
    self.publish(self.total)
}


*/

```

