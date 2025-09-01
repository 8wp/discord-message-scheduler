import json
import requests
import time
import os

CONFIG_FILE = 'config.json'

def load_settings():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        return {
            "token": "",
            "channel_id": "",
            "message": "",
            "interval": 300
        }

def save_settings(settings):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(settings, f, indent=4)

def edit_settings(settings):
    print("\nEdit Settings:")
    settings['token'] = input(f"Token [{settings['token']}]: ") or settings['token']
    
    channel_input = input(f"Channel ID [{settings['channel_id']}]: ")
    if channel_input and channel_input.strip().isdigit():
        settings['channel_id'] = channel_input.strip()

    settings['message'] = input(f"Message [{settings['message']}]: ") or settings['message']

    try:
        interval_input = input(f"Interval in seconds [{settings['interval']}]: ")
        if interval_input:
            settings['interval'] = int(interval_input)
    except ValueError:
        print("Invalid interval input. Keeping previous value.")

    save_settings(settings)
    print("✅ Settings saved.\n")

def send_message(token, channel_id, message):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    json_data = {'content': message}
    response = requests.post(url, headers=headers, json=json_data)

    if response.status_code == 200:
        print(f"✅ Sent to channel {channel_id}: {message}")
    elif response.status_code == 429:
        try:
            retry_after = response.json().get('retry_after', 1)
            print(f"⚠️ Rate limited. Retrying after {retry_after} seconds.")
            time.sleep(retry_after)
        except Exception:
            print("⚠️ Rate limited. Retrying after 1 second (default).")
            time.sleep(1)
    else:
        print(f"❌ Failed to send to {channel_id}: {response.status_code} - {response.text}")

def start_sending(settings):
    print("\nStarting periodic message sender... Press Ctrl+C to stop.\n")
    try:
        while True:
            if not settings['channel_id']:
                print("⚠️ No channel ID configured.")
                break

            send_message(settings['token'], settings['channel_id'], settings['message'])
            time.sleep(settings['interval'])
    except KeyboardInterrupt:
        print("\nStopped by user.\n")

def main_menu():
    settings = load_settings()
    while True:
        print("=== Discord Message Sender ===")
        print("1. Start")
        print("2. Edit Settings")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            start_sending(settings)
        elif choice == '2':
            edit_settings(settings)
            settings = load_settings()  
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == '__main__':
    main_menu()
