<p><sub>Created by 8wp</sub></p>

<h2>How it works</h2>

  <p>This tool is a locally hosted Python script that interfaces directly with the Discord gateway to automate message sending. 
It uses your bot (or user) token to authenticate and establish a persistent WebSocket connection, allowing messages 
to be dispatched programmatically at defined intervals. The script handles rate-limiting by default to prevent 
flooding the server, and all configuration — including target channel, message content, and interval — is done 
through the built-in menu interface. Essentially, it provides a lightweight, end-to-end solution for scheduled 
messaging without requiring external hosting or services.</p>

<h2>Demonstration</h2>

W.I.P

<h2>Install dependencies</h2>

Run the following command to install all required packages:

```sh
pip install requests
```

<h2>How to use</h2>

<ol>
  <li>Download the <code>discord-message-scheduler.py</code> file.</li>
  <li>Open the file using Python.</li>
  <li>Click <code>2</code> on the startup menu, and input the following data required:</li>
    <ul>
      <li> <code>Token</code> - You can find your bot token on the <a href="https://discord.com/developers/applications" target="_blank" rel="noopener noreferrer">Discord Developer Portal</a> under the <code>Bot</code> tab of your chosen application. Alternatively, you can use your user token which you can find on the <a href="https://discord.com/channels/@me" target="_blank" rel="noopener noreferrer">Web App</a> through using <code>Ctrl + Shift + I</code> and under the <code>Storage</code> header, opening the dropdown on <code>Local Storage</code> and clicking on <code>https://discord.com</code>. Then filter your search to sort for the <code>token</code> key. If it does not show up, use <code>Ctrl + Shift + M</code> two times, to refresh for the <code>token</code> key. Through clicking on it, a window will be visible that you can copy and paste your token from. You must remove the quotation marks before pasting the token, or else it will not approve. Do not share your user token with anyone, as it allows for gateway access to your account if used maliciously, it is recommended to reset your password if you believe to have accidentally shared it with anyone, as this will reset your user token.</li>
      <li><code>Channel ID</code> - Enable <code>Developer Mode</code> in Discord settings, this can be found under the <code>Advanced</code> tab. Then <code>Right Click</code> the channel you wish to send the messages to, and <code>Copy Channel ID</code>.</li>
      <li><code>Message</code> - This is the message you wish to send in your chosen channel within Discord, e.g <code>Hello World</code>.</li>
       <li><code>Interval in seconds</code> - How often you wish for your message to be sent. By default this is set to <code>500</code>, it is not recommended to go below this interval due to rate limits.</li>
    </ul>
  <li>On the startup menu click <code>1</code> to start the tool.</li>
  <li>When you wish to turn off the tool, click <code>Ctrl + C</code>.</li>
</ol>

<h2>Disclaimer</h2>
  <p>Using your user token violates <a href="https://discord.com/terms/guidelines-march-2023" target="_blank" rel="noopener noreferrer">Discord Community Guidelines</a>, and as such is for educational purposes only.</p>

