allow1,allow2,allow3=input("0 0 0 을 입력하세요").split()
authority=[1,2]
player=["penguin_21", "bbiyaki", "MoonEunWol"]
authorityas=int(authority[1])
allow1=int(allow1)
allow2=int(allow2)
allow3=int(allow3)
player_isallowed=[allow1,allow2,allow3]

#penguin_21 함수
def executeas_allow(): #권한 부여
  allow1=int(authority[0])
  print("penguin_21에게 접근 권한이 부여되었습니다.")

def executeas_unallow(): #권한 제거
  allow1=int(authority[1])
  print("penguin_21에게서 접근 권한을 제거했습니다.")

#bbiyaki 함수
def executeas_allow1(): #권한 부여
  allow2=int(authority[0])
  print("bbiyaki에게 접근 권한이 부여되었습니다.")

def executeas_unallow1(): #권한 제거
  allow2=int(authority[1])
  print("bbiyaki에게서 접근 권한을 제거했습니다.")

#MoonEunWol 함수
def executeas_allow2(): #권한 부여
  allow3=int(authority[0])
  print("MoonEunWol에게 접근 권한이 부여되었습니다.")

def executeas_unallow2(): #권한 제거
  allow3=int(authority[1])
  print("MoonEunWol에게서 접근 권한을 제거했습니다.")



execute_as=input("명령을 입력해주세요.")
if execute_as=="allow penguin_21":
  executeas_allow()
elif execute_as=="disallow penguin_21":
  executeas_unallow()
elif execute_as=="allow bbiyaki":
  executeas_allow1()
elif execute_as=="disallow bbiyaki":
  executeas_unallow1()
elif execute_as=="allow MoonEunWol":
  executeas_allow2()
elif execute_as=="disallow MoonEunWol":
  executeas_unallow2()
else:
  print("Input Error.")