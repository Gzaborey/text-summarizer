# text-summarizer

A simple servise to summarize text messages.  

## Project description

This project has two implementations of a servise. One uses the functionality of only LangChain libraries, other one uses functionality from LangChain and 'transformers' library.

**Why was it needed to create two different implementations of a single service?**  

the initial idea was to create an app using pure LangChain implementation.

However, there are several problems with this solution:  
1. **HuggignFaceEndpoint library from LangChain has a critical bug in it.** To avoid it, an out-of-date LangChain module huggingface-hub should be used, but it will be deprecated with the release of LangChain 3.0.0. and is not recommended by the developers.  
2. **More configuration actions.** To use a huggingface-hub implementation, a Hugging Face API token should be provided. Therefore, the end user should do more actions to configure the service. Create an account, copy and paste the token, etc.

The implementation with the usage of 'transformers' library fixes these issues:  
1. **Official documentation suggests the usage of HuggingFacePipeline in conjunction with 'transformers' library.** 
2. **Better results due to the usage of a pre-trained tokenizer for a Hugging Face model.**
3. **No authentication needed, the model is loaded on a server and used locally.**

## Setup (for Windows)

1. Create a virtual environment:

    ```bash
    python -m venv myenv
    ```
2. Activate a virtual environment:    



    ```bash
    myenv\Scripts\activate
    ```

3. Install dependencies via 'pip' (choose one):  
a. Install dependencies only for pure LangChain implementation of service (not recommended).  

    ```bash
    pip install fastapi uvicorn langchain-community huggingface-hub dotenv
    ```  
   Also, you need to copy and paste your Hugging Face API token in '.env' file. You can claim the token here: https://huggingface.co/settings/tokens.

   b. Install dependencies only for LangChain + Hugging Face implementation of service.

   ```bash
   pip install fastapi uvicorn langchain-huggingface transformers numpy<2
    ```  
   Also, you need to make changes in the import part of the 'main.py' file.  
   - **comment** the 'from summarizer_downgraded import TextSummarizer' line.
   - **uncomment** the 'from summarizer import TextSummarizer' line.
 
   c. Install dependencies for both implementations of service.

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
