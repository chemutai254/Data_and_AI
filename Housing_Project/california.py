import joblib
import streamlit as st

# Define functions
with open("california_knn_pipeline.pkl", "rb") as model:
    regressor = joblib.load(model)
    
def predict_price(input_data):
    global regressor
    
    input_data = [input_data]
    prediction = regressor.predict([input_data])
    return prediction[0]

# Create Web app
def main():
    st.title("California Housing Price Prediction")
    
    # Input features with default values
    MedInc = st.number_input("Median Income", value=3.0, min_value=0.0)
    HouseAge = st.number_input("House Age", value=20, min_value=0, max_value=100)
    AveRooms = st.number_input("Average Rooms", value=1000, min_value=0)
    AveBedrms = st.number_input("Average Bedrooms", value=300, min_value=0)
    Population = st.number_input("Population", value=1000, min_value=0)
    AveOccup = st.number_input("Average Occupancy", value=300, min_value=0)
    Latitude = st.number_input("Latitude", value=36.7783, format="%.4f")
    Longitude = st.number_input("Longitude", value=-119.4179, format="%.4f")
    

    # Predict button
    if st.button("Predict"):
        input_data = [[MedInc, HouseAge, AveRooms, AveBedrms, Population,
                       AveOccup, Latitude, Longitude]]
        prediction = predict_price(input_data)
        st.success(f"Predicted House Price: ${prediction:,.2f}")
    else:
        st.info("Enter the details and click on 'Predict' to see the house price.")
        
if __name__ == "__main__":
    main()
