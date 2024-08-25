{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from rich import print as pprint\n",
    "import requests"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "GET  \n",
    "http://127.0.0.1:9090/Http_Water_Tower/Simulate_Initialize  \n",
    "http://127.0.0.1:9090/Http_Water_Tower/Read_All_DBL  \n",
    "http://127.0.0.1:9090/Http_Water_Tower/Read_All_Boolean  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get('http://127.0.0.1:9090/Http_Water_Tower/Simulate_Initialize')\n",
    "# 查看狀態碼\n",
    "pprint('Status Code:', response.status_code)\n",
    "# 查看請求的內容\n",
    "pprint('Response Text:', response.text)\n",
    "# 解析 JSON 響應   \n",
    "pprint('JSON Response:', response.json())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">JSON Response:\n",
       "<span style=\"font-weight: bold\">{</span><span style=\"color: #008000; text-decoration-color: #008000\">'Read DBL Array'</span>: <span style=\"font-weight: bold\">[</span><span style=\"color: #008080; text-decoration-color: #008080; font-weight: bold\">70.5500000000001</span>, <span style=\"color: #008080; text-decoration-color: #008080; font-weight: bold\">8.1</span>, <span style=\"color: #008080; text-decoration-color: #008080; font-weight: bold\">3.2</span>, <span style=\"color: #008080; text-decoration-color: #008080; font-weight: bold\">85.3</span>, <span style=\"color: #008080; text-decoration-color: #008080; font-weight: bold\">25.5</span><span style=\"font-weight: bold\">]}</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "JSON Response:\n",
       "\u001b[1m{\u001b[0m\u001b[32m'Read DBL Array'\u001b[0m: \u001b[1m[\u001b[0m\u001b[1;36m70.5500000000001\u001b[0m, \u001b[1;36m8.1\u001b[0m, \u001b[1;36m3.2\u001b[0m, \u001b[1;36m85.3\u001b[0m, \u001b[1;36m25.5\u001b[0m\u001b[1m]\u001b[0m\u001b[1m}\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "response = requests.get('http://127.0.0.1:9090/Http_Water_Tower/Read_All_DBL')\n",
    "pprint('JSON Response:', response.json())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">JSON Response:\n",
       "<span style=\"font-weight: bold\">{</span><span style=\"color: #008000; text-decoration-color: #008000\">'Read Bool Array'</span>: <span style=\"font-weight: bold\">[</span><span style=\"color: #00ff00; text-decoration-color: #00ff00; font-style: italic\">True</span>, <span style=\"color: #00ff00; text-decoration-color: #00ff00; font-style: italic\">True</span>, <span style=\"color: #ff0000; text-decoration-color: #ff0000; font-style: italic\">False</span>, <span style=\"color: #ff0000; text-decoration-color: #ff0000; font-style: italic\">False</span><span style=\"font-weight: bold\">]}</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "JSON Response:\n",
       "\u001b[1m{\u001b[0m\u001b[32m'Read Bool Array'\u001b[0m: \u001b[1m[\u001b[0m\u001b[3;92mTrue\u001b[0m, \u001b[3;92mTrue\u001b[0m, \u001b[3;91mFalse\u001b[0m, \u001b[3;91mFalse\u001b[0m\u001b[1m]\u001b[0m\u001b[1m}\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "response = requests.get('http://127.0.0.1:9090/Http_Water_Tower/Read_All_Boolean')\n",
    "pprint('JSON Response:', response.json())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "POST  \n",
    "http://127.0.0.1:9090/Http_Water_Tower/Set_InputWaterSwitch?Web_Input_Switch={value}  \n",
    "http://127.0.0.1:9090/Http_Water_Tower/Set_OutputWaterSwitch?Web_Output_Switch={value}  \n",
    "http://127.0.0.1:9090/Http_Water_Tower/Set_UpLevel?W_UplevelSetting={value}  \n",
    "http://127.0.0.1:9090/Http_Water_Tower/Set_LowLevel?W_LowLevelSetting={value}  \n",
    "http://127.0.0.1:9090/Http_Water_Tower/Set_IWSpeed?W_IWSpeed={value}  \n",
    "http://127.0.0.1:9090/Http_Water_Tower/Set_OWSpeed?W_OWSpeed={value}  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "data={\n",
    "    \"device\":\"EQPT_NO\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Web_Input_Switch\n",
    "value = 1\n",
    "response = requests.post(f'http://127.0.0.1:9090/Http_Water_Tower/Set_InputWaterSwitch?Web_Input_Switch={value}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Web_Output_Switch\n",
    "value = 1\n",
    "response = requests.post(f'http://127.0.0.1:9090/Http_Water_Tower/Set_OutputWaterSwitch?Web_Output_Switch={value}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "#W_LowLevelSetting\n",
    "value = 31.0\n",
    "response = requests.post(f'http://127.0.0.1:9090/Http_Water_Tower/Set_LowLevel?W_LowLevelSetting={value}', json=data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "#W_UpLevelSetting\n",
    "value = 77.0\n",
    "response = requests.post(f'http://127.0.0.1:9090/Http_Water_Tower/Set_UpLevel?W_UpLevelSetting={value}', json=data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "# [[重要]]錯誤的輸入會使面板上的元件錯誤\n",
    "# #W_UpLevelSetting\n",
    "# value = 77.8\n",
    "# response = requests.post(f'http://127.0.0.1:9090/Http_Water_Tower/Set_LowLevel?W_UpLevelSetting={value}', json=data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "#W_IWSpeed\n",
    "value = 20\n",
    "response = requests.post(f'http://127.0.0.1:9090/Http_Water_Tower/Set_IWSpeed?W_IWSpeed={value}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "#W_OWSpeed\n",
    "value = 40\n",
    "response = requests.post(f'http://127.0.0.1:9090/Http_Water_Tower/Set_OWSpeed?W_OWSpeed={value}')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
