# 스터디 자료: 스택 / 큐 / 해시테이블

> 대상: 자료구조를 처음 접하는 분들 (Bronze 수준)
> 목표: 세 가지 자료구조의 원리를 이해하고 Python으로 문제를 풀 수 있다

---

## 1. 스택 (Stack)

### 비유로 이해하기

**프링글스 통을 떠올려 보세요.**

과자를 통 위에서 넣으면, 꺼낼 때도 위에서부터 꺼냅니다.
제일 나중에 넣은 과자가 제일 먼저 나옵니다.

```
     ┌───┐
     │ D │  ← 가장 최근에 넣음 (가장 먼저 나옴)
     ├───┤
     │ C │
     ├───┤
     │ B │
     ├───┤
     │ A │  ← 가장 먼저 넣음 (가장 나중에 나옴)
     └───┘
      스택
```

**브라우저 뒤로가기 버튼도 스택입니다.**

```
페이지 방문 순서: 구글 → 네이버 → 유튜브

스택 상태:
┌─────────┐
│  유튜브  │  ← 뒤로가기 누르면 여기서 나옴
├─────────┤
│  네이버  │
├─────────┤
│  구글   │
└─────────┘

뒤로가기 1번 → 유튜브 pop → 네이버로 이동
뒤로가기 2번 → 네이버 pop → 구글로 이동
```

**ctrl+Z (실행 취소)도 스택입니다.**

```
문서 편집 기록:
┌───────────────┐
│  "안녕" 입력  │  ← ctrl+Z 누르면 취소됨
├───────────────┤
│  "hello" 입력 │
├───────────────┤
│  파일 열기    │
└───────────────┘

ctrl+Z 1번 → "안녕" 입력 취소
ctrl+Z 2번 → "hello" 입력 취소
```

---

### push / pop 동작 단계별 추적

```
명령: push(1) → push(2) → push(3) → pop() → push(4) → pop() → pop()

초기:  []

push(1):  [1]
           ↑ top

push(2):  [1, 2]
               ↑ top

push(3):  [1, 2, 3]
                  ↑ top

pop():    [1, 2]      반환값: 3
               ↑ top

push(4):  [1, 2, 4]
                  ↑ top

pop():    [1, 2]      반환값: 4
               ↑ top

pop():    [1]         반환값: 2
           ↑ top
```

---

### 핵심 개념

**LIFO (Last In, First Out)** — 마지막에 넣은 것이 먼저 나온다.

모든 연산은 **O(1)**입니다. push든 pop이든 항상 맨 위(top)에서만 작업하기 때문입니다.

| 연산 | 설명 | 시간복잡도 |
|------|------|-----------|
| push | 스택 맨 위에 값 추가 | O(1) |
| pop | 스택 맨 위의 값 꺼내기 (삭제 + 반환) | O(1) |
| peek / top | 스택 맨 위의 값 보기 (삭제하지 않음) | O(1) |
| is_empty | 스택이 비었는지 확인 | O(1) |
| size | 스택에 저장된 원소 개수 | O(1) |

---

### Python 구현

#### 기본 사용법

Python의 `list`는 스택으로 쓰기 딱 좋습니다.
`append()`가 push, `pop()`이 pop 역할을 합니다.

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
print(stack[-1])

top = stack.pop()
print(top)
print(stack)
```

```
[10, 20, 30]
30
30
[10, 20]
```

#### 빈 스택에서 pop하면 오류

반드시 pop 전에 스택이 비어있는지 확인해야 합니다.

```python
stack = []

if stack:
    print(stack.pop())
else:
    print("스택이 비어있습니다")
```

또는 `-1`을 반환하도록 처리하는 방식이 문제에서 자주 나옵니다.

```python
stack = []

result = stack.pop() if stack else -1
print(result)
```

```
-1
```

#### peek — 꺼내지 않고 맨 위 값만 보기

`stack[-1]`로 맨 위 값을 꺼내지 않고 볼 수 있습니다.

```python
stack = [1, 2, 3]

top = stack[-1]
print(top)
print(stack)
```

```
3
[1, 2, 3]
```

`pop()`과 달리 스택이 그대로 유지됩니다.

#### 스택 전체 순서 뒤집기

스택의 원소를 pop하면 넣은 순서의 반대로 나옵니다. 이를 이용해 리스트를 뒤집을 수 있습니다.

```python
original = [1, 2, 3, 4, 5]
stack = original[:]

reversed_list = []
while stack:
    reversed_list.append(stack.pop())

