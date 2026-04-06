from flask import Flask, request, flash, render_template

app=Flask( __name__ )
app.secret_key ='787643'
@app.route('/', methods=["GET", "POST"])
def home():
    a= ['A', 'AB', 'CD', 'EF']
    b= ['1','2','3', '4', '5']
    c=['PYTHON']
    if request.method=="POST":
        user=request.form.get("user")
        pw=request.form.get("password")
        key=request.form.get("list_key")
        if user=='admin'and pw=='1234':
            flash("hello")
        if key== 'a':
            flash (a)
        elif key == 'b':
             flash (b)
        elif key =='c':
            flash (c)
        else:
            flash("Error")
            flash("wrong user or password")
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
