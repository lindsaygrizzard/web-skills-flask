from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return render_template("application-form.html")

@app.route('/application')
def returned_data():
    first = request.args.get("first")
    last = request.args.get("last")
    salary = request.args.get("salary")
    job = "job"



    return render_template("form-return.html",
        first=first, last=last, salary=salary, job=job)




if __name__ == "__main__":
    app.run(debug=True)