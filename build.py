import html
import json
from data import PORTFOLIO_DATA

def generate_html(data):
    p = data["personal"]
    
    # Skills HTML rendering
    skills_sections = []
    for cat_name, skill_list in data["skills"].items():
        cards = []
        for s in skill_list:
            card = f"""
            <div class="skill-card">
                <div class="skill-icon"><i class="{s['icon']}"></i></div>
                <div class="skill-info">
                    <h4>{html.escape(s['name'])}</h4>
                    <span class="skill-level">{html.escape(s['level'])}</span>
                </div>
            </div>
            """
            cards.append(card)
        
        sec = f"""
        <div class="skills-category">
            <h3 class="category-title"><i class="fa-solid fa-layer-group"></i> {html.escape(cat_name)}</h3>
            <div class="skills-grid">
                {''.join(cards)}
            </div>
        </div>
        """
        skills_sections.append(sec)

    # Projects HTML rendering
    project_cards = []
    for prj in data["projects"]:
        tech_tags = "".join([f'<span class="tech-tag">{html.escape(t)}</span>' for t in prj["tech"]])
        details_list = "".join([f'<li>{html.escape(d)}</li>' for d in prj["details"]])
        
        card = f"""
        <div class="project-card" data-category="{html.escape(prj['category'])}">
            <div class="project-header">
                <div class="project-badge"><i class="{prj['icon']}"></i> {html.escape(prj['category'])}</div>
                <span class="project-year">{html.escape(prj['year'])}</span>
            </div>
            <h3 class="project-title">{html.escape(prj['title'])}</h3>
            <p class="project-summary">{html.escape(prj['summary'])}</p>
            
            <div class="project-tech">
                {tech_tags}
            </div>
            
            <ul class="project-details">
                {details_list}
            </ul>
        </div>
        """
        project_cards.append(card)

    # Education HTML rendering
    edu_cards = []
    for edu in data["education"]:
        card = f"""
        <div class="timeline-item">
            <div class="timeline-dot"><i class="{edu['icon']}"></i></div>
            <div class="timeline-content glass-card">
                <div class="timeline-header">
                    <h3>{html.escape(edu['degree'])}</h3>
                    <span class="timeline-period">{html.escape(edu['period'])}</span>
                </div>
                <h4 class="timeline-sub">{html.escape(edu['institution'])}</h4>
                <div class="score-badge">{html.escape(edu['score'])}</div>
                <p class="timeline-desc">{html.escape(edu['highlight'])}</p>
            </div>
        </div>
        """
        edu_cards.append(card)

    # Achievements HTML rendering
    achieve_cards = []
    for ach in data["achievements"]:
        card = f"""
        <div class="achievement-card glass-card">
            <div class="achievement-icon">
                <i class="{ach['icon']}"></i>
            </div>
            <div class="achievement-body">
                <div class="achievement-top">
                    <span class="badge-tag">{html.escape(ach['badge'])}</span>
                    <span class="achievement-year">{html.escape(ach['year'])}</span>
                </div>
                <h3>{html.escape(ach['title'])}</h3>
                <h4>{html.escape(ach['organization'])}</h4>
                <p>{html.escape(ach['description'])}</p>
            </div>
        </div>
        """
        achieve_cards.append(card)

    # Stats HTML
    stats_html = "".join([
        f"""
        <div class="stat-box glass-card">
            <span class="stat-value">{html.escape(s['value'])}</span>
            <span class="stat-label">{html.escape(s['label'])}</span>
        </div>
        """ for s in data["stats"]
    ])

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(p['name'])} | Portfolio</title>
    <meta name="description" content="Portfolio of {html.escape(p['name'])}, {html.escape(p['title'])}. Specializing in Data Science, EDA, Python, SQL, and Software Engineering.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="css/styles.css?v=2">
