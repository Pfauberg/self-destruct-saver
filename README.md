# Self-Destruct Saver

A Telegram bot that saves self-destructing photos, videos, voice messages, and video notes to "Saved Messages."

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pfauberg/self-destruct-saver.git
   cd self-destruct-saver
   ```
2. Install dependencies:
   ```bash
   pip install pyrogram tgcrypto configparser
   ```
3. Configure `config.ini`:
   ```ini
   [telegram]
   api_id = YOUR_API_ID
   api_hash = YOUR_API_HASH
   ```

## Usage

Run the bot:
```bash
python main.py
```
