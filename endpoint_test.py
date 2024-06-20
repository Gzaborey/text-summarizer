import requests


url = 'http://127.0.0.1:8000/summarize'
text = ''' 
    Programming is the process of designing and building an executable computer software to accomplish
 a specific task. It involves writing code in various programming languages such as Python, JavaScript, or C++. 
 Programming not only requires knowledge of syntax and logic but also problem-solving skills to debug and optimize code. 
 As technology continues to evolve, programming becomes increasingly important in automating tasks, 
 developing applications, and driving innovation across various industries. Whether for web development, 
 data analysis, or artificial intelligence, programming is a fundamental skill that shapes the digital world.
'''

print(requests.post(url, json={'text':  text}).json())