</head>
<body>

    <!-- Background Elements -->
    <div class="bg-glow bg-glow-1"></div>
    <div class="bg-glow bg-glow-2"></div>
    <div class="bg-grid"></div>

    <!-- Navigation Header -->
    <header class="navbar">
        <div class="container nav-container">
            <a href="#" class="nav-logo">Jannatul<span class="logo-accent">.</span></a>
            
            <nav class="nav-links">
                <a href="#about" class="nav-item">About</a>
                <a href="#skills" class="nav-item">Skills</a>
                <a href="#projects" class="nav-item">Projects</a>
                <a href="#education" class="nav-item">Education</a>
                <a href="#achievements" class="nav-item">Achievements</a>
                <a href="#contact" class="nav-item">Contact</a>
                <a href="#contact" class="btn btn-primary btn-sm mobile-menu-cta mobile-only"><i class="fa-solid fa-paper-plane"></i> Get In Touch</a>
            </nav>

            <div class="nav-actions">
                <button id="theme-toggle" class="icon-btn" aria-label="Toggle Theme">
                    <i class="fa-solid fa-moon"></i>
                </button>
                <a href="#contact" class="btn btn-primary btn-sm nav-cta-btn">Get In Touch</a>
                <button id="mobile-menu-btn" class="icon-btn mobile-only" aria-label="Toggle Menu">
                    <i class="fa-solid fa-bars"></i>
                </button>
            </div>
        </div>
    </header>

    <main>
        <!-- Hero Section -->
        <section id="hero" class="hero-section">
            <div class="container hero-container">
                <div class="hero-content">
                    <div class="hero-badge">
                        <span class="pulsing-dot"></span> Available for Data Analyst Roles
                    </div>
                    <h1 class="hero-name">{html.escape(p['name'])}</h1>
                    <h2 class="hero-title">{html.escape(p['title'])}</h2>
                    <p class="hero-subtitle"><i class="fa-solid fa-graduation-cap"></i> {html.escape(p['subtitle'])}</p>
                    <p class="hero-location"><i class="fa-solid fa-location-dot"></i> {html.escape(p['location'])}</p>

                    <p class="hero-bio">{html.escape(p['bio'])}</p>

                    <div class="hero-cta">
                        <a href="#projects" class="btn btn-primary"><i class="fa-solid fa-rocket"></i> View Projects</a>
                        <a href="#contact" class="btn btn-outline"><i class="fa-solid fa-paper-plane"></i> Contact Me</a>
                    </div>

                    <div class="hero-socials">
                        <a href="mailto:{html.escape(p['email'])}" class="social-link" title="Email"><i class="fa-solid fa-envelope"></i></a>
                        <a href="{html.escape(p['linkedin'])}" target="_blank" rel="noopener" class="social-link" title="LinkedIn"><i class="fa-brands fa-linkedin"></i></a>
                        <a href="{html.escape(p['google_sites'])}" target="_blank" rel="noopener" class="social-link" title="Google Sites"><i class="fa-solid fa-globe"></i></a>
                        <a href="tel:{html.escape(p['phone'])}" class="social-link" title="Phone"><i class="fa-solid fa-phone"></i></a>
                    </div>
                </div>

                <div class="hero-visual">
                    <div class="avatar-card glass-card">
                        <div class="avatar-circle">
                            <i class="fa-solid fa-user-astronaut"></i>
                        </div>
                        <h3 class="avatar-name">{html.escape(p['name'])}</h3>
                        <p class="avatar-role">Data Analyst & Python Dev</p>

                        <div class="stats-grid">
                            {''.join(stats_html)}
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- About / Summary Section -->
        <section id="about" class="section">
            <div class="container">
                <div class="section-header">
                    <span class="section-subtitle">Overview</span>
                    <h2 class="section-title">About Me</h2>
                    <div class="title-bar"></div>
                </div>
                
                <div class="about-card glass-card">
                    <div class="about-icon-box">
                        <i class="fa-solid fa-chart-pie"></i>
                    </div>
                    <div class="about-text">
                        <h3>Turning Complex Data into Strategic Insights</h3>
                        <p>{html.escape(p['bio'])}</p>

                        <div class="highlights-grid">
                            <div class="highlight-item">
                                <i class="fa-solid fa-circle-check"></i>
                                <span>Exploratory Data Analysis (EDA) & Data Cleaning</span>
                            </div>
                            <div class="highlight-item">
                                <i class="fa-solid fa-circle-check"></i>
                                <span>Statistical Modeling & Feature Engineering</span>
                            </div>
                            <div class="highlight-item">
                                <i class="fa-solid fa-circle-check"></i>
                                <span>Data Visualization with Power BI & Python</span>
                            </div>
                            <div class="highlight-item">
                                <i class="fa-solid fa-circle-check"></i>
                                <span>Structured Programming & MVC Web Development</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Skills Section -->
        <section id="skills" class="section bg-alt">
            <div class="container">
                <div class="section-header">
                    <span class="section-subtitle">Technical Proficiency</span>
                    <h2 class="section-title">Skills & Expertise</h2>
                    <div class="title-bar"></div>
                </div>

                <div class="skills-wrapper">
                    {''.join(skills_sections)}
                </div>
            </div>
        </section>

        <!-- Projects Section -->
        <section id="projects" class="section">
            <div class="container">
                <div class="section-header">
                    <span class="section-subtitle">Portfolio Showcase</span>
                    <h2 class="section-title">Featured Projects</h2>
                    <div class="title-bar"></div>
                </div>

                <div class="projects-grid">
                    {''.join(project_cards)}
                </div>
            </div>
        </section>

        <!-- Education Section -->
        <section id="education" class="section bg-alt">
            <div class="container">
                <div class="section-header">
                    <span class="section-subtitle">Academic Journey</span>
                    <h2 class="section-title">Education</h2>
                    <div class="title-bar"></div>
                </div>

                <div class="timeline">
                    {''.join(edu_cards)}
                </div>
            </div>
        </section>

        <!-- Achievements Section -->
        <section id="achievements" class="section">
            <div class="container">
                <div class="section-header">
                    <span class="section-subtitle">Recognitions</span>
                    <h2 class="section-title">Honors & Achievements</h2>
                    <div class="title-bar"></div>
                </div>

                <div class="achievements-grid">
                    {''.join(achieve_cards)}
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="section bg-alt">
            <div class="container">
                <div class="section-header">
                    <span class="section-subtitle">Connect With Me</span>
                    <h2 class="section-title">Get In Touch</h2>
                    <div class="title-bar"></div>
                </div>

                <div class="contact-container">
                    <div class="contact-info glass-card">
                        <h3>Let's Collaborate!</h3>
                        <p>I am open to data analyst opportunities, research collaborations, and software projects. Feel free to reach out!</p>
                        
                        <div class="contact-details">
                            <div class="contact-item">
                                <div class="contact-icon"><i class="fa-solid fa-envelope"></i></div>
                                <div>
                                    <h4>Email</h4>
                                    <a href="mailto:{html.escape(p['email'])}">{html.escape(p['email'])}</a>
                                </div>
                            </div>

                            <div class="contact-item">
                                <div class="contact-icon"><i class="fa-solid fa-phone"></i></div>
                                <div>
                                    <h4>Phone</h4>
                                    <a href="tel:{html.escape(p['phone'])}">{html.escape(p['phone'])}</a>
                                </div>
                            </div>

                            <div class="contact-item">
                                <div class="contact-icon"><i class="fa-solid fa-location-dot"></i></div>
                                <div>
                                    <h4>Location</h4>
                                    <span>{html.escape(p['location'])}</span>
                                </div>
                            </div>

                            <div class="contact-item">
                                <div class="contact-icon"><i class="fa-brands fa-linkedin"></i></div>
                                <div>
                                    <h4>LinkedIn</h4>
                                    <a href="{html.escape(p['linkedin'])}" target="_blank" rel="noopener">Connect on LinkedIn</a>
                                </div>
                            </div>

                            <div class="contact-item">
                                <div class="contact-icon"><i class="fa-solid fa-globe"></i></div>
                                <div>
                                    <h4>Google Sites</h4>
                                    <a href="{html.escape(p['google_sites'])}" target="_blank" rel="noopener">Academic Webpage</a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <form id="contact-form" class="contact-form glass-card" action="https://formspree.io/f/sample" method="POST">
                        <h3>Send a Message</h3>
                        <div class="form-group">
                            <label for="name">Your Name</label>
                            <input type="text" id="name" name="name" placeholder="John Doe" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Your Email</label>
                            <input type="email" id="email" name="email" placeholder="john@example.com" required>
                        </div>
                        <div class="form-group">
                            <label for="subject">Subject</label>
                            <input type="text" id="subject" name="subject" placeholder="Project Inquiry / Job Opportunity" required>
                        </div>
                        <div class="form-group">
                            <label for="message">Message</label>
                            <textarea id="message" name="message" rows="5" placeholder="Hi Jannatul, I would like to discuss..." required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary btn-full"><i class="fa-solid fa-paper-plane"></i> Send Message</button>
                        <div id="form-status" class="form-status"></div>
                    </form>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-container">
            <div class="footer-left">
                <p>&copy; 2026 <strong>{html.escape(p['name'])}</strong>. Built with Python & Hosted on Netlify.</p>
            </div>
            <div class="footer-right">
                <a href="#hero" class="back-to-top"><i class="fa-solid fa-arrow-up"></i> Top</a>
            </div>
        </div>
    </footer>

    <!-- JS Scripts -->
    <script src="js/main.js"></script>
</body>
</html>
"""
    return html_content

def main():
    print("[BUILD] Compiling portfolio website from data.py...")
    html_output = generate_html(PORTFOLIO_DATA)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_output)
    print("[SUCCESS] Successfully generated index.html!")

if __name__ == "__main__":
    main()
