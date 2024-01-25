import streamlit as st # 프레임 워크


st.set_page_config(page_title="T/F Checker", page_icon="📌")
st.markdown("# T/F Checker")
st.sidebar.header("T/F Checker")
st.write(
    """작업 파일에 대해 T/F 체크를 실행하는 프로그램입니다."""
)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

 
