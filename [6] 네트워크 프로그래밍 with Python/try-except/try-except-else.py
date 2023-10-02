import sys
try:
    fp = open('sample.txt')
    sl = fp.readline()
    value = int(sl.strip())
except OSError as err:
    print("OS 오류: ", err)
except ValueError:
    print("정수로 변환할 수 없습니다.")
except:
    print("알 수 없는 오류가 발생하였습니다.")