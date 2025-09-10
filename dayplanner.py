from flask import Flask,render_template,request,redirect,url_for,jsonify
from database import init_db


app=Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")
@app.route('/home',methods=['POST','GET'])
def log():
    if request.method=='POST':
          data=request.get_json()
          if not data:
              return jsonify({"error":"no data"}),400
          username=data.get('username')
          password=data.get('password')
          print("hello")
          if len(username)<8 or len(password)<8:
              return jsonify({"error":"Both credentials should be of 8 or morre characters"}),400
          a=init_db()
          cursor=a.cursor()
          cursor.execute("""SELECT * FROM userdetails where username=?""",(username,))
          r=cursor.fetchone()
          a.close()
          if not r:
              a=init_db()
              cursor=a.cursor()
              cursor.execute("INSERT INTO userdetails (username,password) VALUES(?,?)",(username,password))
              a.commit()
              a.close()
              return jsonify({"message":"welcome"}),201
          if r:
              if password!=r[1]:
                  return jsonify({"error":"wrong credentials"}),401
          return jsonify({"message":"WELCOME"}),200
    else:
        return render_template("homepage.html")
     
    
@app.route('/task',methods=['POST','GET'])
def task():
    if request.method=='post':
      todaytask=request.form["today"]
      return redirect(url_for('home'))
    render_template("home.html")
    
@app.route('/remain',methods=['GET','POST'])
def remainder():
    if request.method=='post':
        event=request.form.get('event')
        date=request.form.get('addate')
        return redirect(url_for("home"))
    return render_template("home.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/usersignin',methods=['GET','POST'])
def usersignin():
    if request.method=='post':
        newuser=request.form.get('newuser')
        newpass=request.form.get('newp')
        repass=request.form.get('repass')
        return render_template("home.html")
    return render_template("home.html")



if __name__=='__main__':
    app.run(debug=True,port=5000,host="0.0.0.0")