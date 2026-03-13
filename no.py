csimport streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="دورة التجارة الإلكترونية المجانية", page_icon="🎓", layout="centered")

# 2. تصميم CSS (العنوان باللون الأحمر + الخلفية اللؤلؤية)
st.markdown("""
    <style>
    /* خلفية لؤلؤية مهدئة ومتدرجة */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* تنسيق العنوان الرئيسي باللون الأحمر */
    .main-title {
        color: #FF0000;
        text-align: center;
        font-family: 'Cairo', sans-serif;
        font-weight: 900;
        font-size: 40px;
        margin-bottom: 10px;
    }
    
    /* تنسيق العنوان الفرعي */
    .sub-title {
        color: #2c3e50;
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 30px;
    }

    /* تنسيق الصندوق الرئيسي */
    .main-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    /* زر "ابدأ مجاناً" البرتقالي الجذاب */
    div.stButton > button:first-child {
        background-color: #ff9800;
        color: white;
        font-size: 24px;
        font-weight: bold;
        border-radius: 12px;
        width: 100%;
        height: 65px;
        border: none;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(255, 152, 0, 0.4);
    }
    
    div.stButton > button:first-child:hover {
        background-color: #e68a00;
        transform: scale(1.01);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. محتوى الصفحة (العنوان الأحمر والكلمات الاحترافية)
st.markdown("<h1 class='main-title'>🔴 دورة مجانية في التجارة الإلكترونية</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>تعلم أسرار الربح من الإنترنت وابدأ مشروعك الخاص تحت إشراف خبراء متخصصين</p>", unsafe_allow_html=True)

# 4. رسالة توضيحية احترافية
st.info("💡 هذه الدورة مصممة لتأخذك من الصفر حتى احتراف بناء الأنظمة التجارية الناجحة.")

# 5. استمارة البيانات التفاعلية
with st.container():
    with st.form("training_form"):
        st.markdown("### 📝 سجل بياناتك للحصول على رابط الدورة")
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("الاسم واللقب")
        with col2:
            gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
            
        col3, col4 = st.columns(2)
        with col3:
            age = st.number_input("العمر", 18, 70, 25)
        with col4:
            phone = st.text_input("رقم الهاتف (لإرسال تفاصيل الدورة)")
            
        email = st.text_input("البريد الإلكتروني")

        st.write("---")
        
        # سؤال الخبرة
        experience = st.radio(
            "ما هو مستواك الحالي في العمل عبر الإنترنت؟",
            [
                "مبتدئ تماماً (أريد البدء من الصفر)",
                "مستوى متوسط (أبحث عن نظام عمل متكامل)",
                "مستوى متقدم (أطمح لتوسيع نطاق أرباحي ضمن فريق)"
            ]
        )

        # خانة النيشات
        niches = st.multiselect(
            "ما هي التخصصات التي ترغب في احترافها؟",
            ["الصحة والجمال", "العناية بالبشرة", "المكملات الغذائية", "التسويق الرقمي", "إدارة الفرق التجارية"]
        )
        
        # الطموح المادي
        st.write("---")
        goal = st.select_slider(
            "ما هو هدفك المالي الشهري الذي تطمح لتحقيقه؟",
            options=["100$", "500$", "1000$", "2000$ فأكثر"]
        )

        # زر الإرسال الضخم
        submitted = st.form_submit_button("احجز مقعدك المجاني الآن 🚀")

    if submitted:
        if name and phone:
            st.success(f"تم تسجيلك بنجاح يا {name}! سيتم مراجعة بياناتك وإرسال تفاصيل الدورة لك قريباً.")
            st.balloons()
        else:
            st.error("يرجى إكمال البيانات الأساسية (الاسم ورقم الهاتف) لضمان قبول طلبك.")

# 6. التذييل (Footer)
st.markdown("<br><p style='text-align: center; font-size: 0.9em; color: #7f8c8d; border-top: 1px solid #ddd; padding-top: 20px;'>نحن نساعدك على بناء مستقبلك الرقمي | جميع الحقوق محفوظة © 2026</p>", unsafe_allow_html=True)        height: 65px;
        border: none;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(255, 152, 0, 0.4);
    }
    
    div.stButton > button:first-child:hover {
        background-color: #e68a00;
        transform: scale(1.01);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. محتوى الصفحة (العنوان الأحمر والكلمات الاحترافية)
st.markdown("<h1 class='main-title'>🔴 دورة مجانية في التجارة الإلكترونية</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>تعلم أسرار الربح من الإنترنت وابدأ مشروعك الخاص تحت إشراف خبراء متخصصين</p>", unsafe_allow_html=True)

# 4. رسالة توضيحية احترافية
st.info("💡 هذه الدورة مصممة لتأخذك من الصفر حتى احتراف بناء الأنظمة التجارية الناجحة.")

# 5. استمارة البيانات التفاعلية
with st.container():
    with st.form("training_form"):
        st.markdown("### 📝 سجل بياناتك للحصول على رابط الدورة")
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("الاسم واللقب")
        with col2:
            gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
            
        col3, col4 = st.columns(2)
        with col3:
            age = st.number_input("العمر", 18, 70, 25)
        with col4:
            phone = st.text_input("رقم الهاتف (لإرسال تفاصيل الدورة)")
            
        email = st.text_input("البريد الإلكتروني")

        st.write("---")
        
        # سؤال الخبرة
        experience = st.radio(
            "ما هو مستواك الحالي في العمل عبر الإنترنت؟",
            [
                "مبتدئ تماماً (أريد البدء من الصفر)",
                "مستوى متوسط (أبحث عن نظام عمل متكامل)",
                "مستوى متقدم (أطمح لتوسيع نطاق أرباحي ضمن فريق)"
            ]
        )

        # خانة النيشات
        niches = st.multiselect(
            "ما هي التخصصات التي ترغب في احترافها؟",
            ["الصحة والجمال", "العناية بالبشرة", "المكملات الغذائية", "التسويق الرقمي", "إدارة الفرق التجارية"]
        )
        
        # الطموح المادي
        st.write("---")
        goal = st.select_slider(
            "ما هو هدفك المالي الشهري الذي تطمح لتحقيقه؟",
            options=["100$", "500$", "1000$", "2000$ فأكثر"]
        )

        # زر الإرسال الضخم
        submitted = st.form_submit_button("احجز مقعدك المجاني الآن 🚀")

    if submitted:
        if name and phone:
            st.success(f"تم تسجيلك بنجاح يا {name}! سيتم مراجعة بياناتك وإرسال تفاصيل الدورة لك قريباً.")
            st.balloons()
        else:
            st.error("يرجى إكمال البيانات الأساسية (الاسم ورقم الهاتف) لضمان قبول طلبك.")

# 6. التذييل (Footer)

st.markdown("<br><p style='text-align: center; font-size: 0.9em; color: #7f8c8d; border-top: 1px solid #ddd; padding-top: 20px;'>نحن نساعدك على بناء مستقبلك الرقمي | جميع الحقوق محفوظة © 2026</p>", unsafe_allow_html=True)
