### Llama Vision Debugger

This is a Streamlit-based web application designed to interact with the **Llama Vision model**, a multimodal AI model capable of processing both text and images. The application allows users to upload or paste an image, ask questions or provide prompts related to the image, and receive responses from the Llama Vision model.

#### Key Features:
- **Image Input**: Upload an image file (JPG, JPEG, PNG) or paste an image directly from your clipboard.
- **Image Display**: View the uploaded or pasted image in the application.
- **Chat Interface**: Enter text prompts to ask questions or provide instructions about the image.
- **Multimodal AI**: Send the image and prompt to the Llama Vision model (`llama3.2-vision`) for processing and receive detailed responses.
- **Error Handling**: Includes error messages for invalid inputs or processing failures.

#### How It Works:
1. Provide an image by uploading a file or pasting from the clipboard.
2. Enter a text prompt related to the image.
3. The application processes the image and sends it along with the prompt to the Llama Vision model.
4. The model's response is displayed in the application.

#### Example Use Cases:
- Describe the contents of an image.
- Identify objects or features in an image.
- Answer questions about the image (e.g., "What is the color of the car?" or "How many people are in the picture?").
- Debug and test the capabilities of the Llama Vision model.

#### Technical Details:
- Built with **Streamlit** for the web interface.
- Uses **Pillow (PIL)** for image handling and **base64** for encoding image data.
- Integrates with the **Ollama** library to interact with the Llama Vision model.
- Supports image pasting via the `streamlit_paste_button` component.

#### Requirements:
- Python 3.x
- Libraries: `streamlit`, `Pillow`, `ollama`, `streamlit_paste_button`

#### How to Run:
1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install streamlit Pillow ollama streamlit_paste_button
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
4. Open the provided URL in your browser to use the application.

#### Notes:
- Ensure the Llama Vision model (`llama3.2-vision`) is available via the Ollama library.
- An image must be provided before sending a prompt.

---

This tool is ideal for exploring the capabilities of multimodal AI models and debugging their performance with image and text inputs.