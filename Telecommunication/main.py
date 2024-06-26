import pandas as pd
import streamlit as st
import matplotlib as plt
import matplotlib.image as mp
import joblib
from sklearn.preprocessing import LabelEncoder




def main():
	from PIL import Image
	image = Image.open('icone.png')
	image2 = Image.open('image2.png')
	st.image(image,use_column_width=False)
	add_selectbox = st.sidebar.selectbox(
	"How would you like to predict?",
	("Online", "Batch"))
	st.sidebar.info('This app is created to predict Customer Churn')
	st.sidebar.image(image2)
	st.title("Predicting Customer Churn")
	if add_selectbox == 'Online':
		account_length=st.number_input('Number of months the customer has been with the current telco provider :' , min_value=0, max_value=240, value=0)
		international_plan=st.selectbox('The customer has international plan :' , ['','1', '0'])
		voice_mail_plan=st.selectbox('The customer has voice mail plan :' , ['','1', '0'])
		number_vmail_messages=st.slider('Number of voice-mail messages. :' , min_value=0, max_value=60, value=0)
		total_day_minutes=st.slider('Total minutes of day calls :' , min_value=0, max_value=360, value=100)
		total_day_calls=st.slider('Total day calls :' , min_value=0, max_value=200, value=50)
		total_eve_minutes=st.slider('Total minutes of evening calls :' , min_value=0, max_value=400, value=200)
		total_eve_calls=st.slider('Total number of evening calls :' , min_value=0, max_value=200, value=100)
		total_night_minutes=st.slider('Total minutes of night calls :' , min_value=0, max_value=400, value=200)
		total_night_calls=st.slider('Total number of night calls :' , min_value=0, max_value=200, value=100)
		total_intl_minutes=st.slider('Total minutes of international calls :' , min_value=0, max_value=60, value=0)
		total_intl_calls=st.slider('Total number of international calls :' , min_value=0, max_value=20, value=0)
		number_customer_service_calls=st.slider('Number of calls to customer service :' , min_value=0, max_value=10, value=0)
		output=""
		input_dict={'account_length':account_length,'international_plan':international_plan,'voice_mail_plan':voice_mail_plan\
		,'number_vmail_messages':number_vmail_messages,'total_day_minutes':total_day_minutes,'total_day_calls':total_day_calls\
		,'total_eve_minutes':total_eve_minutes,'total_eve_calls':total_eve_calls,'total_night_minutes':total_night_minutes\
		,'total_night_calls':total_night_calls,'total_intl_minutes':total_intl_minutes,'total_intl_calls':total_intl_calls\
		,'number_customer_service_calls':number_customer_service_calls}
		input_df = pd.DataFrame([input_dict])
		model = joblib.load(open("finalised_model.pkl","rb"))
		if st.button("Predict"):
			output = model.predict(input_df)
			output = str(output)
		st.success('Churn : {}'.format(output))
	if add_selectbox == 'Batch':
		file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
		if file_upload is not None:
			data = pd.read_csv(file_upload)
			model2 = joblib.load(open("finalised_model.pkl","rb"))
			predictions = model2.predict(data)
			st.write(predictions)
if __name__ == '__main__':
	main()
	