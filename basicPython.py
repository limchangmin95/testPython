# ※문제 1번
# station = ['사당', '신도림', '인천공항']
# for i in station:
#  print(i +'행 열차가 들어오고 있습니다.')

# ※숫자처리함수

# from math import *
# print(floor(4.99)) 내림
# print(ceil(4.99)) 올림
# print(round(4.99)) 반올림
# print(sqrt(4.99)) 제곱근

# ※랜덤함수 

# from random import *
# print(1+ int(random() * 45))
# print(4+ int(random()*28))
# print(randrange(4, 29))
# print(randint(4,28))
# day1 = 4 + int(random()*28)
# day2 = randrange(4, 29)
# day3 = randint(4,28)

# ※문제 2번
# print('오프라인 스터디 모임 날짜는 매월' , str(day1) ,'일로 선정되었습니다.')
# print('오프라인 스터디 모임 날짜는 매월' , str(day2) ,'일로 선정되었습니다.')
# print('오프라인 스터디 모임 날짜는 매월' , str(day3) ,'일로 선정되었습니다.')

# ※문자열 슬라이스
# aaa = '951028-1000000'
# print('성별:' + aaa[7])
# print('연 : ' + aaa[0:2]) 
# print('월 : ' + aaa[2:4])
# print('일 : ' + aaa[4:6])
# print('생년월일 : ' + aaa[:6])
# print('생년월일 : ' + aaa[-7:])

# ※문자열 처리함수

# a = 'Python is Amazing'
# print(a.lower())
# print(a.upper())
# print(a[0].isupper())
# print(len(a))
# print(a.replace('Python','Ruby'))

# index = a.index('i')
# print(index)
# b = a.index('i', index + 1)
# print(b)
# print(a.find('b'))

# ※문자열 포맷

# 방법1
# print('나는 %d살입니다.' % 20)
# print('나는 %s살입니다.' % '20')
# print('나는 %c살입니다.' % 'A')
# print('나는 %s색과 %s색을 좋아해요' % ('파랑','빨강'))

# 방법2
# print('나는 {}색과 {}색을 좋아해요'.format('파랑','빨강'))
# print('나는 {0}색과 {1}색을 좋아해요'.format('파랑','빨강'))
# print('나는 {1}색과 {0}색을 좋아해요'.format('파랑','빨강'))

# 방법3
# print('나는 {color}색과 {color2}색을 좋아해요'.format(color ='파랑', color2='빨강'))

# 방법4
# color = '파랑'
# color2= '빨강'
# print(f'나는 {color}색과 {color2}색을 좋아해요')

# ※탈출문자
# print('백문이 붙여일견\n백견이 붙여일타')
# \", \' : 문장 내에서 따옴표
# print("저는 \"임창민\"입니다.") 저는 "임창민"입니다.
# \\ : 문장 내에서 \
# print("C:\\pythonhome\\Third\\week")
# \r : 커서를 맨 앞으로 이동
# print('Red Apple \rPine') PineApple
# \b : 백스페이스 (한글자 삭제)
# print('Redd\bApple') RedApple
# \t : 탭
# print('Redd\tApple') Redd    Apple

# ※문제 3번
# 예) http://naver.com
# a = 'http://naver.com'
# a = a.replace('http://', '')
# a = a[:a.index('.')]

# c = a[:3]
# d = len(a)
# e = a.count('e')
# print('생성된 비밀번호 : {0}{1}{2}!'.format(c,d,e))
# print(f'생성된 비밀번호 : {c}{d}{e}!')

# ※리스트
# a = ['유재석', '조세호', '임창민']
# print(a.index('임창민'))
# a.append('이보현')
# print(a)
# a.insert(1,'정형돈')
# print(a)
# print(a.pop()) 맨뒤에서 하나씩 빼기
# print(a)
# a.append('임창민')
# print(a.count('임창민'))

# ※정렬
# num_list = [5,2,4,1,3]
# mix_list = ['임창민',20,True]
# print(num_list)
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)
# num_list.clear()
# print(num_list)

# num_list.extend(mix_list)
# print(num_list)

# a = {1:'임창민', 5:'유재석'}
# print(a[1])
# print(a.get(5)) 유재석
# print(a.get(6)) None
# print(a.get(6, '이보현')) 이보현

# print(1 in a) True
# print(2 in a) False
# del a[5]
# print(a)
# key 들만 출력
# print(a.keys())
# value 들만 출력
# print(a.values())
# key, value 쌍으로 출력
# print(a.items())
# key, value 전부삭제
# a.clear()
# print(a)

