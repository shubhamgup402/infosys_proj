# AI-Based Automated Content Marketing Optimizer (NVIDIA Tech Niche)

This project is an **AI-powered solution for automated content marketing optimization**, focused on the technology and AI sector using NVIDIA historical tweets. It analyzes, generates, and compares high-engagement tweets, helping tech businesses and marketing teams create impactful social media content.

## About

- **What:** Automates tweet analysis and generation for tech/AI brands using real NVIDIA tweet data.
- **Why:** Saves time, boosts engagement, and ensures content resonates with technical audiences.
- **How:** Uses Google Gemini API to analyze sentiment, engagement, and keywords, then generates and compares new tweets for maximum impact.

## Industry & Audience

- **Niche:** AI, technology, robotics, cloud computing, high-performance computing.
- **Ideal Users:** Tech companies, AI startups, cloud service providers, robotics firms, marketing teams, social media managers, PR agencies in tech.

## Features

- Analyze NVIDIA tweets for sentiment, engagement type, keywords, and audience.
- Select top-performing tweets based on engagement metrics.
- Generate new tweets using Google Gemini API, leveraging proven engagement strategies.
- Compare and predict performance of generated tweets, with detailed explanations.
- Modern Flask web interface for prompt input and instant results.

## Example Prompts

- `Announce the launch of NVIDIA's new AI-powered graphics card for data centers.`
- `Invite developers to join NVIDIA's upcoming AI conference.`
- `Share a customer success story using NVIDIA GPUs for AI model training.`
- `Promote NVIDIA's commitment to renewable energy in AI infrastructure.`

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

- **Run the Flask web app:**
  ```sh
  python app.py
  ```

- **Run prompt directly:**
  ```sh
  python run_prompt.py
  ```

## File Structure

- `app.py` — Flask web app for interactive tweet generation and comparison.
- `create_tweet.py` — Main script for tweet analysis and generation.
- `run_prompt.py` — Handles prompt execution and Gemini API interaction.
- `sentiment-analysis.py` — Analyzes tweets for sentiment and engagement.
- `get_tweet.py` — Fetches tweets from Twitter API.
- `requirements.txt` — Python dependencies.
- `LICENSE` — MIT License.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

Example Prompts

Product Launch

Create a tweet announcing the launch of NVIDIA's new AI-powered graphics card for data centers.


Event Promotion

Write a tweet inviting developers to join NVIDIA's upcoming AI conference and hands-on workshops.


Industry Collaboration

Generate a tweet about NVIDIA partnering with leading robotics companies to advance AI in automation.


Milestone Achievement

Craft a tweet celebrating NVIDIA reaching 2 million developers in its global AI community.


Tech Innovation

Compose a tweet highlighting the breakthrough performance of NVIDIA's latest supercomputer in climate research.


Customer Success Story

Write a tweet sharing how a startup used NVIDIA GPUs to accelerate their AI model training.


Sustainability

Generate a tweet about NVIDIA's commitment to renewable energy in powering AI infrastructure.


Employee Spotlight

Create a tweet featuring an NVIDIA engineer's innovative work in cloud security for AI.

