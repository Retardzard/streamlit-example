import streamlit as st
import pickle
import pandas as pd
mobile_list= pickle.load(open('movie_dict.pkl','rb'))
mobiles= pd.DataFrame(mobile_list)
st.title("Mobile Recommendation System")



similarity=pickle.load(open('similarity.pkl', 'rb'))
def recommend(mobile):
    mobile_index = mobiles[mobiles['Name']==mobile].index[0]
    distances = similarity[mobile_index]
    mobile_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_mobiles_images= []
    recommended_mobiles = []
    for i in mobile_list:
        recommended_mobiles.append(mobiles.iloc[i[0]].Name)
        recommended_mobiles_images.append(mobiles.iloc[i[0]].Image)
    return recommended_mobiles,recommended_mobiles_images

selected_mobile_name= st.selectbox(
'How would you like to be contacted?',
mobiles['Name'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_mobile_name)
    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
