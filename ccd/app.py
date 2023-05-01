import streamlit as st
import pandas as pd
import pickle

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


def predict_default(features):
    input_df = pd.DataFrame([features])
    prediction = model.predict(input_df)
    return prediction[0]


def main():

    st.set_page_config(page_title='Credit Card Default Prediction')
    st.title('Credit Card Default Prediction')
    st.write('Enter the following information to make a prediction:')

    limit_bal = st.text_input('Credit Limit')

    education_dict = {'graduate school': 1, 'university': 2,
                      'high school': 3, 'others': 4, 'unknown': 5, 'unknown': 6}
    education = st.selectbox('Education', list(education_dict.keys()))

    marriage_dict = {'married': 1, 'single': 2, 'others': 3}
    marriage = st.selectbox('Marital Status', list(marriage_dict.keys()))

    pay_0 = st.slider('Payment Status - September', -2, 8, 0)
    pay_2 = st.slider('Payment Status - August', -2, 8, 0)
    pay_3 = st.slider('Payment Status - July', -2, 8, 0)

    bill_amt1 = st.text_input('Bill Amount - September')
    bill_amt2 = st.text_input('Bill Amount - August')
    bill_amt3 = st.text_input('Bill Amount - July')

    pay_amt1 = st.text_input('Amount Paid - September')
    pay_amt2 = st.text_input('Amount Paid - August')

    education_val = education_dict[education]
    marriage_val = marriage_dict[marriage]

    if st.button('Predict'):
        try:
            limit_bal = int(limit_bal)
            bill_amt1 = int(bill_amt1)
            bill_amt2 = int(bill_amt2)
            bill_amt3 = int(bill_amt3)
            pay_amt1 = int(pay_amt1)
            pay_amt2 = int(pay_amt2)
        except ValueError:
            st.error('Please enter a valid integer value')
            return

        features = {'LIMIT_BAL': limit_bal,
                    'EDUCATION': education_val,
                    'MARRIAGE': marriage_val,
                    'PAY_0': pay_0,
                    'PAY_2': pay_2,
                    'PAY_3': pay_3,
                    'BILL_AMT1': bill_amt1,
                    'BILL_AMT2': bill_amt2,
                    'BILL_AMT3': bill_amt3,
                    'PAY_AMT1': pay_amt1,
                    'PAY_AMT2': pay_amt2,
                    }

        prediction = predict_default(features)
        if prediction == 0:
            st.write('The predicted default status is:',
                     prediction, "(Not Default)")
        else:
            st.write('The predicted default status is:',
                     prediction, "(Default)")


# Run the app
if __name__ == '__main__':
    main()
