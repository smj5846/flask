from flask import Flask


# app = Flask(__name__)
# app 객체를 전체 전역으로 사용하는데
# 프로젝트 규모가 커질수록 문제가 발생
# 문제: 순환참조 오류
# 이 문제를 방지하기 위해 애플리케이션 팩토리가 필요하다.

# create_app() 함수 안에 app 이라는 Flask 인스턴스를 생성해서 작동하게 함.
def create_app():
    app = Flask(__name__)

# '/' 주소가 호출이 되면
# 밑에 있는 hello_pybo() 함수가 실행된다.
# @app.route와 같은 애너테이션으로 url을 매핑하는 hello_pybo()와 같은 함수를 라우팅 함수라고 한다.
    @app.route('/') 
    def hello_pybo():
        return 'Hello, Pybo!'

# 만약에 새로운 url 매핑이 필요하다면 라우팅 함수를
# create_app 함수 안에 계속 추가해야 한다. 그러면 create_app() 함수는
# 엄청나게 크고 복잡한 함수가 된다.
# -> 이 문제를 블루프린트(Blueprint)를 사용해서 관리한다.

    return app