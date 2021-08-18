import streamlit as st
import pandas as pd
import os
import errno
import openpyxl
import base64
import io
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')


st.title('EXCEL編集ツール：列抽出')
try:
    file = st.file_uploader("ファイル（.xlsx）をアップロードしてください", type='xlsx')
    df = pd.read_excel(file, engine='openpyxl')
    col_list = df.columns.unique()
    choose_columns = st.multiselect("抽出する行を選んでください",col_list)
    df2 = df[choose_columns]
    st.write(df2)
    towrite = io.BytesIO()
    download_file = df2.to_excel(towrite, encoding='utf-8', index=False, header = True)
    towrite.seek(0)
    b64 = base64.b64encode(towrite.read()).decode()
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="editted_file.xlsx">ダウンロードはこちら</a>'
    st.markdown("▶ "+linko, unsafe_allow_html=True)
except (ValueError, NameError):
    pass #ファイルアップロードしないとエラーが発生し続けるため
except FileNotFoundError:
    st.error("ファイルが見つかりません")

st.sidebar.markdown("""
## 使い方
1. .xlsxファイルをアップロード（データは保存されません）
2. 抽出したい行を選択
3. 「ダウンロードはこちら」をクリック
""")