# ※튜플: 1.리스트보다 빠름 2.따로 추가(add or insert)는 안됨
# menu = ('돈까스', '치즈까스')
# print(menu[0])
# print(menu[1])
# (a, b, c) = ('임창민', 28 ,'이보현')
# print((a, b, c))

# ※세트 : 1.set 2.중복안됨 3.순서없음
# my_set = {1,2,3,3,3}
# print(my_set)
# a = {'임창민','유재석','임창민'}
# b = set(['1', '임창민'])
# print(a)
# print(a & b)
# print(a.intersection(b))
# print(a | b)
# print(a.union(b))
# print(a - b)
# print(a.difference(b))
# b.add('이보현')
# print(b)
# b.remove('임창민')
# print(b)

# ※자료구조의 변경
# menu = {'임창민', '이보현','유재석'}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))
# menu = tuple(menu)
# print(menu, type(menu))
# menu = set(menu)
# print(menu, type(menu))

# ※문제4
# from random import *
# c = []
# for i in range(1,21):
#  c.append(i)
# shuffle(c)
# d = sample(c, 1)
# print(int(d))

# c.remove(sample(c, 1))
# print(c)
# print(list(sample(c,3)))

# print('-- 당첨자 발표 --')
# print('치킨 당첨자' + a)
# # print('커피 당첨자' + b)
# print('-- 축하합니다 --')

# ※if 문
# we = input('오늘날씨 어때요?')
# if we == '비':
#     print('우산을 챙기세요')
# elif we == '미세먼지':
#     print('마스크를 챙기세요')
# else:
#     print('준비물 필요없어요')

# temp = int(input('기온은 어때요?'))
# if 30 <= temp:
#     print('너무 더워요')
# elif 10 <= temp | 30 > temp:
#     print('괜찮은 날씨에요')
# elif 0<= temp < 10:
#     print('외투를 챙기세요')
# else:
#     print('너무 추워여')

# ※for 문
# for i in range(1, 5):
#     print(str(i), '111')
# star = ['아이언맨', '토르', '아이엠 그루트']
# for i in star:
#     print('{0}, 커피가 준비되었습니다.'.format(i))

# ※while 문
# we = '토르'
# index = 5
# while index >= 1:
#     print('{0}, 커피가 준비되었습니다. {1}번 남았어요.'.format(we, index))
#     index -= 1
#     if index == 0:
#         print('커피는 폐기처분 되었습니다.')
    
# cus = '아이언맨'
# person = 'Unknown'
# while person != cus:
#     print('{0}, 커피가 준비됨'.format(cus))
#     person = input('이름이 어떻게 되세요?')

# ※continue, break
# absent = [2, 5]
# no = [7]
# for stu in range(1,11):
#     if stu in absent:
#         continue
#     elif stu in no:
#         print('오늘 수업 끝 {0}은 교무실로 와'.format(stu))
#         break
#     print('{0}, 책을 읽어줘'.format(stu))

# ※한줄 for
# stu =[1,2,3,4,5]
# stu = [i+100 for i in stu]
# print(stu)

# stu = ['Iron man', 'Thor', 'I am groot']
# stu = [len(i) for i in stu]
# print(stu)

# stu = ['Iron man', 'Thor', 'I am groot']
# stu = [i.upper() for i in stu]
# print(stu)

# ※문제 5번 
# from random import *
# count = 0
# for i in range(1, 51):
#     num = int(5+(random() * 45))
#     if 5 <= num and num <= 15:
#          print('[O] {0}번째 손님 (소요시간 : {1}분)'.format(i, num))
#          count += 1
#          continue
#     print('[] {0}번째 손님 (소요시간 : {1}분)'.format(i, num))
         
# print('총 탑승 승객 : {0}분'.format(count))  

# ※함수
# def tt():
#     print('22')
# tt()
# def aaa(a ,b):
#     print('입금이 완료되었습니다. 잔액은 {0} 원입니다.'.format(a+b))
#     return a+ b
# bbb = 0     
# print(aaa(bbb, 5))

# ※기본값
# def profile(name, age = 28, main_lag):
#     print('이름 : {0}\t나이 : {1}\t주 사용언어 : {2}'.format(name, age, man))

# profile('임창민','자바')

# ※키워드 값
# def profile(name, age, main_lag):
#     print(name, age, main_lag)
# profile(main_lag = '파이썬', name = '임창민', age = 28)
# profile(age = 29, name = '이보현', main_lag = '자바')

# ※가변인자
# def profile(name, age, *lang):
#     print('이름 = {0}\t나이 = {1}'.format(name, age), end = " ")
#     for i in lang:
#         print(i, end = ' ')
#     print()
# profile('임창민', 28, '파이썬', '자바', '루비')
# profile('이보현', 29, 'swift', '자바')

