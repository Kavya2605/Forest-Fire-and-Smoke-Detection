import streamlit as st
import numpy as np
import cv2
import pickle
from PIL import Image

model = pickle.load(open("fire_model.pkl", "rb"))

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def extract_features(image):

    img = np.array(image)

    img = cv2.resize(img,(224,224))

    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]

    # RGB features
    mean_red = np.mean(red) / 255
    mean_green = np.mean(green) / 255
    mean_blue = np.mean(blue) / 255

    red_blue_ratio = (
        mean_red /
        (mean_blue + 0.001))

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_RGB2GRAY)


    intensity_std = (
        np.std(gray) / 255)

    edges = cv2.Canny(
        gray,50,150)

    edge_density = (
        np.sum(edges > 0)/edges.size)


    # smoke detection
    smoke_pixels = (
        (abs(red-green)<35) & (abs(green-blue)<35) & (red>80))

    smoke_whiteness = (np.sum(smoke_pixels)/smoke_pixels.size)

    haze_index = (
        np.mean(gray)/255
    )

    fire_pixels = (
        (red > 120) & (green > 50) & (red > green) & (green > blue)
    )

    hot_pixel_fraction = (
        np.sum(fire_pixels) / fire_pixels.size
    )

    local_contrast = (
        np.max(gray) -np.min(gray)) / 255

    Features =  np.array([[

        mean_red,
        mean_green,
        mean_blue,
        red_blue_ratio,
        intensity_std,
        edge_density,
        smoke_whiteness,
        haze_index,
        hot_pixel_fraction,
        local_contrast

    ]])

    return Features

# Streamlit 

st.set_page_config(
    page_title="Forest Fire Detection",
    page_icon="🔥",
    layout="centered"
)

st.title(
    "🔥 Forest Fire Smoke Detection"
)
st.write( """
    AI based aerial image monitoring system
    using Computer Vision + Gradient Boosting.
    """
)
uploaded_file = st.file_uploader(
    "Upload Forest / Drone Image",
    type=[
        "jpg",
        "jpeg",
        "png"
    ]
)
if uploaded_file is not None:
    image = Image.open(uploaded_file ).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_column_width=True )
if st.button(
        "Analyze Image"
    ):


        # Extract Features

        features = extract_features(
            image
        )



        st.subheader(
            "Extracted Image Features"
        )


        feature_names = [

            "Mean Red",
            "Mean Green",
            "Mean Blue",
            "Red Blue Ratio",
            "Intensity STD",
            "Edge Density",
            "Smoke Whiteness",
            "Haze Index",
            "Hot Pixel Fraction",
            "Local Contrast"

        ]
        for name,value in zip(
            feature_names,
            features[0]
        ):

            st.write(
                name,
                ":",
                round(float(value),4)
            )
        # Scale features

        features_scaled = scaler.transform(
            features
        )
        # Prediction probability

        probability = model.predict_proba(
            features_scaled
        )[0][1]
        st.subheader(
            f"Fire Probability : {probability:.2f}"
        )
        # High recall threshold

        if probability >= 0.70:


            st.error(
                "🔥 HIGH FIRE ALERT"
            )


        elif probability >= 0.25:


            st.warning(
                "⚠️ Possible Smoke / Early Fire Detected"
            )


        else:


            st.success(
                "🌲 No Fire Detected"
            )

        st.info(
            """Note:
            This system is optimized for high recall.
            False alarms are acceptable,
            but missing real fire is minimized.
            """)