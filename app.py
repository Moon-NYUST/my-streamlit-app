import streamlit as st
import psycopg

st.title("📢 公告系統")
st.write("歡迎使用公告系統！")

st.divider()
st.header("📢 最新公告")

try:
    conn = psycopg.connect(st.secrets["DATABASE_URL"])
    cursor = conn.cursor()

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

    cursor.close()
    conn.close()

except Exception as e:
    st.error("目前無法讀取公告資料")
    st.exception(e)
