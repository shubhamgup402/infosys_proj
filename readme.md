# Infosys Tweet Analysis & Generation

This project analyzes tweets related to products (e.g., iPhone 17 Pro), selects top-performing examples, and uses generative AI (Gemini API) to create new tweets with predicted engagement and explanations.

## Features

- Analyze tweets for sentiment, engagement type, keywords, and more.
- Select top tweets based on engagement metrics.
- Generate new tweets using Google Gemini API, comparing them with top examples.
- Predict and explain the performance of generated tweets.

## Setup

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd infosys_proj
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. **Set up API keys**
   - Set your Gemini API key as an environment variable:
     ```sh
     set GEMINI_API_KEY=your_api_key_here
     ```

## Usage

- **Analyze and generate tweets:**
  ```sh
  python create_tweet.py
  ```

- **Run prompt directly:**
  ```sh
  python run_prompt.py
  ```

## File Structure

- `create_tweet.py` — Main script for tweet analysis and generation.
- `run_prompt.py` — Handles prompt execution and Gemini API interaction.
- `requirements.txt` — Python dependencies.
- `LICENSE` — MIT License.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.