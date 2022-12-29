import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('clean_start.csv')

def load_overall_analysis():
    st.title('overall Analysis')

    # total invested amount
    total = round(df['amount'].sum())
    # max amount infused in a startup
    max_funding = df.groupby('Startup Name')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size
    avg_funding = df.groupby('Startup Name')['amount'].sum().mean()
    # total funded startups
    num_startups = df['Startup Name'].nunique()
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('Total', str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')

    with col3:
        st.metric('Avg', str(round(avg_funding)) + ' Cr')

    with col4:
        st.metric('Funded Startups', num_startups )

    #sector investment Analysis
    col1,col2=st.columns(2)
    with col1:
        sec=df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head(9)
        st.subheader('Investmnet By Sector%')
        fig3,ax3 = plt.subplots()
        ax3.pie(sec,labels=sec.index,autopct='%0.01f%%')
        st.pyplot(fig3)

    with col2:
        ct=df.groupby('city')['amount'].count().sort_values(ascending=False).head(15)
        st.subheader('Investmnet By City%')
        fig4,ax4 = plt.subplots()
        ax4.pie(ct,labels=ct.index,autopct='%0.01f%%')
        st.pyplot(fig4)
    #Top Startup
    top=df.groupby(['Startup Name','year'])['amount'].sum().reset_index().sort_values('amount',ascending=False).drop_duplicates(subset=['year'],keep='first').sort_values('year',ascending=False).set_index('year')
    st.subheader('Top Investmnet Startup OF The Year')
    st.dataframe(top)
    #Type OF Funding
    a = {'Type': ['Private Equity','Seed Funding','Seed / Angel Funding','Debt Funding','Series A','Series B','Series C','Series D', ]}
    ad = pd.DataFrame(a)
    st.subheader('Type OF Funding')
    st.dataframe(ad)

def load_investor_details(investor):
    st.title(investor)
    #load biggest 5 investment of investor
    recent5=df[df.investors.str.contains(investor)].head(6)[
        ['date', 'Startup Name', 'vertical', 'city', 'Round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(recent5)

    col1,col2=st.columns(2)
    with col1:
        #biggest investment
        big5=df[df.investors.str.contains(investor)].groupby('Startup Name')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investment')

        fig, ax = plt.subplots()
        ax.bar(big5.index,big5.values)
        st.pyplot(fig)

    with col2:
        vertical=df[df.investors.str.contains(investor)].groupby('vertical')['amount'].sum()

        st.subheader('Sector invest in')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical,labels=vertical.index,autopct="%0.01f%%")
        st.pyplot(fig1)

    col3,col4=st.columns(2)
    with col3:
        vertical=df[df.investors.str.contains(investor)].groupby('Round')['amount'].sum()

        st.subheader('Stage of investment')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical,labels=vertical.index,autopct="%0.01f%%")
        st.pyplot(fig1)

    with col4:
        vertical=df[df.investors.str.contains(investor)].groupby('city')['amount'].sum()

        st.subheader('City Of investment')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical,labels=vertical.index,autopct="%0.01f%%")
        st.pyplot(fig1)

    year_series=df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader('Year On Year')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index, year_series.values)
    st.pyplot(fig2)

st.sidebar.title('Stratup Funding')

option =  st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp',sorted(df['Startup Name'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')
else:
    selected=st.sidebar.selectbox('Select StartUp',sorted(set(df.investors.str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected)
    st.title('Investor Analysis')

