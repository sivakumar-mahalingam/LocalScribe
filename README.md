# LocalScribe

# Setup Instructions for Offline Speech-to-Text Web App

Follow these steps carefully to run the application on your local machine.

### Step 1: Install Python

If you don't have Python installed, download and install it from the official website:
<https://www.python.org/downloads/>

Make sure to check the box that says **"Add Python to PATH"** during installation.

### Step 2: Create Project Structure

1. Create a new folder for your project (e.g., `speech-to-text-app`).
2. Inside this folder, place the `app.py` file.
3. Create a subfolder named `templates` and place `index.html` inside it.
4. Create a subfolder named `model`. This is where you will put the speech recognition model.

Your folder structure should look like this:

```

speech-to-text-app/
├── app.py
├── model/
│   └── (vosk model files will go here)
└── templates/
└── index.html

````

### Step 3: Install Required Python Libraries

1. Open your terminal or command prompt.
2. Navigate to your project folder (`speech-to-text-app`).
3. Install the necessary libraries by running this command:

  ```bash
   pip install -r requirements.txt
  ```

  * `flask`: The web server.
  * `vosk`: The offline speech recognition engine.
  * `soundfile`: To properly read the audio file sent from the browser.
  * `flask-cors`: To allow the browser to communicate with your local server.

### Step 4: Download the Vosk Speech Model

For the application to work offline, you need to download a Vosk model.

1.  Go to the Vosk models page: [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)
2.  Download a model. For beginners, a small model is recommended. For example, download **`vosk-model-small-en-us-0.15`** (around 45 MB).
3.  Unzip the downloaded file.
4.  You will see a folder with a name like `vosk-model-small-en-us-0.15`. **Copy the contents** of this folder into the `model` directory you created in Step 2.

After this step, your `model` folder should contain several files and subfolders (`am`, `conf`, `graph`, `ivector`).

### Step 5: Run the Application

1.  Make sure you are still in your project directory in the terminal.

2.  Run the Flask application with the following command:

    ```bash
    python app.py
    ```

3.  You should see output in your terminal indicating that the server is running, something like:
    `* Running on http://127.0.0.1:5000/`

4.  Open your web browser (like Chrome or Firefox) and go to the address: **https://www.google.com/search?q=http://127.0.0.1:5000**

5.  The first time you load the page, your browser will ask for permission to use your microphone. **You must click "Allow"** for the application to work.

You are now ready to use the app\! Click the mic, speak, click stop, and see your speech converted to text.
