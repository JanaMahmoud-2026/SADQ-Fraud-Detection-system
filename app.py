import streamlit as st
import re

st.set_page_config(page_title="SADQ", page_icon="🛡️")
st.title("🛡️ SADQ نظام كشف الاحتيال")
st.write("حطي اللينك أو الفاتورة وهنقولك نصب ولا آمن")

tab1, tab2 = st.tabs(["🔗 فحص اللينكات", "🧾 فحص الفواتير"])

with tab1:
    link = st.text_input("حطي اللينك هنا:", placeholder="https://...")
    if st.button("افحص اللينك", type="primary", use_container_width=True):
        if not link:
            st.warning("اكتبي لينك الأول")
        else:
            bad = []
            if link.startswith("http://"): bad.append("http مش آمن")
            if re.search(r'\d+\.\d+\.\d+\.\d+', link): bad.append("IP مباشر")
            if any(x in link.lower() for x in ["bit.ly","tinyurl","free","prize","bank","verify"]): bad.append("كلمات نصب")
            
            if bad:
                st.error("🚨 اوعي تفتحيه ده نصب!")
                for b in bad: st.write(f"- {b}")
            else:
                st.success("✅ آمن تقدر تفتحه")
                st.balloons()

with tab2:
    num = st.text_input("رقم الفاتورة")
    amount = st.number_input("المبلغ", min_value=0)
    if st.button("افحص الفاتورة", use_container_width=True):
        if amount > 100000 or len(num) < 4:
            st.error("🚨 فاتورة مشبوهة!")
        else:
            st.success("✅ الفاتورة سليمة")
