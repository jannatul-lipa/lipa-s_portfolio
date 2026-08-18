# Jannatul Ferdousi Lipa - Portfolio Website

A data-driven portfolio website designed for **Jannatul Ferdousi Lipa** (Aspiring Data Analyst & Software Engineer). 

Built with a Python-powered static generation engine (`data.py` -> `build.py` -> `index.html`) for seamless editing and zero-hassle Netlify deployment.

---

## 🛠️ How to Manage & Update Your Portfolio

### 1. Update Portfolio Content
Edit the file [`data.py`](data.py). All your information (Bio, Skills, Projects, Education, Achievements, Contact links) is stored in standard Python dictionary format.

### 2. Generate / Build Website
To re-generate the website HTML whenever you edit `data.py`, run:
```bash
python build.py
```

### 3. Local Preview
To preview your website locally in your web browser:
```bash
python server.py
```
This will start a local server at `http://localhost:8000` and automatically open it in your web browser.

---

## 🚀 How to Host on Netlify

### Option A: Drag and Drop (Fastest & Easiest)
1. Run `python build.py` on your computer.
2. Go to [Netlify Drop](https://app.netlify.com/drop).
3. Drag and drop this entire project folder (`jannat_portfolio`) into Netlify.
4. Your website will be live instantly!

### Option B: Host via GitHub (Automated Deployments)
1. Push this folder to a GitHub repository.
2. Log into [Netlify](https://app.netlify.com/) and click **"Add new site" -> "Import an existing project"**.
3. Select your GitHub repository.
4. Netlify will automatically detect `netlify.toml` and run `python build.py` to build and publish your site!
