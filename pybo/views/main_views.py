from flask import Blueprint, render_template

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')
# url_prefix = '/'


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    # render_template("html 파일 경로", html에 변수=python 변수)
    # db에서 query만들어서 가져온 question_list를 question_list.html안에 있음
    # question_list에 대입
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    #DB에서 question_id 로 question 자료를 가져옴
    question = Question.query.get_or_404(question_id)
    # render_templates: EB데서 가져온 qustion들ㅡㅡ
    return render_template('question/question_detail.html', question=question)