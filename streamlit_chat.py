from pandas.core.frame import AggFuncType
import streamlit as st
from openai import OpenAI
from streamlit_highcharts import streamlit_highcharts
import pandas as pd

line_chart_options = {
    "chart": {
        "type": "bar"
    },
    "title": {
        "text": "Fruit Consumption"
    },
    "xAxis": {
        "categories": ["Apples", "Bananas", "Oranges"]
    },
    "yAxis": {
        "title": {
            "text": "Number of fruits"
        }
    },
    "series": [{
        "name": "Jane",
        "data": [1, 0, 4]
    }, {
        "name": "John",
        "data": [5, 7, 3]
    }]
}

pie_chart_options = {
  "chart": {
    "type": "pie"
  },
  "title": {
    "text": "Dummy Pie Chart"
  },
  "subtitle": {
    "text": "Sample data"
  },
  "tooltip": {
    "pointFormat": "{series.name}: <b>{point.percentage:.1f}%</b>"
  },
  "accessibility": {
    "point": {
      "valueSuffix": "%"
    }
  },
  "plotOptions": {
    "pie": {
      "allowPointSelect": "true",
      "cursor": "pointer",
      "dataLabels": {
        "enabled": "true",
        "format": "<b>{point.name}</b>: {point.y}"
      }
    }
  },
  "series": [
    {
      "name": "Share",
      "colorByPoint": "true",
      "data": [
        { "name": "Alpha", "y": 35 },
        { "name": "Beta", "y": 25 },
        { "name": "Gamma", "y": 20 },
        { "name": "Delta", "y": 10 },
        { "name": "Other", "y": 10 }
      ]
    }
  ]
}

data_table  = {
    "chart": {
        "type": "table"
    },
    "title": {
        "text": "Simple Grid Data"
    },
    "data": {
        "rows": [
            ["Name", "Age", "City"],
            ["Alice", 25, "New York"],
            ["Bob", 30, "London"],
            ["Charlie", 28, "Toronto"],
            ["Diana", 32, "Sydney"]
        ]
    },
    "table": {
        "showRowSums": False,
        "showColSums": False
    }
}


df = pd.DataFrame({
    "Product": ["Shoes", "Bag", "Watch"],
    "Price": [2000, 1500, 3000],
    "Rating": [4.2, 3.8, 4.5]
})


MODEL = "llama3.1:latest"

st.set_page_config(page_title="Analytics", layout="wide")

st.title("Analytics AI")

chart_data = df.to_dict(orient="records")
st.write(chart_data)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        streamlit_highcharts(data_table)

    # Generate bot response (dummy or API call)
    bot_reply = f"You said: {user_input}"

    # Add bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)