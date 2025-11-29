# Instagram CLI / Bot

A simple modular Instagram CLI tool using [instagrapi](https://github.com/adw0rd/instagrapi) and [Rich](https://github.com/willmcgugan/rich) for professional output.

## Features

- Login via Instagram session ID
- Fetch user information (username, full name, followers, following, media count)
- List recent posts with likes and comments count
- View comments for a post
- Modular architecture with `core`, `services`, and `utils`
- Rich console output
- Robust exception handling

## Project Structure

```

instagram-bot/
│
├── main.py
├── core/
│   ├── __init__.py
│   ├── logger.py
│   └── exceptions.py
├── services/
│   ├── __init__.py
│   ├── auth_service.py
│   ├── user_service.py
│   └── media_service.py
└── utils/
├── __init__.py
└── env_loader.py

````

## Requirements

- Python 3.11+
- instagrapi
- python-dotenv
- rich

```bash
pip install instagrapi python-dotenv rich
````

## Usage

1. Create a `.env` file:

```env
SESSION_ID=your_instagram_session_id
TARGET_USERNAME=instagram_username
```

2. Run the CLI:

```bash
python main.py
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

