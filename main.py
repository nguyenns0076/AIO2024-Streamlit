"""
demo các lệnh sử dụng streamlit
import random as r 

"""
import streamlit as st


st.header("Hello")

st.audio('./source/audio.mp4')

st.video('./source/video.mp4')

st.logo('./source/dog.jpeg')

st.image(('./source/logo.png'))

st.divider()


def get_fullname():
    return "Nguyen"


agree = st.checkbox("I agree!", on_change=get_fullname)
if agree:
    st.write("Thanks")

status = st.radio('Color:', ["Yellow", "Blue"], captions=["Vang", "Xanh"])
print(status)

status = st.selectbox("A", ["B", "C"])
print(status)

options = st.multiselect("A", ["B", "C", "D"])
print(options)

st.select_slider("A", ["0", "1", "2"])

st.divider()

if st.button("Say Hello"):
    st.write("Hello")
else:
    st.write("Bye")

value = st.text_input('Your Name', value="Thai")
st.write(value)

st.divider()

upload_files = st.file_uploader('Nhap file vao:', accept_multiple_files=True)

for upload_file in upload_files:
    read_f = upload_file.read()
    st.write("File Name:", upload_file.name)

st.divider()

with st.form(' my form'):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("Name:")
    f_age = col2.text_input("Age:")
    submited = st.form_submit_button('Submit')

    if submited:
        st.write(f"Name: {f_name}, Age: {f_age}")

st.divider()

"value = r.randint(1, 10)"
value = (1, 2, 3, 4, 5, 6)
if 'key' not in st.session_state:
    st.session_state['key'] = value
st.write(st.session_state.key)