# ※지역변수 전역변수
# gun = 10
# def checkpoint(sol):
#     global gun 
#     gun = gun - sol
#     print('[함수 내] 남은 총 : {0}'.format(gun))

# def checkpoint_return(gun, sol):
#     gun = gun - sol
#     print('[함수 내] 남은 총 : {0}'.format(gun))
#     return gun

# print('전체 총 : {0}'.format(gun))
# # checkpoint(4)
# gun = checkpoint_return(gun, 4)
# print('남은총 : {0}'.format(gun))

# ※문제 6번
# def std_weight(height, gender):
#     if gender == '남자':
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175
# gender = '남자'
# weight = round(std_weight(height / 100, gender), 2)  
# print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height, gender, weight))

# ※표준 입출력
# print('임창민', '이보현', sep=',')
# print('임창민', '이보현 무엇이 더 재밌을까여', sep=',', end='?')
# import sys
# print('Python', 'Java', file= sys.stdout)
# print('Python', 'Java', file= sys.stderr)

# score = {'수학': 0, '영어' : 50 ,'코딩': 90}
# for sub, score in score.items():
    #  print(sub, score)
#     print(sub.ljust(3), str(score).rjust(4), sep = ':')
# for i in range(1,21):
#     print('대기번호 : ' + str(i).zfill(2))

# answer = input('아무값이나 입력하세요 : ')
# print(type(answer))
# print('입력하신값은 ' + answer + '입니다.')

# ※다양한 출력 포맷
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print('{0: >10}'.format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print('{0: >+10}'.format(500))
# print('{0: >+10}'.format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
# print('{0:_<+10}'.format(500))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print('{0:+,}'.format(100000000000))
# print('{0:+,}'.format(-100000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니깐 빈 자리는 ^로 채우주기
# print('{0:^<+30,}'.format(100000000000))
# 소수점을 출력
# print('{0:f}'.format(5/3))
# 소주점을 특정 자리수 까지만 표시
# print('{0:.3f}'.format(5/3))

# ※파일 입출력
# 파일 작성하기
# score_file = open('score.txt','w',encoding = 'utf8')
# print('수학 : 0', file = score_file)
# print('영어 : 60', file = score_file)
# score_file.close()
# 작성된 파일에 이어 작성하기
# score_file = open('score.txt','a', encoding= 'utf8')
# score_file.write('과학 : 80\n')
# score_file.write('코딩 : 100')
# score_file.close()
# 파일 열기
# score_file = open('score.txt','r', encoding = 'utf8')
# print(score_file.read())
# score_file.close()
# score_file = open('score.txt','r', encoding = 'utf8')
# print(score_file.readline(), end ='') # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end ='') 
# print(score_file.readline(), end ='') 
# print(score_file.readline(), end ='') 
# score_file.close()
# score_file = open('score.txt','r', encoding = 'utf8')
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end= '')
# score_file.close()
# score_file = open('score.txt','r', encoding = 'utf8')
# lines = score_file.readlines() # list 형태로 저장
# for i in lines:
#     print(i, end='')
# score_file.close()

# ※pickle(프로그램에 있는 데이터를 파일형태로 저장)
# import pickle
# profile_file = open('profile.pickle','wb') # w : 쓰기 , b: 바이너리
# profile = {'이름':'임창민', '나이': 28, '취미':['유튜브','넷플', '등산']}
# print(profile)
# pickle.dump(profile, profile_file) # 프로필에 있는 정보를 file에 저장
# profile_file.close()
# profile_file = open('profile.pickle','rb')
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# ※with 
# import pickle
# with open('profile.pickle','rb') as profile_file:
#     print(pickle.load(profile_file))
# with open('study.txt', 'w', encoding= 'utf8') as study_file:
#     study_file.write('파이썬을 열심히 공부하고 있어요.')

# with open('study.txt', 'r', encoding= 'utf8') as study_file:
#     print(study_file.read())

# ※문제 7번
# for i in range(1, 51):
#     with open('{0}주차.txt'.format(i), 'w', encoding= 'utf8') as report_file:
#         report_file.write("""
#         - {0}주차 주간 보고-
#         부서 : 개발부
#         이름 : 임창민
#         업무요약 : 
#         """.format(i))

# ※클래스
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print('{0} 유닛이 생성되었습니다.'.format(self.name))
#         print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

# marine1 = Unit('마린', 40, 5)
# marine2 = Unit('마린', 40, 5)
# tank1 = Unit('탱크', 150, 35)
# tank2 = Unit('탱크', 150, 35)

