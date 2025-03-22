---
hide:
  - navigation
  - toc
---

<style>
.hero {
  padding: 4rem 0;
  text-align: center;
  background: linear-gradient(135deg, var(--md-primary-fg-color) 0%, var(--md-primary-fg-color--light) 100%);
  color: white;
  border-radius: 8px;
  margin-bottom: 3rem;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.hero p {
  font-size: 1.2rem;
  max-width: 800px;
  margin: 0 auto 2rem;
  opacity: 0.9;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 2rem;
}

.hero-button {
  display: inline-block;
  padding: 0.8rem 1.5rem;
  border-radius: 4px;
  font-weight: 600;
  transition: all 0.3s ease;
  text-decoration: none;
}

.primary-button {
  background-color: white;
  color: var(--md-primary-fg-color);
}

.primary-button:hover {
  background-color: #f5f5f5;
  transform: translateY(-2px);
}

.secondary-button {
  background-color: rgba(255, 255, 255, 0.2);
  color: white;
}

.secondary-button:hover {
  background-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
}

.section-title {
  font-size: 2rem;
  text-align: center;
  margin: 2rem 0;
  position: relative;
  padding-bottom: 0.5rem;
}

.section-title::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 4px;
  background-color: var(--md-primary-fg-color);
  border-radius: 2px;
}

.course-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.course-card {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.course-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.card-content {
  padding: 1.5rem;
  flex-grow: 1;
}

.card-title {
  font-size: 1.4rem;
  margin-top: 0;
  margin-bottom: 1rem;
  color: var(--md-primary-fg-color);
}

.card-footer {
  padding: 1rem 1.5rem;
  text-align: right;
}

.card-link {
  color: var(--md-primary-fg-color);
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  transition: all 0.3s ease;
}

.card-link:hover {
  color: var(--md-primary-fg-color--light);
}

.card-link .material-icons {
  margin-left: 0.5rem;
  font-size: 1.2rem;
}

.features-section {
  padding: 3rem 2rem;
  border-radius: 8px;
  margin: 3rem 0;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  transition: all 0.3s ease;
}

.feature-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--md-primary-fg-color);
}

.feature-title {
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.newsletter {
  padding: 2rem;
  border-radius: 8px;
  margin: 3rem 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  border: none;
}

.newsletter h4 {
  font-size: 1.4rem;
  margin-top: 0;
  color: var(--md-primary-fg-color);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.newsletter-body {
  padding: 1rem 0;
}

.newsletter-frame {
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
  display: block;
}

.author-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  margin: 3rem 0;
}

.author-image {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 1.5rem;
  border: 4px solid var(--md-primary-fg-color);
}

.author-bio {
  max-width: 700px;
  margin: 0 auto;
}

.social-links {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}

.social-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  color: white;
  transition: all 0.3s ease;
}

.social-link:hover {
  transform: translateY(-3px);
}
</style>

<div class="hero">
  <h1>Programming for Data Science</h1>
  <p>A comprehensive and dynamic course designed to equip you with the skills to thrive in the world of data science</p>
  <div class="hero-buttons">
    <a href="#courses" class="hero-button primary-button">Explore Courses</a>
    <a href="#about" class="hero-button secondary-button">About the Author</a>
  </div>
</div>

<h2 class="section-title" id="courses">What You Will Learn</h2>

<div class="course-cards">
  <div class="course-card">
    <div class="card-image" style="height: 160px; overflow: hidden; position: relative;">
      <img src="https://images.unsplash.com/photo-1526379095098-d400fd0bf935?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Python Programming" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">
    </div>
    <div class="card-content">
      <h3 class="card-title">Python Programming</h3>
      <p>Start with the basics of Python, a versatile and powerful programming language. This course lays the foundation for your data science journey.</p>
    </div>
    <div class="card-footer">
      <a href="/Python/11_python_tutorial/" class="card-link">
        Get Started
        <span class="material-icons">arrow_forward</span>
      </a>
    </div>
  </div>
  
  <div class="course-card">
    <div class="card-image" style="height: 160px; overflow: hidden; position: relative;">
      <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Python Data Analysis" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">
    </div>
    <div class="card-content">
      <h3 class="card-title">Python Data Analysis</h3>
      <p>Explore data analysis using libraries like Pandas, NumPy, and Matplotlib. Learn to transform raw data into actionable insights.</p>
    </div>
    <div class="card-footer">
      <a href="/Data%20Collection%20and%20Visulization/31_matplotlib_refined/" class="card-link">
        Get Started
        <span class="material-icons">arrow_forward</span>
      </a>
    </div>
  </div>
  
  <div class="course-card">
    <div class="card-image" style="height: 160px; overflow: hidden; position: relative;">
      <img src="https://images.unsplash.com/photo-1515879218367-8466d910aaa4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Machine Learning (Python)" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">
    </div>
    <div class="card-content">
      <h3 class="card-title">Machine Learning (Python)</h3>
      <p>Discover the principles of machine learning and gain hands-on experience in building and optimizing models.</p>
    </div>
    <div class="card-footer">
      <a href="/Machine%20Learning/41_overview_of_machine_learning/" class="card-link">
        Get Started
        <span class="material-icons">arrow_forward</span>
      </a>
    </div>
  </div>
