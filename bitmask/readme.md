# bitmask
2진법으로 계산해보자!
## WHY?
* 비트연산을 통한 삽입, 삭제, 조회가 가능
* 더 간결한 코드
* 더 빠른연산 가능
* 비트마스크를 이용한 DP 가능(중요!)

## 비트 연산자
### 기본
아래와 같은 형태로 2진수로 표현할 수 있다.
```python
0b11001001 # 201
```

### AND (&)
대응하는 숫자가 모두 1일경우 1을 반환
```python
bin(0b10110010 & 0b11100110) # '0b10100010'
```

### OR (|)
대응하는 숫자가 하나라도 1일경우 1을 반환
```python
bin(0b10110010 | 0b11100110) # '0b11110110'
```

### XOR (^)
대응하는 숫자가 같을 경우 0, 다를 경우 1을 반환
```python
bin(0b10110010 ^ 0b11100110) # '0b1010100'
```

### SHIFT (a << b, a >> b)
b칸 만큼 a의 비트를 화살표 방향으로 밀어낸다.
```python
n = 2
bin(0b10110010 << n) # '0b1011001000'
```
### NOT (~)
bit를 반전시킨다.(Two's complement)
```
0000 0000 -> 1111 1111 -> -1
0000 0001 -> 1111 1110 -> -2
0000 0010 -> 1111 1101 -> -3
```
실제로는 ~a = -1 - a 로 출력된다.


## 푼 문제
* [12813 - 이진수 연산](https://www.acmicpc.net/problem/12813)


