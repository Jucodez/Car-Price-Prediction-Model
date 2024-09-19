import pickle 
import streamlit as st

model = pickle.load(open("C:/Users/adenu/Downloads/Python_notebooks-2/Python_notebooks/ML Projects/Car price prediction project/Car price prediction model/car_price_predictor.pkl",'rb'))

def main():
    st.title('Car Pricing Predictor')

    #input variables
    Year = st.text_input('Year of Manufacture')
    Km_driven = st.text_input('Kilometers Driven')
    engine = st.text_input('Engine Capacity (cc)')
    max_power = st.text_input('Maximum Power (bhp)')
    mileage_kmpl = st.text_input('Fuel Efficiency (kmpl)')

    if st.button('Predict'):
        makeprediction = model.predict([[Year,Km_driven,engine,max_power,mileage_kmpl]])
        output = round(makeprediction[0]*19.61,-3)
        formatted_output = "{:,.0f}".format(output)
        st.success('You Can Sell Your Car for {} Naira'. format (formatted_output))

if __name__ == '__main__':
    main()