<!DOCTYPE html>
<html>

<body>

  <h1>Keylogger</h1>

  <p>This Keylogger is a Python-based tool designed to log keystrokes from a user's keyboard. It captures both alphanumeric and special keys and stores them in a log file. Additionally, it can email the logs periodically for remote monitoring.</p>

  <h2>Features</h2>
  <ul>
    <li>Logs all keystrokes, including special keys (e.g., Enter, Backspace, Tab)</li>
    <li>Encrypts log files using Fernet encryption for enhanced security</li>
    <li>Sends email notifications with the logs after a set threshold of captured keys</li>
    <li>Runs in the background without console window visibility (stealth mode)</li>
    <li>Supports customizable exit triggers (e.g., pressing the Escape key)</li>
  </ul>

  <h2>Getting Started</h2>

  <p>To get started with the Keylogger, follow these steps:</p>
  <ol>
    <li>Clone the repository:</li>
  </ol>
  <pre><code>git clone https://github.com/your-username/keylogger.git</code></pre>

  <ol start="2">
    <li>Navigate to the project directory:</li>
  </ol>
  <pre><code>cd keylogger</code></pre>

  <ol start="3">
    <li>Create a virtual environment (optional but recommended):</li>
  </ol>
  <pre><code>python -m venv .venv</code></pre>

  <ol start="4">
    <li>Activate the virtual environment:</li>
  </ol>
  <pre><code>.venv\Scripts\activate  # On Windows</code></pre>
  <pre><code>source .venv/bin/activate  # On macOS/Linux</code></pre>

  <ol start="5">
    <li>Install the required dependencies:</li>
  </ol>
  <pre><code>pip install pynput cryptography</code></pre>

  <ol start="6">
    <li>Run the keylogger script:</li>
  </ol>
  <pre><code>python main.py</code></pre>

  <h2>Usage</h2>
  <ol>
    <li>Run the keylogger script using <code>python main.py</code>.</li>
    <li>The script will silently start logging keystrokes in the background.</li>
    <li>It will send an email with the logs after a set number of keys have been captured.</li>
    <li>To stop the keylogger, press the <code>Esc</code> key on your keyboard.</li>
    <li>The logs are encrypted for security, and email notifications are sent when the threshold is reached.</li>
  </ol>

  <h2>Contributing</h2>

  <p>Contributions are welcome! If you want to improve the code or add more features, follow these steps:</p>
  <ol>
    <li>Fork the repository.</li>
    <li>Create a new branch for your feature or fix.</li>
    <li>Make your changes and commit them.</li>
    <li>Push your branch to your forked repository.</li>
    <li>Submit a pull request with a detailed description of your changes.</li>
  </ol>

  <h2>License</h2>

  <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

  <h2>Acknowledgments</h2>
  <ul>
    <li>Special thanks to the developers of the <a href="https://pynput.readthedocs.io/en/latest/">pynput</a> and <a href="https://cryptography.io/en/latest/">cryptography</a> libraries for making keylogging and encryption easier.</li>
  </ul>

</body>

</html>
