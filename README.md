# mlang

다음과 같은 목표로 만들어 보는 게임 개발용 언어
- 스크립팅 지원

- 정적 타입

- 변수에 Semantic 추가 가능
```
semantic Position:Vector3;

type Transform
{
    Position;
    Rotation: Quaternion;
}
```
- 함수형

- 리엑티브
```
(model.Position + Vector3(0,1,0)) => nameTag.Position
// Model Position 이 변경되면 nameTag.Position 도 변경
```

- 타입 믹싱
```
semantic Vector3 Position;

type Tranform
{
    Position;
    Rotation: Quaternion;
}

type Rigidbody
{
    Position;
}

type BaseModel = Transform + Rigidbody;

/* 결과적으로는 BaseModel 은 다음과 같은 구조가 됨
type BaseModel
{
    Position;   // Semantic 을 기준으로 merge
    Rotation: Quaternion;
}
*/
```

- 패치
```
// 어딘가에 정의되어 있는 Semantic
semantic Position: Vector3;

// 메인 모듈에 정의 되어 있는 Semantic
// Position Semantic 을 쓰는 부분이 모두 Vector3  에서 Vector2 로 변경
semantic Position: Vector2;
```

```
semantic HP:number;

type Stat {
    HP;
    MP: number;
}

type Stat += {
    Shield: number;
}

type Stat -= {
    MP;
}

// Stat 이 다음과 같이 수정되며, Stat 을 쓰는 모든 곳이 변경됨
type Stat {
    HP;
    Shield: number;
}
```

- 분산 처리