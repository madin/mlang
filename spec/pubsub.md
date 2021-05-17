
```
var count: number; // count 는 Number 를 pub, sub 할 수 있는 녀석?

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
```

sum 은 number 를 sub 하고 pub 하는 녀석, 

원래는 이렇게 생각했는데
```
type sum {
    total: number = 0;
}


func (self:sum) @consume:begin()
{
    self.total = 0;
}

func (self:sum) @consume:on(value:number)
{
    self.total = self.total + value;
}

func (self:sum) @consume:end(self:sum)
{
    self.publish(self.total)
}
```

생각해보니 이런게 더 맞겠다
```
type sum {
    total: number = 0;
}


func (self:sum) @constructor()
{
    self.total = 0;
}

func (self:sum) @consume(value:number)
{
    self.total = self.total + value;
}

func (self:sum) @destructor()
{
    self.publish(self.total)
}
```

desturctor 에서 Publish 하는게 적절해 보이진 않는다.