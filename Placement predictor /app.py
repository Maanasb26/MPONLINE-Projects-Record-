from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open("logistic_regression_placement_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load the scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load feature names
with open("feature_names.pkl", "rb") as f:
    feature_names = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get numeric inputs
    cgpa = float(request.form["cgpa"])
    tenth = float(request.form["tenth"])
    twelfth = float(request.form["twelfth"])
    backlogs = float(request.form["backlogs"])
    communication = float(request.form["communication"])
    aptitude = float(request.form["aptitude"])
    projects = float(request.form["projects"])
    certifications = float(request.form["certifications"])
    attendance = float(request.form["attendance"])

    # Internship
    internship = request.form["internship"]
    internship_yes = 1 if internship == "Yes" else 0

    # DSA Level
    dsa = request.form["dsa"]

    if dsa == "Beginner":
        dsa_beginner = 1
        dsa_intermediate = 0
    elif dsa == "Intermediate":
        dsa_beginner = 0
        dsa_intermediate = 1
    else:
        # Advanced
        dsa_beginner = 0
        dsa_intermediate = 0

    # Scale ONLY the 9 numeric features
    numeric_data = [[
        cgpa,
        tenth,
        twelfth,
        backlogs,
        communication,
        aptitude,
        projects,
        certifications,
        attendance
    ]]

    scaled_numeric = scaler.transform(numeric_data)

    # Final input for the model (12 features)
    final_data = [[
        scaled_numeric[0][0],
        scaled_numeric[0][1],
        scaled_numeric[0][2],
        scaled_numeric[0][3],
        scaled_numeric[0][4],
        scaled_numeric[0][5],
        scaled_numeric[0][6],
        scaled_numeric[0][7],
        scaled_numeric[0][8],
        internship_yes,
        dsa_beginner,
        dsa_intermediate
    ]]

    # Predict
    prediction = model.predict(final_data)[0]

    if prediction == 1:
        result = "🎉 Student is Likely to be Placed"
    else:
        result = "❌ Student is Not Likely to be Placed"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)