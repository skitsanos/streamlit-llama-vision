import base64
from io import BytesIO
from PIL import Image
import streamlit as st
import ollama
from streamlit_paste_button import paste_image_button as pbutton


def process_image(image_data):
    """Process image data and return base64 encoded string"""
    try:
        if isinstance(image_data, bytes):
            # For uploaded file
            return base64.b64encode(image_data).decode('utf-8')
        elif isinstance(image_data, Image.Image):
            # For pasted image
            buffered = BytesIO()
            image_data.save(buffered, format="PNG")
            return base64.b64encode(buffered.getvalue()).decode('utf-8')
        return None
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
        return None


# Sidebar
with st.sidebar:
    st.title("Llama Vision Debugger")
    st.write("This is a debugger for the Llama Vision model.")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    # Clipboard paste button
    paste_result = pbutton("Paste from Clipboard")

# Main content
current_image = None
image_source = None

if uploaded_file is not None:
    current_image = uploaded_file.getvalue()
    image_source = "upload"
elif paste_result.image_data is not None:
    current_image = paste_result.image_data
    image_source = "clipboard"

if current_image is not None:
    # Display the image
    st.image(current_image, caption=f"Image from {image_source}")
else:
    st.write("Please upload an image file or paste from clipboard to display it here.")

# Chat input for the model
prompt = st.chat_input("Enter a prompt for the model")

if prompt and current_image:
    st.markdown(f"#### {prompt}")

    with st.spinner("Processing your request..."):
        # Process the image to base64
        image_base64 = process_image(current_image)

        if image_base64:
            response = ollama.chat(
                model='llama3.2-vision',
                messages=[{
                    'role': 'user',
                    'content': prompt,
                    'images': [image_base64]
                }]
            )

            st.write(response.message.content)
        else:
            st.error("Error processing image")
elif prompt:
    st.warning("Please provide an image before sending a prompt")
