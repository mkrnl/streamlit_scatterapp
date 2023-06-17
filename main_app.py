import streamlit as st
import pandas as pd
import seaborn as sns
import chardet


st.title("散布図行列作成ツール")
st.caption("csv、xlsxデータから散布図行列を出力します")
uploaded_file = st.file_uploader("エクセルファイルをアップロード",type = ["csv","xlsx"])
submit = st.button("表示", key="scatter")

tab1,tab2 = st.tabs(["散布図行列","表"])

def detect_encoding(file):
    rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result["encoding"]
    return encoding

def main():
    
    if uploaded_file is not None :
       
        try:
            encoding = detect_encoding(uploaded_file)
            file_extension = uploaded_file.name.split(".")[-1]
            
            if file_extension =="csv":
                df = pd.read_csv(uploaded_file,encoding = encoding)
            
            else:
                df = pd.read_excel(uploaded_file)

            if submit :
            
                with tab1:
                    # 散布図行列をプロット
                    sns.set(style='ticks',font='IPAexGothic')
                    scatter_plot = sns.pairplot(df, diag_kind='kde')
                    st.pyplot(scatter_plot.fig)

                with tab2:
                    st.dataframe(df)
                
        except Exception as e:
            st.error("ファイルの読み込み中にエラーが発生しました: {}".format(str(e)))
            
    
if __name__ == "__main__":
    main()