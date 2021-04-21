from werkzeug.utils import redirect
from flask import render_template, session, request, url_for
from mypage import app
from mypage.forms import QuestionForm
from mypage.models import Question, Answer, CategoryEnum
from mypage.paginator import Paginator


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/projects")
def projects_page():
    return render_template("projects.html")


@app.route("/contacts", methods=['GET', 'POST'])
def contacts_page():
    question_form = QuestionForm()
    if question_form.validate_on_submit():
        question = create_question(question_form)
        if question:
            question.save()
        return redirect(url_for('contacts_page'))
    return render_template("contacts.html",
                           vkuser=session.get('vkuser'),
                           question_form=question_form)


def create_question(question_form):
    vkuser = session.get('vkuser')
    question = None
    if vkuser:
        question = Question(vkuser.get('id'),
                            question_form.category.data,
                            question_form.question.data,
                            question_form.detailed_description.data)
    return question


@app.route("/questions")
def questions_page():
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category', None, type=int)
    answer_query = Answer.query
    if category in range(4):
        category = CategoryEnum(category)
        answer_query = Answer.query.filter(Answer.question.has(Question.category == category))
    else:
        category = None
    answers = Paginator(answer_query, items_per_page=4, page=page, radius=3)
    return render_template("questions.html",
                           answers=answers,
                           category=category,
                           categories=CategoryEnum)
