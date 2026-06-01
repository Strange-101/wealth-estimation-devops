import requests
import streamlit as st

st.set_page_config(
    page_title="Wealth Estimation", layout="centered", background_color="white"
)

st.title("AI Household Wealth Estimation")

st.write("Upload a house image to estimate wealth category.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", width="stretch")

    if st.button("Predict Wealth"):
        files = {"file": uploaded_file.getvalue()}

        response = requests.post(
            "http://backend:8000/predict",
            files={
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type,
                )
            },
        )

        result = response.json()

        prediction = result["prediction"]
        confidence = result["confidence"]

        st.success(f"Prediction: {prediction.upper()}")

        st.info(f"Confidence: {confidence:.2%}")

        # Policy recommendations
        if prediction == "low":
            st.warning(
                "Suggested Policies:\n"
                "- Food subsidy\n"
                "- Healthcare support\n"
                "- Educational assistance"
            )

        elif prediction == "medium":
            st.warning("Suggested Policies:\n- Housing loan support\n- Tax assistance")

        else:
            st.warning(
                "Suggested Policies:\n- Investment planning\n- Property tax category"
            )
