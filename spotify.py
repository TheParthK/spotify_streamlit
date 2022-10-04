import streamlit as st


from streamlit.components.v1 import iframe
# st.image('Spotify-logo.png')
st.title('Liked Songs')
st.write('Here are some of the songs I like')
col1, col2 = st.columns((3, 2))
col3, col4 = st.columns((2, 3))
col5, col6 = st.columns((3, 2))
col7, col8 = st.columns((2, 3))

with col1:
    iframe("https://open.spotify.com/embed/track/0NLkVxf0PyxsXBG3EuZcJf?utm_source=generator", height=250)
with col2:
    iframe("https://open.spotify.com/embed/track/6BvRzfqi3sMAoQYnRpMVL0?utm_source=generator", height=250)
with col3:
    iframe("https://open.spotify.com/embed/track/4eaynYNbGdL9F90LGLcUsU?utm_source=generator", height=250)
with col4:
    iframe("https://open.spotify.com/embed/track/3OUyyDN7EZrL7i0Sbi5SVd?utm_source=generator", height=250)
with col5:
    iframe("https://www.youtube.com/embed/UIwdCN4dV6w", height=250)
# with col5:
#     iframe("https://open.spotify.com/embed/track/6VCeywT4JeawuZOUkQ1okx?utm_source=generator", height=250)
with col6:
    iframe("https://open.spotify.com/embed/track/6ymoA9aCgqTyoQLIeR7vCX?utm_source=generator", height=250)
with col7:
    iframe("https://open.spotify.com/embed/track/0iU7CgogGTTJdms1raHgZp?utm_source=generator", height=250)
with col8:
    iframe("https://open.spotify.com/embed/track/2cIGfiNI7HuaoWYTWyrOse?utm_source=generator", height=250)

