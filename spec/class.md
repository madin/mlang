클래스는 존재하지 않고 다 structure + pure function 으로 구성

```
type MyType {
    value: int;
}

func @constructor(self:MyType) {
	self.value = -1;
}

func @destructor(self:MyType) {
}

func @change(self:MyType, value:MyType) {
}

func add(self:MyType, value:int) {
    self.value += value;
}
```

아니면 golang 같은 느낌의 이런 방식도 좋긴 하겠다
```
type MyType {
    value: int;
}

func (self:MyType) @constructor() {
	self.value = -1;
}

func (self:MyType) @destructor() {
}

func (self:MyType) @change(value:MyType) {
}

func (self:MyType) add(value:int) {
    self.value += value;
}
```