print(reversed_list)
```

```
[5, 4, 3, 2, 1]
```

#### 클래스로 스택 직접 구현하기

`list`를 감싸서 스택 인터페이스를 명확하게 만들 수 있습니다.

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            return -1
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return -1
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.peek())
print(s.pop())
print(s.size())
print(s.is_empty())
```

```
3
3
2
False
```

#### 괄호 검사 — 스택의 대표적인 활용

열린 괄호를 만나면 스택에 쌓고, 닫힌 괄호를 만나면 스택에서 꺼내 짝이 맞는지 확인합니다.

```python
def is_valid(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


print(is_valid("((()))"))
print(is_valid("(()"))
print(is_valid(")("))
print(is_valid("()()()"))
```

```
True
False
False
True
```

단계별 추적 (`"(())"` 입력 시):

```
문자  스택     설명
'('   ['(']    열린 괄호 → push
'('   ['(','('] 열린 괄호 → push
')'   ['(']    닫힌 괄호 → pop (짝 맞음)
')'   []       닫힌 괄호 → pop (짝 맞음)
끝   []        스택이 비어있음 → True
```

단계별 추적 (`")("` 입력 시):

```
문자  스택   설명
')'   []     닫힌 괄호인데 스택이 비어있음 → 즉시 False 반환
```

#### 연속된 같은 값 제거 (같은 숫자는 싫어 패턴)

스택 top과 현재 값이 같으면 push하지 않습니다.

```python
def remove_consecutive_duplicates(arr):
    stack = []
    for num in arr:
        if not stack or stack[-1] != num:
            stack.append(num)
    return stack


print(remove_consecutive_duplicates([1, 1, 3, 3, 0, 1, 1]))
print(remove_consecutive_duplicates([4, 4, 4, 3, 3]))
```

```
[1, 3, 0, 1]
[4, 3]
```

---

### 연습 문제