# wraith1 = Unit('레이스', 80, 5)
# print(wraith.name, wraith.damage)

# wraith2 = Unit('레이스', 80, 5)
# wraith2.clocking = True
# if wraith1.clocking == True:
    # print('{0} 는 현재 클로킹 상태입니다.'.format(wraith2.name))

# ※메소드
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
    
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]'.format(\
#             self.name, location, self.damage))

#     def damaged(self, damage):
#         print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
#         self.hp -= damage
#         print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
#         if self.hp <= 0: 
#             print('{0} : 파괴되었습니다.'.format(self.name))

# firebat = AttackUnit('파이어뱃',50, 16)
# firebat.attack('5시')
# firebat.damaged(25)
# firebat.damaged(25)

# ※상속
# class Unit: # 부모 클래스
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
       
# class AttackUnit(Unit): # 자식클래스, 상속
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp) # 부모클래스의 name과 hp를 사용
#         self.damage = damage
    
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]'.format(\
#             self.name, location, self.damage))

#     def damaged(self, damage):
#         print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
#         self.hp -= damage
#         print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
#         if self.hp <= 0: 
#             print('{0} : 파괴되었습니다.'.format(self.name))


# firebat = AttackUnit('파이어뱃', 50, 16)
# firebat.attack('5시')
# firebat.damaged(25)
# firebat.damaged(25)

# ※다중상속(부모가 다중)
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print('{0} 유닛이 생성되었습니다.'.format(self.name))

#     def move(self, location):
#         print('[지상 유닛 이동]') 
#         print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
#         self.hp -= damage
#         print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
#         if self.hp <= 0: 
#             print('{0} : 파괴되었습니다.'.format(self.name))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
    
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]'.format(\
#             self.name, location, self.damage))

# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, '마린', 40, 1, 5)

#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print('{0} : 스팀팩을 사용합니다. (HP 10 감소)'.format(self.name))
#         else:
#             print('{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.'.format(self.name))

# class Tank(AttackUnit):
#     seize_developed = False

#     def __init__(self):
#         AttackUnit.__init__(self, '탱크', 150, 1, 35)
#         self.seize_mode = False     

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         if self.seize_mode == False:
#             print('{0} : 시즈모드로 전환합니다.'.format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         else:
#             print('{0} : 시즈모드를 해제합니다.'.format(self.name))
#             self.damage /= 2
#             self.seize_mode = False   

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
        
#     def fly(self, name, location):
#         print('{0} : {1}방향으로 날아갑니다. [속도 {2}]'\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print('[공중유닛 이동]')
#         self.fly(self.name, location)

# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self,'레이스', 80, 20, 5)
#         self.clocked = False       

#     def clocking(self):
#         if self.clocked == True:
#             print('{0} : 클로킹 모드 해제합니다.'.format(self.name))
#             self.clocked = False    
#         else:
#             print('{0} : 클로킹 모드 설정합니다.'.format(self.name))
#             self.clocked == True


# valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
# valkyrie.fly('발키리', '3시')
# valkyrie.damaged(50)
# valkyrie.attack('5시')
# vulture = AttackUnit('벌쳐', 80, 10, 20)
# battlescruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)
# vulture.move('3시')
# battlescruiser.fly('배틀크루저', '9시')
# battlescruiser.move('9시')

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#        # Unit.__init__(self, name, hp, 0) # 아랫줄이랑 같은것임, 그대신 다중상속은 안됨
#        super().__init__(name, hp, 0)
#        self.location = location

# supply_depot = BuildingUnit('서플라이 디폿', 500, '7시')

# def game_start():
#     print('[알림] 새로운 게임을 시작합니다.')

# def game_over():
#     print('Player : GG')
#     print('[Player] 님이 게임에서 퇴장하셨습니다.')

# from random import *

# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)


# for i in attack_units:
#     i.move('1시')

# Tank.seize_developed = True
# print('[알림] 탱크 시즈모드 개발이 완료되었습니다.')

# for i in attack_units:
#     if isinstance(i, Marine):
#         i.stimpack()
#     elif isinstance(i, Tank):
#         i.set_seize_mode()
#     elif isinstance(i, Wraith):
#         i.clocking()

# for i in attack_units:
#     i.attack('1시')

# for i in attack_units:
#     i.damaged(randint(5, 21))

# game_over()

# ※문제 8
# class House:

#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print('{0} {1} {2} {3} {4}'.format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))

# house = []

# house1 = House('강남', '아파트', '매매', '10억', '2010년')
# house2 = House('마포', '오피스텔', '전세', '5억', '2007년')
# house3 = House('송파', '빌라', '월세', '500/50', '2000년')

