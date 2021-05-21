def hi():
    print('Hi, Python!')
    print(__name__)

msg = '파이썬, 재미있네요!'

if __name__ == '__main__' :
    hi()
    print(msg)

#임포트 실행이 아닌, 쉘에서 이 파일이 직접실행되면
#__name__이 메인이된다.