</div>

<div class="features-section">
  <h2 class="section-title">Why Choose This Course?</h2>
  
  <div class="features-grid">
    <div class="feature-item">
      <span class="material-icons feature-icon">code</span>
      <h3 class="feature-title">Hands-On Learning</h3>
      <p>Each module is designed with practical exercises and real-world projects to ensure you can apply what you've learned.</p>
    </div>
    
    <div class="feature-item">
      <span class="material-icons feature-icon">route</span>
      <h3 class="feature-title">Flexible Learning Path</h3>
      <p>Choose to follow the entire course or focus on specific modules that meet your individual learning goals.</p>
    </div>
    
    <div class="feature-item">
      <span class="material-icons feature-icon">psychology</span>
      <h3 class="feature-title">Expert Guidance</h3>
      <p>Gain insights from industry professionals who are passionate about data science and dedicated to your success.</p>
    </div>
    
    <div class="feature-item">
      <span class="material-icons feature-icon">trending_up</span>
      <h3 class="feature-title">Career-Ready Skills</h3>
      <p>By the end of this course, you'll be ready to tackle data science challenges, whether you're transitioning careers or enhancing your current role.</p>
    </div>
  </div>
</div>

<div class="newsletter">
  <h4><span class="material-icons">notifications</span> Don't Miss Any Updates!</h4>
  <div class="newsletter-body">
    <p>
      To be among the first to hear about future updates of the course materials, simply enter your email below, follow us on 
      <a href="https://x.com/dataideaorg"><span class="material-icons" style="font-size: 1rem; vertical-align: middle;">open_in_new</span> Twitter</a>, 
      or subscribe to our <a href="https://www.youtube.com/@dataidea-science"><span class="material-icons" style="font-size: 1rem; vertical-align: middle;">play_circle</span> YouTube channel</a>.
    </p>
    <iframe class="newsletter-frame" src="https://embeds.beehiiv.com/5fc7c425-9c7e-4e08-a514-ad6c22beee74?slim=true" data-test-id="beehiiv-embed" height="52" frameborder="0" scrolling="no"></iframe>
  </div>
</div>

<div class="author-section" id="about">
  <img src="./assets/logo.png" alt="Juma Shafara" class="author-image">
  <h2>About the Author</h2>
  <div class="author-bio">
    <p>Hi, My name is Juma Shafara. I am a Data Scientist at Raising The Village and Instructor at DATAIDEA. I have taught hundreds of people Programming, Data Analysis, and Machine Learning.</p>
    <p>I enjoy developing innovative algorithms and models that can drive insights and value. I regularly share content that I find useful throughout my work/learning/teaching journey to simplify concepts in Machine Learning, Mathematics, Programming, and related topics on my website <a href="https://jumashafara.dataidea.org">jumashafara.dataidea.org</a>.</p>
    <p>Besides these technical stuff, I enjoy watching soccer, movies, and reading mystery books.</p>
  </div>
  <div class="social-links">
    <a href="https://twitter.com/jumashafara" class="social-link" target="_blank"><span class="material-icons">language</span></a>
    <a href="https://github.com/jumashafara" class="social-link" target="_blank"><span class="material-icons">code</span></a>
    <a href="mailto:example@email.com" class="social-link"><span class="material-icons">email</span></a>
  </div>
</div>

<small style="display: block; text-align: center; margin-top: 2rem; color: #888;">
  **Last Updated:** November 5, 2024 | **Author:** Juma Shafara
</small>
