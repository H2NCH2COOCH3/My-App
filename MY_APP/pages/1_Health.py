import streamlit as st
from sklearn.linear_model import LinearRegression
# ================= HEALTH TAB =================


st.header("😁 Sức khỏe")

tabC, tabD, tabE, tabF = st.tabs([
    "BMI",
    "Uống nước",
    "Số bước",
    "Dự đoán giờ ngủ"
])

with tabC:

    weight = st.number_input("Cân nặng (kg)", 10.0, 200.0)
    height = st.number_input("Chiều cao (m)", 1.0, 2.5)

    if st.button("Tính BMI"):
        bmi = weight / (height**2)
        st.success(f"BMI của bạn: {bmi:.2f}")

with tabD:

    age = st.number_input("Tuổi", 1, 100)

    if st.button("Khuyến nghị"):

        if age < 18:
            st.info("2 - 2.5 lít/ngày")
    else:
        st.info("2.5 - 3.7 lít/ngày")

with tabE:

    age2 = st.number_input("Tuổi của bạn", 1, 100)

    if st.button("Kiểm tra bước"):

        if age2 < 18:
            st.info("12000 bước/ngày")
        elif age2 < 40:
            st.info("10000 bước/ngày")
        else:
            st.info("8000 bước/ngày")

with tabF:

    x = [[10,1,8],[20,5,6],[25,8,3],[30,6,5]]
    y = [10,8,6,7]

    model = LinearRegression()
    model.fit(x,y)

    age = st.number_input("Tuổi",5,100)
    activity = st.slider("Hoạt động",1,10)
    screen = st.number_input("Giờ màn hình",0,24)
    if st.button("Dự đoán"):

        result = model.predict([[age,activity,screen]])[0]
        st.success(f"Bạn nên ngủ {result:.1f} giờ")
