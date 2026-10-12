
import streamlit as st
import psycopg

# =====================================
# 網頁基本設定
# =====================================

st.title("📢 公告系統")
st.write("歡迎使用公告系統！")


# =====================================
# 側邊欄：基本資料
# =====================================

st.sidebar.header("基本資料")

department = st.sidebar.selectbox(
    "科系",
    ["資訊工程系", "電子工程系", "其他"]
)


# =====================================
# 第一部分：最新公告
# =====================================

st.divider()
st.header("📢 最新公告")

try:
    with psycopg.connect(st.secrets["DATABASE_URL"]) as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT title, content, created_at
                FROM announcements_announcement
                ORDER BY created_at DESC
            """)

            announcements = cursor.fetchall()

    if announcements:
        for title, content, created_at in announcements:
            st.subheader(title)
            st.write(content)
            st.caption(f"發布時間：{created_at}")
    else:
        st.info("目前沒有公告")

except Exception as e:
    st.error("目前無法讀取公告資料")
    st.exception(e)


# =====================================
# 第二部分：課程回饋表單
# =====================================

st.divider()
st.title("📋 課程回饋表單")
st.write("請填寫以下資料，完成後按下送出。")

name = st.text_input("姓名")

satisfaction = st.slider(
    "課程滿意度",
    1, 5, 3
)

feedback = st.text_area("意見回饋")

if st.button("送出"):
    if name.strip() == "":
        st.warning("請先輸入姓名")
    else:
        st.success("感謝您的回饋！")
        st.write("姓名：", name)
        st.write("科系：", department)
        st.write("課程滿意度：", satisfaction)
        st.write("意見回饋：", feedback)
