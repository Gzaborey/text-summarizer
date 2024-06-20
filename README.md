# text-summarizer

A simple servise to summarize text messages.  

## Project description

A brief description of your project and what it does.

## Setup (for Windows)

1. Create a virtual environment:

    ```bash
    python -m venv env
    ```
2. Activate a virtual environment:    



    ```bash
    env\Scripts\activate
    ```

3. Install dependencies via 'pip' (choose one):  
a. Install dependencies only for pure LangChain implementation of service (not recommended).  

    ```bash
    pip install fastapi uvicorn langchain_community huggingface_hub
    ```  
   b. Install dependencies only for LangChain + Hugging Face implementation of service.

   ```bash
   pip install fastapi uvicorn langchain_huggingface transformers numpy<2
    ```  
   c. Install dependencies for both implementation of service.

   ```bash
   pip install -r requirements.txt
   ```  


## Usage
1. Run the application.

   ```bash
   python main.py
   ```
2. Test the endpoint:  
   - Send a POST request to http://127.0.0.1:8000/summarize with a JSON body containing the text to be summarized.

   * For testing you can run 'endpoint_test.py'. It already contains a request ready to be sent.  

        ```bash
        python endpoint_test.py
        ``` 
