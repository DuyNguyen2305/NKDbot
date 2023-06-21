import streamlit as st

def login():
    # Hiển thị giao diện đăng nhập
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_button = st.sidebar.button("Login")

    if login_button:
        # Kiểm tra thông tin đăng nhập
        if username == "admin" and password == "123":
            st.success("Đăng nhập thành công!")
            # Hiển thị chatbot nếu đăng nhập thành công
            show_chatbot()
        else:
            st.error("Tên người dùng hoặc mật khẩu không đúng")

def show_chatbot():
    # Hiển thị giao diện chatbot
    st.title("Chatbot")
    # Code của chatbot trong Streamlit ở đây

# if __name__ == "__main__":
#     main()
