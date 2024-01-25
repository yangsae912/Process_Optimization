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

 
 
# uploaded_file = st.file_uploader("파일 업로드", type='xlsx', key='file')

# try: 
#         file = st.file_uploader("파일 업로드", type='xlsx', key='file')




#         if st.session_state.file != None:
#             with st.container():
#                 tags = None
#                 use_tagset = st.radio(label="tagset을 제공하시겠습니까?", 
#                               options=('아니오', '예'), 
#                               help='tagset에 포함되지 않은 tag를 식별하기 위해 tagset을 입력합니다.', 
#                               key='use_tagset')
#                 if st.session_state.use_tagset =='예':
#                     tags = st.text_area("tagset을 입력하시오. (No Tag와 Obscure 제외, **각 tag 줄바꿈으로 분리** 필수!)", 
#                                 key='tags')
# except Exception as e:
#         st.error(str(e))
    