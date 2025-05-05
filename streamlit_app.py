import streamlit as st
import boto3
from sagemaker.predictor import Predictor
from sagemaker.serializers import CSVSerializer
from sagemaker.deserializers import JSONDeserializer

# Replace with your SageMaker endpoint name
ENDPOINT_NAME = "your-endpoint-name"

states = ['California', 'Florida', 'New York']

st.title("📊 Predict Startup Profit Using SageMaker")

rd = st.number_input("R&D Spend", min_value=0.0)
admin = st.number_input("Administration Spend", min_value=0.0)
marketing = st.number_input("Marketing Spend", min_value=0.0)
state = st.selectbox("State", states)

if st.button("Predict Profit"):
    state_encoded = [0, 0, 0]
    state_encoded[states.index(state)] = 1
    features = state_encoded + [rd, admin, marketing]
    csv_input = ",".join(map(str, features))

    # Set up predictor
    predictor = Predictor(
        endpoint_name="linear-learner-2025-05-05-17-55-55-189",
        serializer=CSVSerializer(),
        deserializer=JSONDeserializer()
    )

    try:
      score = result['predictions'][0]['score']
      st.success(f"📈 Predicted Profit: ₹ {round(score, 2)}")
    except Exception as e:
      st.error(f"Prediction format error: {e}")