# house.append(house1)
# house.append(house2)
# house.append(house3)

# print('총 {0}대의 매물이 있습니다.'.format(len(house)))
# for i in house:
#     i.show_detail()

# ※예외처리
# try: 
#     print('나누기 전용 계산기입니다.')
#     nums = []
#     nums.append(int(input('첫번째 숫자를 입력하세여 : ')))
#     nums.append(int(input('두번째 숫자를 입력하세여 : ')))
#     # nums.append(int(nums[0]/nums[1]))
#     print('{0} / {1} = {2}'.format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print('에러! 잘못된 값을 입력하였습니다.')
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print(err)

# class BigNum(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print('한자리 숫자 나누기 전용 계산기입니다.')
#     num1 = int(input('첫번째 숫자를 입력하세여 : '))
#     num2 = int(input('두번째 숫자를 입력하세여 : '))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNum('입력값 : {0}, {1}'.format(num1, num2))
#     print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))
# except BigNum as err:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')
#     print(err)
# finally:
#     print('계산기를 이용해 주셔서 감사합니다.')

# 문제 9
# class SoldOutError(Exception):
    
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print('[남은 치킨 : {0}]'.format(chicken))
#         order = int(input('치킨 몇 마리 주문하시겠습니까?'))
#         if order > chicken:
#             print('재료가 부족합니다.')
#         elif order < 1: 
#             raise ValueError
#         else:
#             print('[대기 번호 {0}] {1} 마리 주문이 완료되었습니다.'.format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#            raise SoldOutError('재료가 소진되어 더 이상 주문을 받지 않습니다.')
#     except ValueError:
#         print('잘못된 값을 입력하였습니다.')
#     except SoldOutError as err:
#         print(err)
#         break

# ※모듈
# import theather_module
# theather_module.price(3)
# theather_module.price_morning(4)
# theather_module.price_soldier(5)

# import theather_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theather_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theather_module import price, price_morning
# price(3)
# price_morning(4)

# from theather_module import price_soldier as price
# price(5)

# ※패키지
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_t = thailand.ThailandPackage()
# trip_to.detail()
# trip_t.detail()

# import inspect
# import random
# print(inspect.getfile(vietnam))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# ※내장함수 / 구글에 [list of python builtins] 라고 검색해보기
# print(dir())
# import random
# print(dir(random))
# import pickle
# print(dir())
# g = 5
# print(dir(g))

# ※외장함수 / 구글에 [list of python modules] 라고 검색해보기
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob('*.py'))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())

# folder = 'sample_dir'

# if os.path.exists(folder):
#     print('이미 존재하는 폴더입니다.')
#     os.rmdir(folder)
#     print(folder,'폴더를 삭제하였습니다.')
# else:
#     os.makedirs(folder)
#     print(folder, '폴더를 생성하였습니다.')

# print(os.listdir())

# import time
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

# import datetime
# print('오늘 날짜는', datetime.date.today())

# timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()
# td = datetime.timedelta(days = 100)
# print(today + td)

# ※문제 10
# import byme
# byme.sign()



# 기본편 문제 1번(레벨 2)
# import pickle

# names = ['유튜브1', '유튜브2', '유튜브3', '유튜브4']

# for i in names:
#     with open('{0}.txt'.format(i), 'w', encoding= 'utf8') as report_file:
#         report_file.write('''
#             안녕하세요! {0}님.
#             임창민입니다.
#             현재 저희 출판사는 ~~
#             {0}님의 유튜브 영상을 보고 연락을 드리게~
#             자세한 내용은 ~
    
#             좋은 하루 보내세여 ^^
#             감사합니다.

#             -창민 드림.
#             '''.format(i))

#  기본편 문제 2번(레벨 4)
# from random import *

# fruit = ['apple', 'banana', 'orange']
# word = choice(fruit)
# letters = ''
# print('answer :', word)

# while True:
#     lim = True
#     print('letters =', letters)
#     print('word =', word)
#     for i in word:
#         if i in letters:
#             print(i, end =' ')
#         else:
#             print('_', end = ' ')
#             lim = False

#     print()
#     print('lim =', lim)

#     if lim:
#         print('Succeed')
#         break
#     letter = input('Input letter > ')


#     if letter not in letters:
#         letters += letter

#     if letter in word:
#         print('Correct')
#     else:
#         print('Wrong')
# lst = ['임', '창', '민']
# for lst_inx, lst_val in enumerate(lst):
#     print(lst_inx, lst_val)

a = int(input())
for i in range(a):
    b,c = input().split()
    b = int(b)
    for j in c:
        print(j*b,end="")
    print()