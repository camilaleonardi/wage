import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

car = pd.read_csv("car.csv")
st.title("Analisis Salario")

tab1, tab2 = st.tabs(["Tab1", "Tab2"])

with tab1:
    st.header("Analisis Univariado")
    fig, ax = plt.subplots(1,4, figsize=(10,4))

    #educ
    ax[0].hist(car["educ"])
    ax[0].set_title("Educacion")

    #sexo
    conteo = car["sexo"].value_counts()
    ax[1].bar(conteo.index, conteo.values)
    ax[1].set_title("Sexo")

    #exper
    ax[2].hist(car["exper"])
    ax[2].set_title("Experiencia")

    #wage
    ax[3].hist(car["wage"])
    ax[3].set_title("Salario")

    fig.tight_layout()

    st.pyplot(fig)


with tab2:
    st.header("Analisis Bivariado")

    fig, ax = plt.subplots(1,3,figsize=(10,4))

    #Educ vs Wage
    ax[0].scatter(car["educ"],car["wage"])
    ax[0].set_title("Salario vs Educ")

    #Salario vs Exper
    ax[1].scatter(car["exper"],car["wage"])
    ax[1].set_title("Salario vs Exper")

    #Salario vs Sexo
    sns.boxplot(data=car, x="sexo", y="wage", ax=ax[2])
    ax[2].set_title("Salario vs Sexo")

    fig.tight_layout()
    
    st.pyplot(fig)

