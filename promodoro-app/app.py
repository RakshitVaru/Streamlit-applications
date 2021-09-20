import streamlit as st
import time 


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

icon("search")
selected = st.text_input("", "Search...")
button_clicked = st.button("OK")

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown('<style>body {color: #2E86C1;background-color: #D6EAF8;}.stButton>button{color: #666;border-radius: 50%;height: 12em;width: 12em;}</style>', unsafe_allow_html=True)

# st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)
# with open("C:/Users/raksh/Documents/Learning/Project1/promodoro-app/style.css") as f:
#     st.markdown(f.read())

#def remote_css(url):
#    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

#def icon(icon_name):
#    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

# local_css("style.css")
#remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

#---------------------------------------------#
st.write("""
Timer Web Application

""")

# Let's do some focus work in data science with this app.

# Developed by: [Data Professor](http://youtube.com/dataprofessor)

button_clicked= st.button("Start")

t1=1500
t2=300

if button_clicked:
    with st.empty():
        while t1:
            mins, secs= divmod(t1, 60)
            timer= '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            t1-=1
            st.success("🔔 25 minutes is over! Time for a break!")

        
    with st.empty():
        while t2:
            # Start the break
            mins2, secs2= divmod(t2, 60)
            timer2= '{:02d}:{:02d}'.format(mins2, secs2)
            st.header(f"⏳ {timer2}")
            time.sleep(1)
            t2-=1
            st.error("⏰ 5 minutes is over!")
