from flask import Flask, session, render_template, request, redirect, url_for
import sys
# import database

app = Flask(__name__)
app.secret_key = "choivy"  # 로그인을 할 때 필요한 secret key 이다.

# 관리자 ID와 PW 임의로 지정
ID = "admin"
PW = "admin"

@app.route("/")
def signin():
    if "userID" in session: # 로그인이 된 상태 userID가 session에 존재하는 상태
        return render_template("signin.html", username = session.get("userID"), login=True) # session 에 있는 username 가져오기
    else: # userID가 session에 존재하지 않은 상태
        return render_template("signin.html", login=False)


@app.route("/login", methods = ["GET", "POST"]) 
def login():
    global ID, PW
    _id_ = request.args.get("loginId") # html에 있는 name
    _password_ = request.args.get("loginPw")

    if ID == _id_ and PW == _password_:
        # print(_id_, _password_)
        session["userID"] = _id_
        return redirect(url_for("index"))
    else:
        return redirect(url_for("signin"))

@app.route("/logout")
def logout():
    session.pop("userID") # pop은 꺼내주는 것
    return redirect(url_for("signin"))


@app.route("/index")  # 원래는 "/"였는데 수정해주었다
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/team")
def team():
    return render_template("team.html")


# @app.route("/applyphoto")
# def photo_apply():
#     location = request.args.get("location")  # name 받아오기
#     cleaness = request.args.get("clean")
#     built_in = request.args.get("built")
#     # print(location, cleaness, built_in)
#     if cleaness == None:
#         cleaness = False
#     else:
#         cleaness = True
#
#     database.save(location, cleaness, built_in)
#     return render_template("apply_photo.html")
#
#
# @app.route("/upload_done", methods=["POST"])  # apply_photo.html 에서 POST로 지정했음
# def upload_done():
#     uploaded_files = request.files["file"]
#     uploaded_files.save("static/img/{}.jpeg".format(database.now_index()))  # static/img/ 안에 파일을 저장한다는 것, 한 줄에 하나씩 입력
#     return redirect(url_for("hello"))  # hello 라는 함수로 리다이렉트


# @app.route("/list")
# def list():
#     house_list = database.load_list()
#     length = len(house_list)
#     return render_template("list.html", house_list=house_list, length=length)  # house_list를 받아와서 html로 보내주게 된다.
#
#
# @app.route("/house_info/<int:index>/")
# def house_info(index):
#     house_info = database.load_house(index)
#     location = house_info["location"]
#     cleaness = house_info["cleaness"]
#     built_in = house_info["built_in"]
#     photo = f"img/{index}.jpeg"

    # return render_template("house_info.html", location=location, cleaness=cleaness, built_in=built_in, photo=photo)
    # 앞에 있는 location, cleaness, built_in, photo은 html에서 썼던 변수 이름
    # 뒤에 있는 location, cleaness, built_in, photo은 def house_info(index)에 있는 변수


if __name__ == "__main__":
    app.run(host='0.0.0.0')