| 플랫폼 | 문제 | 난이도 | 핵심 포인트 |
|--------|------|--------|-------------|
| 백준 | [10828 - 스택](https://www.acmicpc.net/problem/10828) | Silver IV | 스택 5가지 연산 직접 구현 |
| 백준 | [9012 - 괄호](https://www.acmicpc.net/problem/9012) | Silver IV | `(` push, `)` pop으로 짝 맞추기 |
| 프로그래머스 | [같은 숫자는 싫어 (Lv.1)](https://school.programmers.co.kr/learn/courses/30/lessons/12906) | Lv.1 | 스택 top과 현재 값 비교 |
| 프로그래머스 | [올바른 괄호 (Lv.2)](https://school.programmers.co.kr/learn/courses/30/lessons/12909) | Lv.2 | 9012와 동일 유형, 프로그래머스 버전 |

**풀이 힌트**

백준 10828: `push X`, `pop`, `size`, `empty`, `top` 명령어를 if문으로 분기한다.

```
명령어    처리 방법
push X  → stack.append(X)
pop     → stack.pop() (비어있으면 -1 출력)
size    → len(stack)
empty   → 1 if not stack else 0
top     → stack[-1] (비어있으면 -1 출력)
```

백준 9012:

```
'(' 만나면 → push
')' 만나면 → 스택이 비어있으면 NO, 아니면 pop
마지막에 → 스택이 비어있으면 YES, 아니면 NO
```

---

## 2. 큐 (Queue)

### 비유로 이해하기

**놀이공원 줄서기를 떠올려 보세요.**

먼저 줄 선 사람이 먼저 탑니다. 새로 온 사람은 줄 맨 뒤에 섭니다.

```
       앞 (front)              뒤 (back)
         ↓                       ↓
  꺼내기 ← [A][B][C][D] ← 넣기

  먼저 온 A가 먼저 나감
  새로 온 사람은 D 뒤에 붙음
```

**편의점 음료 진열대도 큐입니다.**

```
새 음료 투입 (뒤)              오래된 음료 구매 (앞)
      ↓                              ↓
  [신상][2025.01][2024.12][2024.11] →

뒤에서 채우고, 앞에서 꺼냄
오래된 것이 먼저 팔림
```

**프린터 인쇄 대기도 큐입니다.**

```
인쇄 요청 순서: 문서A → 문서B → 문서C

대기열:
앞 [문서A][문서B][문서C] 뒤

프린터는 앞에서부터 차례대로 인쇄
문서A → 문서B → 문서C 순서로 출력
```

---

### enqueue / dequeue 동작 단계별 추적

```
명령: enqueue(A) → enqueue(B) → enqueue(C) → dequeue() → enqueue(D) → dequeue()

초기:  []

enqueue(A):  [A]
              ↑front  ↑back

enqueue(B):  [A, B]
              ↑front       ↑back

enqueue(C):  [A, B, C]
              ↑front            ↑back

dequeue():   [B, C]       반환값: A
              ↑front       ↑back

enqueue(D):  [B, C, D]
              ↑front            ↑back

dequeue():   [C, D]       반환값: B
              ↑front       ↑back
```

---

### 핵심 개념

**FIFO (First In, First Out)** — 먼저 넣은 것이 먼저 나온다.

| 연산 | 설명 | 시간복잡도 |
|------|------|-----------|
| enqueue | 큐 맨 뒤에 값 추가 | O(1) |
| dequeue | 큐 맨 앞의 값 꺼내기 | O(1) |
| front | 큐 맨 앞의 값 보기 (삭제하지 않음) | O(1) |
| back | 큐 맨 뒤의 값 보기 (삭제하지 않음) | O(1) |
| is_empty | 큐가 비었는지 확인 | O(1) |

---

### list.pop(0)이 느린 이유

Python의 `list`는 내부적으로 **배열(array)**로 구현되어 있습니다.
배열에서 맨 앞 원소를 제거하면 나머지를 모두 한 칸씩 앞으로 당겨야 합니다.

```
list = [A, B, C, D, E]
인덱스: 0  1  2  3  4

pop(0) 실행:
  step 1: A 제거
  step 2: B → 인덱스 0으로 이동
  step 3: C → 인덱스 1로 이동
  step 4: D → 인덱스 2로 이동
  step 5: E → 인덱스 3으로 이동

원소 N개를 모두 이동 = O(N)
```

원소가 100만 개라면 맨 앞 하나를 꺼낼 때마다 100만 번의 이동이 발생합니다.

---

### deque가 빠른 이유

`collections.deque`는 **이중 연결 리스트(doubly linked list)**로 구현되어 있습니다.
각 원소가 앞뒤 원소를 가리키는 화살표를 가지고 있습니다.

```
deque 내부 구조:

None ← [A] ↔ [B] ↔ [C] ↔ [D] ↔ [E] → None
        ↑                              ↑
      left_ptr                     right_ptr

popleft() 실행:
  left_ptr를 B로 바꾸고 A 삭제
  = 화살표 하나만 바꾸면 끝 = O(1)

append() 실행:
  right_ptr 뒤에 새 원소 연결
  = 화살표 하나만 추가 = O(1)
```

---

### Python 구현

#### 기본 사용법

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)
print(queue[0])
print(queue[-1])

front = queue.popleft()
print(front)
print(queue)
```

```
deque([10, 20, 30])
10
30
10
deque([20, 30])
```

#### 초기값을 넣어서 생성하기

```python
from collections import deque

queue = deque([1, 2, 3, 4, 5])
print(queue)

queue.append(6)
print(queue)

queue.popleft()
print(queue)
```

```
deque([1, 2, 3, 4, 5])
deque([1, 2, 3, 4, 5, 6])
deque([2, 3, 4, 5, 6])
```

#### 빈 큐에서 dequeue하면 오류

```python
from collections import deque

queue = deque()

if queue:
    queue.popleft()
else:
    print("큐가 비어있습니다")
```

#### 양방향으로 쓰기 — deque의 특징

`deque`는 앞뒤 양방향으로 넣고 꺼낼 수 있어, 스택과 큐를 동시에 사용할 수 있습니다.

```python
from collections import deque

dq = deque()

dq.append(1)
dq.append(2)
dq.append(3)
print(dq)

dq.appendleft(0)
print(dq)

right = dq.pop()
print(right)
print(dq)

left = dq.popleft()
print(left)
print(dq)
```

```
deque([1, 2, 3])
deque([0, 1, 2, 3])
3
deque([0, 1, 2])
0
deque([1, 2])
```

| 연산 | 방향 | 메서드 |
|------|------|--------|
| 오른쪽에 추가 | 큐의 뒤 / 스택의 위 | `append(x)` |
| 왼쪽에 추가 | 큐의 앞 | `appendleft(x)` |
| 오른쪽에서 꺼내기 | 스택의 pop | `pop()` |
| 왼쪽에서 꺼내기 | 큐의 dequeue | `popleft()` |

#### rotate — 원형으로 회전하기

`rotate(n)`은 전체를 오른쪽으로 n칸 회전합니다. 음수를 넣으면 왼쪽으로 회전합니다.

```python
from collections import deque

dq = deque([1, 2, 3, 4, 5])

dq.rotate(2)
print(dq)

dq.rotate(-1)
print(dq)
```

```
deque([4, 5, 1, 2, 3])
deque([5, 1, 2, 3, 4])
```

#### maxlen — 최대 크기 제한

`maxlen`을 지정하면 크기가 초과될 때 반대쪽 원소가 자동으로 제거됩니다.

```python
from collections import deque

recent = deque(maxlen=3)

recent.append("A")
recent.append("B")
recent.append("C")
print(recent)

recent.append("D")
print(recent)

recent.append("E")
print(recent)
```

```
deque(['A', 'B', 'C'], maxlen=3)
deque(['B', 'C', 'D'], maxlen=3)
deque(['C', 'D', 'E'], maxlen=3)
```

최근 N개만 유지해야 하는 상황 (최근 방문 기록, 슬라이딩 윈도우)에 활용합니다.

#### 큐 시뮬레이션 예제 — 카드 뒤집기

카드 1~5가 순서대로 있다. 맨 앞 카드를 버리고, 그 다음 카드를 맨 뒤로 보낸다. 반복.

```
초기: [1, 2, 3, 4, 5]

step 1: 1 버림, 2를 맨 뒤로 → [3, 4, 5, 2]
step 2: 3 버림, 4를 맨 뒤로 → [5, 2, 4]
step 3: 5 버림, 2를 맨 뒤로 → [4, 2]
step 4: 4 버림, 2를 맨 뒤로 → [2]
step 5: 2 버림 → []

버린 순서: 1, 3, 5, 4, 2
```

```python
from collections import deque

cards = deque([1, 2, 3, 4, 5])
result = []

while cards:
    result.append(cards.popleft())
    if cards:
        cards.append(cards.popleft())

print(result)
```

```
[1, 3, 5, 4, 2]
```

#### 클래스로 큐 직접 구현하기

```python
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.is_empty():
            return -1
        return self._data.popleft()

    def front(self):
        if self.is_empty():
            return -1
        return self._data[0]

    def back(self):
        if self.is_empty():
            return -1
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.front())
print(q.back())
print(q.dequeue())
print(q.size())
```

```
1
3
1
2
```

---

### 연습 문제

| 플랫폼 | 문제 | 난이도 | 핵심 포인트 |
|--------|------|--------|-------------|
| 백준 | [10845 - 큐](https://www.acmicpc.net/problem/10845) | Silver IV | 큐 6가지 연산 직접 구현 |
| 백준 | [2164 - 카드2](https://www.acmicpc.net/problem/2164) | Silver IV | 위 예제와 동일한 카드 시뮬레이션 |
| 프로그래머스 | [기능개발 (Lv.2)](https://school.programmers.co.kr/learn/courses/30/lessons/42586) | Lv.2 | 앞에서부터 완료된 기능 묶어서 배포 |
| 프로그래머스 | [프로세스 (Lv.2)](https://school.programmers.co.kr/learn/courses/30/lessons/42587) | Lv.2 | 우선순위 있는 큐 시뮬레이션 |

**풀이 힌트**

백준 10845: 10828(스택)과 구조가 같다. `push`는 `append`, `pop`은 `popleft`, `front`는 `[0]`, `back`은 `[-1]`.

백준 2164:

```
N장 카드: 1, 2, 3, ..., N

while 카드가 2장 이상:
  맨 앞 카드 버림 (popleft → 버림)
  맨 앞 카드 맨 뒤로 이동 (popleft → append)

남은 1장이 정답
```

---

## 3. 해시테이블 (Hash Table)

### 비유로 이해하기

**학교 사물함을 떠올려 보세요.**

사물함 번호(키)만 알면 바로 내 물건(값)을 찾을 수 있습니다.
처음부터 모든 사물함을 열어보지 않아도 됩니다.

```
사물함 번호(키)    물건(값)
     101    →    교과서
     102    →    체육복
     103    →    도시락
     ...
     250    →    내 가방  ← 250번 알면 바로 찾음!
```

**리스트 검색 vs 해시 검색**

```
리스트에서 "도시락" 찾기 — O(N)

[교과서][체육복][도시락][우산][...]
  1번     2번    발견!
  검사    검사    3번 검사

최악의 경우 끝까지 다 확인해야 함
원소가 100만 개면 최대 100만 번 비교


해시에서 "도시락" 찾기 — O(1)

  "도시락"
     ↓
  해시 함수 실행
     ↓
  인덱스 103 계산
     ↓
  인덱스 103 바로 접근 → "도시락" 발견!

단 1번 만에 끝!
```

---

### 해시 함수란?

키(key)를 숫자 인덱스로 변환해주는 함수입니다.
같은 키를 넣으면 항상 같은 숫자가 나옵니다.

```
해시 함수 동작 방식 (개념도)

  키(key)          해시 함수           인덱스
 "apple"    →  hash("apple")  →    7
 "banana"   →  hash("banana") →    3
 "cherry"   →  hash("cherry") →    11

           해시 테이블 (배열)
           인덱스:  0    1    2    3       7      11
                  [   ][   ][   ][banana][apple][cherry]
```

**중요**: 해시 함수는 입력이 완전히 다르더라도 같은 숫자가 나올 수 있습니다. 이를 **해시 충돌(hash collision)**이라고 합니다. Python의 `dict`는 내부적으로 이를 자동으로 처리합니다.

```
예시:

hash("abc") → 5
hash("xyz") → 5  (같은 인덱스!)

→ 해시 충돌 발생
→ Python dict가 내부에서 알아서 해결해줌
→ 우리가 신경 쓸 필요 없음
```

---

### 핵심 개념

- **키-값(Key-Value) 쌍**으로 데이터를 저장한다
- 검색/삽입/삭제 모두 **평균 O(1)**
- Python에서 `dict` = 해시테이블, `set` = 키만 있는 해시테이블

**리스트 vs 해시 성능 비교**

```
원소 1,000,000개에서 특정 값 찾기

리스트:  최악 1,000,000번 비교 (끝에 있으면)
dict:    평균 1번 (해시 함수로 바로 위치 계산)

원소가 많을수록 해시의 장점이 커짐
```

---

### Python 구현

#### dict (딕셔너리) — 기본 사용법

```python
d = {}

d["사과"] = 1000
d["바나나"] = 500
d["체리"] = 3000

print(d)
print(d["사과"])
print(len(d))
```

```
{'사과': 1000, '바나나': 500, '체리': 3000}
1000
3
```

#### dict — 값 수정과 삭제

```python
d = {"사과": 1000, "바나나": 500}

d["사과"] = 1200
print(d)

del d["바나나"]
print(d)

removed = d.pop("사과")
print(removed)
print(d)
```

```
{'사과': 1200, '바나나': 500}
{'사과': 1200}
1200
{}
```

#### dict — 없는 키에 접근할 때

없는 키에 `[]`로 접근하면 `KeyError`가 발생합니다. `get()`을 쓰면 기본값을 반환합니다.

```python
d = {"사과": 1000}

print(d.get("사과"))
print(d.get("딸기"))
print(d.get("딸기", 0))
```

```
1000
None
0
```

#### dict — 키 존재 여부 확인

```python
d = {"사과": 1000, "바나나": 500}

print("사과" in d)
print("딸기" in d)
print("딸기" not in d)
```

```
True
False
True
```

#### dict — 전체 순회 방법

```python
d = {"사과": 1000, "바나나": 500, "체리": 3000}

for key in d:
    print(key)

print("---")

for value in d.values():
    print(value)

print("---")

for key, value in d.items():
    print(f"{key}: {value}원")
```

```
사과
바나나
체리
---
1000
500
3000
---
사과: 1000원
바나나: 500원
체리: 3000원
```

#### dict — 빈도수 세기 패턴

문제에서 가장 자주 나오는 패턴입니다.

```python
words = ["사과", "바나나", "사과", "체리", "바나나", "사과"]

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 0 + 1
print(freq)
```

```
{'사과': 3, '바나나': 2, '체리': 1}
```

`get(key, 0)`을 쓰면 더 간결합니다.

```python
words = ["사과", "바나나", "사과", "체리", "바나나", "사과"]

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)
```

```
{'사과': 3, '바나나': 2, '체리': 1}
```

#### dict — 그룹핑 패턴

같은 속성을 가진 원소들을 묶을 때 사용합니다.

```python
students = [
    ("수학", "홍길동"),
    ("영어", "이순신"),
    ("수학", "강감찬"),
    ("영어", "유관순"),
    ("과학", "세종대왕"),
]

groups = {}
for subject, name in students:
    if subject not in groups:
        groups[subject] = []
    groups[subject].append(name)

for subject, names in groups.items():
    print(f"{subject}: {names}")
```

```
수학: ['홍길동', '강감찬']
영어: ['이순신', '유관순']
과학: ['세종대왕']
```

---

#### set (집합) — 기본 사용법

`set`은 키만 있는 해시테이블입니다. **중복을 허용하지 않고**, 존재 여부를 O(1)로 확인합니다.

```python
s = set()

s.add("서울")
s.add("부산")
s.add("서울")

print(s)
print(len(s))

s.remove("부산")
print(s)
```

```
{'서울', '부산'}
2
{'서울'}
```

#### set — 존재 여부 확인

```python
visited = {"서울", "부산", "대구"}

print("서울" in visited)
print("광주" in visited)
print("광주" not in visited)
```

```
True
False
True
```

#### set — 리스트로 만들기, 리스트에서 만들기

```python
fruits = ["사과", "바나나", "사과", "체리", "바나나"]

unique_fruits = set(fruits)
print(unique_fruits)

unique_list = list(unique_fruits)
print(unique_list)
```

```
{'사과', '바나나', '체리'}
['사과', '바나나', '체리']
```

중복 제거에 가장 많이 씁니다.

#### set — 집합 연산

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(a ^ b)
```

```
{1, 2, 3, 4, 5, 6, 7, 8}
{4, 5}
{1, 2, 3}
{6, 7, 8}
{1, 2, 3, 6, 7, 8}
```

| 연산 | 기호 | 메서드 | 설명 |
|------|------|--------|------|
| 합집합 | `a \| b` | `a.union(b)` | a 또는 b에 있는 것 |
| 교집합 | `a & b` | `a.intersection(b)` | a와 b 둘 다 있는 것 |
| 차집합 | `a - b` | `a.difference(b)` | a에는 있고 b에는 없는 것 |
| 대칭차집합 | `a ^ b` | `a.symmetric_difference(b)` | 한쪽에만 있는 것 |

---

#### Counter — 개수 세기 특화

`Counter`는 `dict`를 상속받아 개수를 세는 데 특화된 클래스입니다.

```python
from collections import Counter

fruits = ["사과", "바나나", "사과", "체리", "바나나", "사과"]
c = Counter(fruits)

print(c)
print(type(c))
print(c["사과"])
print(c["없는것"])
```

```
Counter({'사과': 3, '바나나': 2, '체리': 1})
<class 'collections.Counter'>
3
0
```

일반 `dict`와 달리, 없는 키를 조회해도 `KeyError` 대신 `0`을 반환합니다.

#### Counter — 문자열에서 사용

```python
from collections import Counter

c = Counter("mississippi")
print(c)
```

```
Counter({'s': 4, 'i': 4, 'p': 2, 'm': 1})
```

#### Counter — most_common

가장 많이 나온 순서대로 반환합니다.

```python
from collections import Counter

c = Counter(["사과", "바나나", "사과", "체리", "바나나", "사과"])

print(c.most_common())
print(c.most_common(2))
print(c.most_common(1)[0][0])
```

```
[('사과', 3), ('바나나', 2), ('체리', 1)]
[('사과', 3), ('바나나', 2)]
사과
```

#### Counter — 산술 연산

```python
from collections import Counter

a = Counter({"사과": 3, "바나나": 2})
b = Counter({"사과": 1, "바나나": 4, "체리": 1})

print(a + b)
print(a - b)
print(a & b)
print(a | b)
```

```
Counter({'바나나': 6, '사과': 4, '체리': 1})
Counter({'사과': 2})
Counter({'사과': 1, '바나나': 2})
Counter({'바나나': 4, '사과': 3, '체리': 1})
```

`a - b`는 양수인 것만 남습니다. `a`에서 `b`를 빼서 0 이하가 되는 키는 결과에서 제거됩니다. 이 특성을 이용한 것이 "완주하지 못한 선수" 문제입니다.

---

#### defaultdict — 기본값 자동 생성

없는 키에 접근하면 지정한 타입의 기본값을 자동으로 만들어 줍니다.

```python
from collections import defaultdict

d = defaultdict(int)

d["사과"] += 1
d["사과"] += 1
d["바나나"] += 1

print(dict(d))
```

```
{'사과': 2, '바나나': 1}
```

일반 `dict`였다면 처음 `d["사과"] += 1` 에서 `KeyError`가 발생합니다.
`defaultdict(int)`는 없는 키에 접근 시 자동으로 `0`을 만들어주기 때문에 `+= 1`이 가능합니다.

```python
from collections import defaultdict

d_list = defaultdict(list)

d_list["수학"].append("홍길동")
d_list["수학"].append("강감찬")
d_list["영어"].append("이순신")

print(dict(d_list))
```

```
{'수학': ['홍길동', '강감찬'], '영어': ['이순신']}
```

| 사용 방법 | 기본값 |
|----------|--------|
| `defaultdict(int)` | `0` |
| `defaultdict(list)` | `[]` |
| `defaultdict(set)` | `set()` |
| `defaultdict(str)` | `""` |

---

### 자주 나오는 해시 활용 패턴 정리

**패턴 1: 원소 존재 여부 O(1) 확인**

```python
data = [3, 1, 4, 1, 5, 9, 2, 6]
lookup = set(data)

queries = [1, 7, 9, 10]
for q in queries:
    print(q, "있음" if q in lookup else "없음")
```

```
1 있음
7 없음
9 있음
10 없음
```

**패턴 2: 중복 원소 제거**

```python
arr = [1, 3, 2, 3, 1, 5, 2]
unique = list(set(arr))
print(unique)
```

```
[1, 2, 3, 5]
```

순서가 중요하다면 `dict.fromkeys()`를 씁니다 (Python 3.7+에서 삽입 순서 보장).

```python
arr = [1, 3, 2, 3, 1, 5, 2]
unique_ordered = list(dict.fromkeys(arr))
print(unique_ordered)
```

```
[1, 3, 2, 5]
```

**패턴 3: 두 리스트의 차이 찾기**

```python
from collections import Counter

participant = ["홍길동", "이순신", "이순신"]
completion = ["이순신"]

diff = Counter(participant) - Counter(completion)
print(list(diff.keys())[0])
```

```
이순신
```

Wait, participant에서 이순신이 2명, completion에서 1명 → 차이는 이순신 1명, 홍길동 1명.

```python
from collections import Counter

participant = ["홍길동", "이순신", "이순신"]
completion = ["이순신"]

diff = Counter(participant) - Counter(completion)
print(diff)
```

```
Counter({'홍길동': 1, '이순신': 1})
```

---

### 연습 문제

| 플랫폼 | 문제 | 난이도 | 핵심 포인트 |
|--------|------|--------|-------------|
| 백준 | [10815 - 숫자 카드](https://www.acmicpc.net/problem/10815) | Silver V | set으로 존재 여부 O(1) 확인 |
| 백준 | [7785 - 회사에 있는 사람](https://www.acmicpc.net/problem/7785) | Silver V | set으로 입/퇴근 기록 관리 |
| 프로그래머스 | [폰켓몬 (Lv.1)](https://school.programmers.co.kr/learn/courses/30/lessons/1845) | Lv.1 | set으로 종류 개수 세기 |
| 프로그래머스 | [완주하지 못한 선수 (Lv.1)](https://school.programmers.co.kr/learn/courses/30/lessons/42576) | Lv.1 | Counter로 참가자-완주자 차이 찾기 |

**풀이 힌트**

백준 10815:

```python
import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))

m = int(input())
queries = list(map(int, input().split()))

print(*[1 if q in cards else 0 for q in queries])
```

백준 7785:

```python
import sys
input = sys.stdin.readline

n = int(input())
status = set()

for _ in range(n):
    name, action = input().split()
    if action == "enter":
        status.add(name)
    else:
        status.discard(name)

for name in sorted(status, reverse=True):
    print(name)
```

프로그래머스 완주하지 못한 선수:

```python
from collections import Counter

def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    return list(diff.keys())[0]
```

---

## 4. 자료구조 비교 요약

| | 스택 (Stack) | 큐 (Queue) | 해시테이블 |
|---|---|---|---|
| 핵심 원리 | LIFO | FIFO | 키-값 매핑 |
| 비유 | 프링글스 통 | 놀이공원 줄 | 사물함 |
| Python | `list` | `collections.deque` | `dict`, `set` |
| 넣기 | `append(x)` | `append(x)` | `d[key] = val` / `s.add(x)` |
| 꺼내기 | `pop()` | `popleft()` | `d.pop(key)` / `s.discard(x)` |
| 조회 | `stack[-1]` | `queue[0]` | `d[key]` / `key in s` |
| 시간복잡도 | O(1) | O(1) | O(1) 평균 |
| 사용 시점 | 되돌리기, 괄호 검사 | 순서대로 처리, BFS | 빠른 검색, 중복 제거 |

### 언제 어떤 자료구조를 쓸까?

```
"가장 최근 것부터 처리해야 해"
→ 스택 (최근 방문 기록, 실행 취소, 괄호 검사)

"먼저 온 것부터 처리해야 해"
→ 큐 (줄서기, 프린터 대기, BFS)

"이 값이 존재하는지 빠르게 알고 싶어"
→ set (중복 제거, 존재 확인, O(1) 검색)

"이 키에 해당하는 값을 빠르게 찾고 싶어"
→ dict (전화번호부, 점수 기록, 빈도수 세기)

"각 원소가 몇 번 등장했는지 세고 싶어"
→ Counter (가장 많이 나온 것 찾기, 두 목록 비교)

"없는 키에 접근해도 에러 없이 처리하고 싶어"
→ defaultdict (그룹핑, 자동 초기화)
```

---

## 5. Python 핵심 도구 정리

### collections.deque 전체 메서드

```python
from collections import deque

dq = deque([1, 2, 3])

dq.append(4)
dq.appendleft(0)
print(dq)

dq.pop()
dq.popleft()
print(dq)

dq.extend([10, 20])
print(dq)

dq.extendleft([30, 40])
print(dq)

dq.rotate(2)
print(dq)

print(len(dq))
print(dq[0])
print(dq[-1])
print(list(dq))
```

```
deque([0, 1, 2, 3, 4])
deque([1, 2, 3])
deque([1, 2, 3, 10, 20])
deque([40, 30, 1, 2, 3, 10, 20])
deque([10, 20, 40, 30, 1, 2, 3])
7
10
3
[10, 20, 40, 30, 1, 2, 3]
```

`extendleft`는 각 원소를 왼쪽에 하나씩 추가하므로 순서가 뒤집힙니다.

### collections.Counter 전체 메서드

```python
from collections import Counter

c = Counter("aabbccca")

print(c)
print(c["a"])
print(c["z"])
print(c.most_common(2))
print(list(c.elements()))
print(sum(c.values()))

c.update("aab")
print(c)

c.subtract("aa")
print(c)
```

```
Counter({'a': 3, 'c': 3, 'b': 2})
3
0
[('a', 3), ('c', 3)]
['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c']
8
Counter({'a': 5, 'c': 3, 'b': 3})
Counter({'a': 3, 'c': 3, 'b': 3})
```

| 메서드 | 설명 |
|--------|------|
| `c[key]` | 해당 키의 개수 (없으면 0) |
| `c.most_common(n)` | 가장 많은 n개를 (키, 개수) 튜플 리스트로 반환 |
| `c.elements()` | 각 원소를 개수만큼 반복한 이터레이터 |
| `c.update(iterable)` | 개수를 더함 |
| `c.subtract(iterable)` | 개수를 뺌 (음수 허용) |
| `sum(c.values())` | 전체 원소 개수 합 |

### collections.defaultdict 전체 활용

```python
from collections import defaultdict

d_int = defaultdict(int)
for ch in "aabbccc":
    d_int[ch] += 1
print(dict(d_int))

d_list = defaultdict(list)
pairs = [("A", 1), ("B", 2), ("A", 3), ("B", 4)]
for key, val in pairs:
    d_list[key].append(val)
print(dict(d_list))

d_set = defaultdict(set)
for key, val in pairs:
    d_set[key].add(val)
print(dict(d_set))
```

```
{'a': 2, 'b': 2, 'c': 3}
{'A': [1, 3], 'B': [2, 4]}
{'A': {1, 3}, 'B': {2, 4}}
```

---

## 전체 연습 문제 목록

### 스택

| 번호 | 문제 | 플랫폼 | URL |
|------|------|--------|-----|
| 1 | 10828 - 스택 | 백준 | https://www.acmicpc.net/problem/10828 |
| 2 | 9012 - 괄호 | 백준 | https://www.acmicpc.net/problem/9012 |
| 3 | 같은 숫자는 싫어 | 프로그래머스 | https://school.programmers.co.kr/learn/courses/30/lessons/12906 |
| 4 | 올바른 괄호 | 프로그래머스 | https://school.programmers.co.kr/learn/courses/30/lessons/12909 |

### 큐

| 번호 | 문제 | 플랫폼 | URL |
|------|------|--------|-----|
| 5 | 10845 - 큐 | 백준 | https://www.acmicpc.net/problem/10845 |
| 6 | 2164 - 카드2 | 백준 | https://www.acmicpc.net/problem/2164 |
| 7 | 기능개발 | 프로그래머스 | https://school.programmers.co.kr/learn/courses/30/lessons/42586 |
| 8 | 프로세스 | 프로그래머스 | https://school.programmers.co.kr/learn/courses/30/lessons/42587 |

### 해시테이블

| 번호 | 문제 | 플랫폼 | URL |
|------|------|--------|-----|
| 9 | 10815 - 숫자 카드 | 백준 | https://www.acmicpc.net/problem/10815 |
| 10 | 7785 - 회사에 있는 사람 | 백준 | https://www.acmicpc.net/problem/7785 |
| 11 | 폰켓몬 | 프로그래머스 | https://school.programmers.co.kr/learn/courses/30/lessons/1845 |
| 12 | 완주하지 못한 선수 | 프로그래머스 | https://school.programmers.co.kr/learn/courses/30/lessons/42576 |
