import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define a function to make predictions


def predict_default(features):
    # Convert the input features into a dataframe
    input_df = pd.DataFrame([features])

    # Use the loaded model to make predictions
    prediction = model.predict(input_df)

    # Return the prediction
    return prediction[0]

# Define the Streamlit app


# Define the Streamlit app
def main():
    # Set the page title
    st.set_page_config(page_title='Credit Card Default Prediction')

    # Define the input features
    st.title('Credit Card Default Prediction')
    st.write('Enter the following information to make a prediction:')

    limit_bal = st.slider('Credit Limit', 0, 100000, 5000)

    education_dict = {'graduate school': 1, 'university': 2,
                      'high school': 3, 'others': 4, 'unknown': 0}
    education = st.selectbox('Education', list(education_dict.keys()))

    marriage_dict = {'married': 1, 'single': 2, 'others': 3}
    marriage = st.selectbox('Marital Status', list(marriage_dict.keys()))

    age = st.slider('Age', 18, 100, 30)
    pay_0 = st.slider('Payment Status - September', -2, 8, 0)
    pay_2 = st.slider('Payment Status - August', -2, 8, 0)
    pay_3 = st.slider('Payment Status - July', -2, 8, 0)
    bill_amt1 = st.slider('Bill Amount - September', 0, 100000, 5000)
    bill_amt2 = st.slider('Bill Amount - August', 0, 100000, 5000)
    bill_amt3 = st.slider('Bill Amount - July', 0, 100000, 5000)
    pay_amt1 = st.slider('Amount Paid - September', 0, 100000, 5000)
    pay_amt2 = st.slider('Amount Paid - August', 0, 100000, 5000)

    # Map education and marriage values for prediction
    education_val = education_dict[education]
    marriage_val = marriage_dict[marriage]

    # Collect the input features into a dictionary
    features = {'LIMIT_BAL': limit_bal,
                'EDUCATION': education_val,
                'MARRIAGE': marriage_val,
                'AGE': age,
                'PAY_0': pay_0,
                'PAY_2': pay_2,
                'PAY_3': pay_3,
                'BILL_AMT1': bill_amt1,
                'BILL_AMT2': bill_amt2,
                'BILL_AMT3': bill_amt3,
                'PAY_AMT1': pay_amt1,
                'PAY_AMT2': pay_amt2,
                }

    # Display a button to make the prediction
    if st.button('Predict'):
        prediction = predict_default(features)
        st.write('The predicted default status is:', prediction)



# Run the app
if __name__ == '__main__':
    main()
