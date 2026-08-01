import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Ứng dụng Sức Khỏe Nâng Cao",layout="centered")
st.title("Ứng dụng Theo Dõi Sức Khỏe Nâng Cao")
st.header("Nhập thông tin cá nhân")
name = st.text_input("Họ và tên:")
age = st.number_input("Tuổi:",min_value=0,max_value=120,step=1)
gender = st.radio("Giới tính:",("Nam","Nữ"))
height = st.number_input("Chiều cao (cm):",min_value=50.0,max_value=250.0,step = 0.1)
weight = st.number_input("Cân nặng (kg):",min_value=10.0,max_value=250.0,step = 0.1)
activity_level = st.selectbox("Mức độ hoạt động thể chất:",[
    "Ít vận động",
    "Vận động nhẹ (1-3 buổi/tuần)",
    "Vận động vừa (3-5 buổi/tuần)",
    "Vận động nhiều (6-7 buổi/tuần)",
    "Vận động rất nhiều (2 lần/ngày)"
])

if st.button("Phân tích sức khoẻ"):
    if height>0 and weight>0:
        height_m = height/100
        bmi = weight/(height_m**2)
        if gender == "Nam":
            bmr = 10*weight+6.25*height-5*age+5
        else:
            bmr = 10*weight+6.25*height-5*age-161

        activity_factors = {
            "Ít vận động": 1.2,
            "Vận động nhẹ (1-3 buổi/tuần)": 1.375,
            "Vận động vừa (3-5 buổi/tuần)": 1.55,
            "Vận động nhiều (6-7 buổi/tuần)": 1.725,
            "Vận động rất nhiều (2 lần/ngày)": 1.9
        }

        activity_factor = activity_factors[activity_level]
        tdee = bmr * activity_factor
        water_intake = weight * 35 / 1000

        st.subheader("Kết quả phân tích")
        st.write(f"**Chào {name}!**")
        st.write(f"**Chỉ số BMI:** {bmi:.2f}")
        st.write(f"**BMR(Tỷ lệ trao đổi chất cơ bản):** {bmr:.0f} kcal/ngày")
        st.write(f"**TDEE(Năng lượng tiêu hao mỗi ngày):** {tdee:.0f} kcal/ngày")
        st.write(f"**Lượng nước nên uống mỗi ngày:** {water_intake:.0f} lít")

        st.markdown("### Đánh giá chỉ số BMI:")
        if bmi < 18.5:
            st.warning(f"Bạn đang thiếu cân. Hãy tăng dinh dưỡng. Bạn nên tăng {round(((18.5 - bmi) * (height_m**2)), 2)} kg")
        elif 18.5 <= bmi < 24.9:
            st.success("Bạn có cân nặng bình thường. Duy trì chế độ sống lành mạnh!")
        elif 25 <= bmi < 29.9:
            st.warning(f"Bạn đang thừa cân. Hãy cân bằng lại chế độ ăn và hoạt động. Bạn nên giảm {round(((bmi - 24.9) * (height_m**2)), 2)} kg")
        else:
            st.error(f"Bạn đang béo phì. Cần tham khảo chuyên gia để cải thiện sức khỏe. Bạn nên giảm {round(((bmi - 24.9) * (height_m**2)), 2)} kg")
        st.markdown("### Gợi ý chế độ ăn (Theo mục tiêu):")

        col1, col2 = st.columns(2)

        with col1:
            st.info("**Duy trì cân nặng:**")
            st.write(f"- Ăn khoảng {tdee:.0f} kcal/ngày")
        with col2:
            st.info("**Giảm cân nhẹ:**")
            st.write(f"- Ăn khoảng {tdee-300:.0f} kcal/ngày")
        st.markdown("### Gợi ý thực đơn mẫu:")
        st.markdown("""
        - **Sáng:** Trứng luộc, bánh mì nguyên cám, trái cây
        - **Trưa:** Cơm gạo lứt, ức gà, rau luộc, canh
        - **Tối:** Salad rau xanh, cá hấp, trái cây ít ngọt
        - **Snack:** Hạt khô, sữa chua ít đường
        """)
st.header("Theo dõi sức khỏe về nhịp tim")
sys = st.number_input("Huyết áp tâm thu(mmHg): ", min_value=50, max_value=250, step=1)
dia = st.number_input("Huyết áp tâm trương(mmHg): ", min_value=30, max_value=150, step=1)
heart_rate = st.number_input("Nhịp tim khi nghỉ( bpm): ", min_value=30, max_value=200, step=1)

if st.button("Phân tích tim mạch"):
    st.subheader("Kết quả phân tích tim mạch")

    if sys < 90 or dia < 60:
        st.warning("Huyết áp thấp")
    elif 90 <= sys <= 120 and 60 <= dia <= 80:
        st.success("Huyết áp bình thường")

    elif 120 < sys < 139 and 80 < dia < 89:
        st.warning("Tiền huyết áp")
    elif 140 <= sys <= 159 or 90 <= dia <= 99:
        st.error("Tăng huyết áp độ 1")