# outer fucn 에서 메인으로 불러오는것

# from outer_func import hello, weather as w          # as w as는 함수를 w로 바꾸는것
# hello()
# weather()
# w
# 노란색 ~~~가 나오면 사용 할 수 없는 함수.
import outer_func  # outer_func 에서 전부 불러오는것.

outer_func.hello() # outer_func. 파일명을 붙여야함.
outer_func.weather()


