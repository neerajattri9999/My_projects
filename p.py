# surname=["attri","Hooda"]
# name=["Neeraj","Ajay"]
# scount=0
# for i in name:
#     print(f"first name is: {i} and last name is {surname[scount]}")
#     scount+=1


# answer=input("Throw water ballon (y/n)")
# while answer=="y":
#     print("Splash")
#     answer=input("Do you want to throw again? (y/n)")
# print("OOps")



# import pyautogui
# import time
# # Function to close all open windows
# def close_all_windows():
#     # Number of windows you want to close (adjust as necessary)
#     windows_to_close = 10

#     for _ in range(windows_to_close):
#         # Press Alt + F4 to close the current window
#         pyautogui.hotkey('alt', 'f4')
        
#         # Wait a moment to ensure the window has closed
#         time.sleep(0.5)

# # Execute the function
# close_all_windows()





# import pygetwindow as gw
# import time
# import pyautogui

# # Function to close all open windows
# def close_all_windows():
#     # Get a list of all open windows
#     windows = gw.getAllWindows()

#     # Loop through the windows and close each one
#     for window in windows:
#         try:
#             if window.isMinimized:  # Check if the window is minimized
#                 window.restore()  # Restore the window if minimized
            
#             window.activate()  # Bring the window to the foreground
#             time.sleep(0.1)  # Short delay to ensure it's focused
#             pyautogui.hotkey('alt', 'f4')  # Close the window using Alt + F4
#             time.sleep(0.5)  # Wait a moment before closing the next one
#         except Exception as e:
#             print(f"Error closing window {window.title}: {e}")

# # Execute the function
# close_all_windows()




# import tkinter as tk
# import pygetwindow as gw
# import time
# import pyautogui

# # Function to close all open windows
# def close_all_windows():
#     windows = gw.getAllWindows()  # Get a list of all open windows
#     for window in windows:
#         try:
#             if window.isMinimized:
#                 window.restore()  # Restore the window if minimized
#             window.activate()  # Bring the window to the foreground
#             time.sleep(0.1)  # Short delay to ensure it's focused
#             pyautogui.hotkey('alt', 'f4')  # Close the window using Alt + F4
#             time.sleep(0.5)  # Wait a moment before closing the next one
#         except Exception as e:
#             print(f"Error closing window {window.title}: {e}")

# # Function to handle button click
# def on_button_click():
#     close_all_windows()

# # Create the main application window
# app = tk.Tk()
# app.title("Close Windows App")
# app.geometry("300x150")  # Set the window size

# # Create a button to close windows
# close_button = tk.Button(app, text="Close Open Windows", command=on_button_click, padx=20, pady=10)
# close_button.pack(pady=30)

# # Run the application
# app.mainloop()





import streamlit as st
from langchain_community import llms
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import ctransformers


def getLLamaresponse(input_text, no_words, blog_style):
    llm=ctransformers(model_path='D:\Genai\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max+new+tokens':256,
                              'temperature':0.01})
    
    template="""
    write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
             """
    prompt=PromptTemplate(input_variables=["blog_style", "input_text",'no_words'],
                          template=template)


    response=llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                   page_icon='🚀',
                   layout='centered',
                   initial_sidebar_state='collapsed')
st.header("Genertae BLogs 🚀")
input_text=st.text_input("Enter the blog topic")


col1, col2=st.columns([5,5])
with col1:
    no_words=st.text_input("no. of words")
with col2:
    blog_style=st.selectbox("Writting the blog for :",
                             ('Researchers','Data Scientist', 'common people'), index=0)


submit=st.button("Generate")

if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))