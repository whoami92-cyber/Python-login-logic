from flask import Flask, request, flash, render_template

attemps=0
app=Flask( __name__ )
app.secret_key ='787643'
@app.route('/', methods=["GET", "POST"])
def home():
    a= ['A', 'AB', 'CD', 'EF']
    b= ['1','2','3', '4', '5']
    c=['PYTHON']
    if request.method=="POST":
        user=request.form.get("username")
        pw=request.form.get("password")
        key=request.form.get("list_key")
        flash("Hello")
    if key==  'a':
        flash (a)
    elif key == 'b':
        flash (b)
    elif key =='c':
        flash (c)
    else:
        flash("Error")
        attemps +=1
        flash ("attemps", attemps)
    if attemps == 3:
        flash("wrong user or password")
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
