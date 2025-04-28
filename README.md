 
 # HappyBot
 A fun, safe app for kids to ask questions and get happy answers! Made for a hackathon with Gemini API, FastAPI, and Streamlit.

 ## What HappyBot Does
 Kids type a question (like “What’s a star?”) on a colorful web page. The AI gives a safe, friendly answer (like “A star shines in the sky!”). We check everything to keep it kid-friendly.

 ## Team Jobs
 We’re all new to coding! Read your part below and follow “How to Start”.

 ### 1. Frontend: Web Page (Hifza Younus, Muhammad Sajjad)
 - **File**: `app/ui/streamlit_app.py`
 - **Job**: Make a fun web page for kids to type questions and see answers.
 - **To Do**:
   - Use Streamlit to add a text box and show the AI’s answer.
   - Use bright colors and big text kids will love.
   - Work with Piotrick to connect to his backend (ask for his `/chat` link).
   - Example: Kid types “How do I draw a dog?” → Show “Draw a circle for the head!”.
 - **Help**: Watch Streamlit’s [easy video](https://docs.streamlit.io/get-started).

 ### 2. Backend: App Setup (Piotrick)
 - **Files**: `app/main.py`, `app/config.py`, `app/agent/positive_mentor.py`
 - **Job**: Build the app’s brain to answer questions.
 - **To Do**:
   - **main.py**: Make a FastAPI app with a `/chat` link for questions and answers.
   - **config.py**: Load the Gemini API key from `.env`.
   - **positive_mentor.py**: Use Gemini API for safe, kid-friendly answers.
   - Help Hifza/Muhammad connect their web page to your `/chat` link.
 - **Help**: Read FastAPI’s [simple guide](https://fastapi.tiangolo.com/).

 ### 3. Backend: Safety Checks (Shamas Liaqat)
 - **Files**: `app/filters/input_filter.py`, `app/filters/output_filter.py`
 - **Job**: Keep questions and answers safe for kids.
 - **To Do**:
   - **input_filter.py**: Block bad words (like “stupid”).
   - **output_filter.py**: Make sure AI answers are nice (no scary words).
   - Test: “Bad word” (block), “I like cats” (allow).
 - **Help**: Find a list of bad words online.

 ### 4. Documentation: Guides and Slides (Majad Ali)

 - **Job**: Write instructions and make slides for the hackathon.
 - **To Do**:
   - **setup_guide.md**: Write how to run the app (like “Type `streamlit run app/ui/streamlit_app.py`”).
   - Make  slides: 1) What HappyBot is, 2) How it’s safe, 3) Our team.
 - **Help**: Use Google Slides for slides.


 ## How to Start
 Easy steps for beginners. Ask the team leader if stuck.

 1. **Join GitHub**:
    - Check your email for the repo invite and click “Accept”.
    - Tell the team leader your GitHub name.

 2. **Get the Code**:
    - Install Git ([git-scm.com](https://git-scm.com/)). Check: `git --version`.
    - Copy the project:
      ```bash
      git clone https://github.com/your-username/HappyBot.git
      cd HappyBot
      ```

 3. **Set Up**:
    - Install Python 3.8+ ([python.org](https://python.org/)).
    - Install tools:
      ```bash
      pip install fastapi uvicorn streamlit google-generativeai python-dotenv
      ```
    - Make `.env`:
      ```bash
      copy .env.example .env
      ```
    - Add the Gemini API key (team leader will send it).

 4. **Do Your Job**:
    - Make a branch:
      ```bash
      git checkout -b your-name
      ```
      Examples: `hifza-frontend`, `piotrick-backend`, `shamas-filters`, `majad-docs`.
    - Edit your files (e.g., Majad edits `docs/setup_guide.md`).
    - Save:
      ```bash
      git add .
      git commit -m "What you did"
      git push origin your-name
      ```
      Example: `git commit -m "Added web page"`

 5. **Share Your Work**:
    - On GitHub, click “Pull requests” > “New pull request”.
    - Pick your branch (like `hifza-frontend`) → `main`.
    - Write what you did (like “Made safety filter”).
    - Ask the team leader to check.
    - Merge when OK.

 6. **Test It**:
    - Run web page: `streamlit run app/ui/streamlit_app.py`
    - Run backend: `uvicorn app.main:app --reload`
    - Test a question (like “What’s a star?”).

 ## Stay Safe
 - **Don’t share `.env`**: It has the API key. `.gitignore` keeps it safe.
 - **Edit your files only**: Like, Shamas only changes `input_filter.py`.
 - **Ask for help**: Tell the team leader if something’s wrong.

 ## Hackathon Goal
 - **Show**: Kid types “What’s a cat?” → “A cat is a furry friend!”.
 - **Safety**: Block bad words (Shamas’s job).
 - **Slides**: Majad makes  slides for judges.
 - **Plan**: Finish web page, backend, safety by the last day. 

 Let’s make HappyBot fun for kids! Ask the team leader for help.

