import os
from flask import Flask, render_template, request
import pandas as pd
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# ============================================================
# LOAD TRAINED MODEL
# ============================================================

model_path = os.path.join(BASE_DIR, "restaurant_revenue_model.pkl")
model = joblib.load(model_path)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():

    return render_template(
        "index.html",
        prediction=None,
        form_data={},
        error=None
    )


# ============================================================
# PREDICTION
# ============================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ====================================================
        # GET FORM VALUES
        # ====================================================

        form_data = {

            "City": request.form.get("City", ""),

            "Cuisine_Type": request.form.get(
                "Cuisine_Type", ""
            ),

            "Seating_Capacity": request.form.get(
                "Seating_Capacity", ""
            ),

            "Average_Meal_Price": request.form.get(
                "Average_Meal_Price", ""
            ),

            "Daily_Customers": request.form.get(
                "Daily_Customers", ""
            ),

            "Staff_Count": request.form.get(
                "Staff_Count", ""
            ),

            "Restaurant_Age": request.form.get(
                "Restaurant_Age", ""
            ),

            "Online_Rating": request.form.get(
                "Online_Rating", ""
            ),

            "Delivery_Service": request.form.get(
                "Delivery_Service", ""
            ),

            "Parking_Available": request.form.get(
                "Parking_Available", ""
            ),

            "Marketing_Budget": request.form.get(
                "Marketing_Budget", ""
            ),

            "Weekend_Customers": request.form.get(
                "Weekend_Customers", ""
            ),

            "Operating_Hours": request.form.get(
                "Operating_Hours", ""
            ),

            "Festival_Discount": request.form.get(
                "Festival_Discount", ""
            ),

            "Customer_Satisfaction": request.form.get(
                "Customer_Satisfaction", ""
            ),

            "Nearby_Competitors": request.form.get(
                "Nearby_Competitors", ""
            ),

            "Monthly_Expenses": request.form.get(
                "Monthly_Expenses", ""
            ),

            "Employee_Experience": request.form.get(
                "Employee_Experience", ""
            )
        }


        # ====================================================
        # CREATE DATAFRAME
        # ====================================================

        input_data = pd.DataFrame({

            "City": [
                form_data["City"]
            ],

            "Cuisine_Type": [
                form_data["Cuisine_Type"]
            ],

            "Seating_Capacity": [
                float(form_data["Seating_Capacity"])
            ],

            "Average_Meal_Price": [
                float(form_data["Average_Meal_Price"])
            ],

            "Daily_Customers": [
                float(form_data["Daily_Customers"])
            ],

            "Staff_Count": [
                float(form_data["Staff_Count"])
            ],

            "Restaurant_Age": [
                float(form_data["Restaurant_Age"])
            ],

            "Online_Rating": [
                float(form_data["Online_Rating"])
            ],

            "Delivery_Service": [
                form_data["Delivery_Service"]
            ],

            "Parking_Available": [
                form_data["Parking_Available"]
            ],

            "Marketing_Budget": [
                float(form_data["Marketing_Budget"])
            ],

            "Weekend_Customers": [
                float(form_data["Weekend_Customers"])
            ],

            "Operating_Hours": [
                float(form_data["Operating_Hours"])
            ],

            "Festival_Discount": [
                form_data["Festival_Discount"]
            ],

            "Customer_Satisfaction": [
                float(form_data["Customer_Satisfaction"])
            ],

            "Nearby_Competitors": [
                float(form_data["Nearby_Competitors"])
            ],

            "Monthly_Expenses": [
                float(form_data["Monthly_Expenses"])
            ],

            "Employee_Experience": [
                float(form_data["Employee_Experience"])
            ]
        })


        # ====================================================
        # MAKE PREDICTION
        # ====================================================

        prediction_value = model.predict(input_data)[0]


        # ====================================================
        # FORMAT PREDICTION
        # ====================================================

        prediction = f"₹{prediction_value:,.2f}"


        # ====================================================
        # SEND PREDICTION + FORM VALUES BACK TO HTML
        # ====================================================

        return render_template(

            "index.html",

            prediction=prediction,

            form_data=form_data,

            error=None

        )


    # ========================================================
    # ERROR HANDLING
    # ========================================================

    except Exception as e:

        print("ERROR:", e)

        return render_template(

            "index.html",

            prediction=None,

            form_data=request.form,

            error=str(e)

        )


# ============================================================
# RUN FLASK APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )