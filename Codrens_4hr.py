print() # print('string','string') print(#)
input() # input('How old are you?:') 입력을 받음

# Variable name = variable value / 대소문자 구분, 한글, 다른 언어도 가능하나 맥은 잘 안 될수도
VarName = 1

## Data type 1
type(VarName) # 변수 또는 객체의 타입 알 수 있음
# 1. Numbers:float 실수형, int 정수형
# 2. String: 문자형
    'Hello'
    "Hello"
    """ """
    "\"include the marks\" inside this string"

    ## "String" 'String'
    # Docstring: ''' """ 세쌍으로 하면 여러 줄 주석처리 또는 여러 줄 하나의 변수로 가능
    my_str = """ 하나
    둘
    셋"""  #출력 시 \n 줄바꿈 표기되어 한 줄에 출력됨

    ## Formatting %d 정수 %f 실수 %s 문자열 %c 문자1개character %% 퍼센트문자자체 대입 가능
    my_str = "My name is %s" % "Bonnie Oh"
    '%d $d' % (1,2) #여러 개 대입은 (괄호) 사용
    # '{}'.format() 좀 더 파이썬스러운 방식
    'My name is {}'.format('Bonnie Oh')
    '{} x {} = {}'.format(2,3,2*3) #출력 시 2x3=6
    '{1} x {0} = {2}'.format(2,3,2*3) #출력 시 3x2=6: 이렇게 순서 지정 가능

    ## Indexing
    '영일이삼사오' #indexing starts from 0 NOT 1
    '마이너스오사삼이일' #indexing using minus starts from the last word
    ## Slicing: 여러 개 뽑아올 수 있음
    '0p1y2t3h4o5n6' 

    ## Method
    VarName.split() #공백 기준으로 또는 옵션 넣어서 스트링 따로따로 출력됨 ['하나', '둘']

    ## print('', end = '')
    print('무슨말', end = '저런말') #무슨말 뒤에 저런말이 공백 없이 출력됨 
    ## Escape code: 특정 기능 수행하는 문자 조합
    # \n 줄바꿈 \t 인덴테이션 tab
# 3. Boolean: 자료형 True, False 두 가지만 있음

## Data type 2
# 1. List: [ ] 위의 형태들을 모아둔 것
student = [var1, var2, var3]
students [0] = 3 #리스트 속 특정 위치의 값 변경 가능 mutable
    ListName.append() # 리스트 맨 뒤에 변수 추가
    ListName.inster() 

    ## Indexing 리스트 속 요소 단위로 인덱싱 들어감
    del ListName[0] # #'th 요소 지우기
    ## Slicing 리스트 속 요소 단위로 슬라이싱됨
    ## Method
    ListName.sort() # 리스트 가나다, a-z 순서로 정렬 출력
    ListName.count() # 리스트 속 ('str') (#) 특정 요소가 몇 개 있는지 출력

    ## 내장함수
    len(ListName) # 리스트 속 요소의 갯수 출력
# 2. Tuple: ( ) 리스트와 비슷하나 안의 값 바꿀 수 없음 immutable
    # 빈 튜플 생성 가능
    ## Packing 여러 값 하나로 묶기 vs. Unpacking 묶인 값 여러개로 풀기
    TupName = 1, 2, 3 # packing
    num1, num2, num3 = TupName # unpacking
    # num1 출력 시 1 출력 됨
    num1, num2 = num2, num1 # 이제부터 num1 과 num2의 값이 서로 바뀌어 출력 
# 3. Dictionary: {key1: var1, var2, ..} 
my_dict = {'쟤': '남', '나': '여'}
my_dict['나'] #값의 위치를 숫자로 불러내는게 아니라 특정 이름(키)을 붙여주어 그 이름을 불러야 값이 출력됨
my_dict['나'] = '남자도 여자도 아님' #마찬가지로 값 변경은 이런 식으로
    my_dict[0] = 'a' # 0key 에 a 값 삽입
    mydict['b'] = 2 # 'b' key에 2 값 삽입
    #...계속 하면 뒤에 계속 추가됨

    ## Method
    DictName.values() # 딕셔너리의 값만 가져옴
    DictName.keys() # 키만 가져옴
    DictName.items() # 키,값을 같이 가져옴
        for key, val in my_dict.items():
            print(key, val)

## Data type 변환
int() float() str() #각 정수형, 실수형 1.0, 스트링으로 변환

## for Var변수 in Container컨테이너: 
# 컨테이너 속 값이 순서대로 Var 변수에 들어가 그 아래 실행 명령을 순차로 진행 후 둘째 값이 반복됨
# Code block: 반복하는 명령라인들. 들여쓰기 꼭 하기 
    ## 중첩 반복문 예시 구구단
    for j in range(2, 10):
        for i in range(1, 10):
            print('{}X{}={}'.format(j, i, j*i))
    ## Comprehension 리스트를 만드는데 for 나 if 등을 사용해 간결히 만드는 것
    [number for number in numbers if number %2 ==1]

range(10,000) # 0부터 특정 숫자 전까지 또는 특정 숫자부터 특정 숫자 전까지 숫자 자동 입력

""" Operators
Assign: Var += 1 ==  Var = Var +1 이런 기능으로 -= *= /= 다 같은 기능
Arithmetic: + - * / -> + 와 *는 string에도 적용 가능
Spetial arithemetic: ** 제곱 // 나눈 후 몫 % 나머지
Comparison: == 같다 != 다르다 > < >= <= 
Logical: and or not
Membership: 리스트 같은거 안에 어떤 값이 있나 없나 확인 in, not in
    'something' in ListName -> 결과로 True False 출력
"""

## if condition: 조건이 참일때만 코드블럭 들어가고 거짓이면 다음으로 넘어감
# else: if 가 거짓일 경우, elif: 다음 if검사

## Other Loop properties
# While condiiton: 조건이 False가 되면 더이상 돌아가지 않게 됨
While count < 10:
    count += 1
    if count <4:
        continue # True면 밑 문장 실행하지 않고 바로 조건문으로 다시 올라감
    print('횟수:', count)
    if count = 8: 
         break # True면 반복문 그냥 끝내버림

""" Function
def FxName(element1,...):
    command1
    command2
    return Result1, Result2,  -> 이건 있어도 되고 없어도 됨
"""
    def add(num1, num2):
        return num1 + num2

## Module: collection of functions, import 적용해서 사용
# Random module
import random
random.choice(ListName) # 리스트중 렌덤으로 값 추출
random.sample(ListName, 2) # 숫자 갯수의 값 랜덤 중복 없이 추출
random.randint(0,0) #숫자 범위 (0,100) 지정해 그 중 하나 정수 추출

## Object: 현실 물건을 컴퓨터로 재현한 것