# A Online Python Compiler

The Online Python Compiler is a fully functional, web-based coding environment that allows users to write, run, and test Python code directly from their browser—without installing any additional software. Designed with Django as the backend framework and a clean, responsive frontend built with HTML, CSS, JavaScript, and Bootstrap, this project delivers a smooth and intuitive Python coding experience suitable for both beginners and advanced users.

Whether you're a student practicing Python syntax, an instructor conducting live demos, or a developer looking to test small code snippets quickly, this tool provides a distraction-free and efficient workflow. The platform executes Python code securely on the server side and delivers real-time output instantly on the user interface. Because everything runs inside the browser, there's no need to worry about environment setup, interpreter installation, or system compatibility issues—making this the perfect solution for learning, teaching, and experimenting with Python online.

The user interface is thoughtfully designed to be minimal yet powerful. With a central code editor and a dedicated output display section, users can focus entirely on coding. Built using PyCharm for a clean and modular development approach, this project is structured for easy customization, scalability, and maintenance. Moreover, the system uses a PostgreSQL database only for storing user feedback and contact messages—no user code is ever stored, ensuring complete privacy and stateless execution.

This project stands out as an excellent choice for educational institutions, online learning platforms, coding bootcamps, or personal use. It allows seamless integration into learning portals or deployment as a standalone tool to give users immediate hands-on experience with Python. Since the project is designed with performance, security, and simplicity in mind, it offers a hassle-free solution that works across all major browsers and devices, empowering users to code anytime, anywhere.

<br>

🔗 [Check Out The Live Version Of This Project Here.](https://online-python-compiler-liard.vercel.app/)

<br>

## ✨ Features Of Online Python Compiler

-  **Real-Time Code Execution** – Instantly runs Python code and displays output within the browser.

-  **No Local Setup Required** – No Python installation needed.

-  **Django-Powered Backend** – Fast and secure code execution handled server-side.

-  **Responsive & Clean UI** – Frontend built with Bootstrap for a seamless user experience.

-  **Supports All Skill Levels** – Friendly for both beginners and experienced developers.

-  **Structured Codebase** – Developed using PyCharm with modular and scalable architecture.

-  **Secure Data Handling** – Only feedback/messages stored via PostgreSQL; user code is never stored.

-  **Cross-Browser Compatibility** – Works on Chrome, Firefox, Safari, Edge, etc.

-  **Perfect for Learning & Teaching** – Ideal for schools, educators, and self-learners.

-  **Lightweight & Fast** – Optimized for minimal lag and fast response.


## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap  

- **Backend**: Python, Django  

- **Database**: PostgreSQL (used only for storing contact form feedback)

- **IDE Used**: PyCharm

  
## Screenshots

**1. Home Page** 

![Home Page](screenshots/home.png)

**2. Compiler Page** 

![Home Page](screenshots/compiler.png)

**3. Contact Us Page** 

![Home Page](screenshots/contact_us.png)

**4. About Page** 

![Home Page](screenshots/about_us.png)


##  🧰  Installation & Setup

**1. Clone the Repository**

   ```
git clone https://github.com/VishwajitPatil0822/Online-Python-Compiler.git

   cd Online-Python-Compiler
   ```

**2. Create & Activate a Virtual Environment**

    python -m venv myvenv
    myvenv\Scripts\activate

**3. Install dependencies**

    pip install -r requirements.txt

**4. Configure PostgreSQL**

- Go to https://neon.tech
- Sign up for a free account using your email or GitHub
- After signing in, click “New Project”.
- Enter a project name, select your region, and click “Create Project”.
- Once your project is created, you will see your Database URL in the Connection Details tab. It will look something like this:

        postgres://username:password@your-db-host.neon.tech/dbname?sslmode=require

- Paste your PostgreSQL database URL like in ```.env``` file like this:

        DATABASE_URL=postgres://username:password@your-db-host.neon.tech/dbname?sslmode=require

**5. Run Migrations**

        python manage.py migrate

**6. Start the Development Server**

        python manage.py runserver


## 📬 Contact

If you have any questions, suggestions, or want to collaborate, feel free to reach out:

- 💌 Email: [vishwajit22patil@gmail.com](mailto:vishwajit22patil@gmail.com)

- 🐙 GitHub: [github.com/VishwajitPatil0822](https://github.com/VishwajitPatil0822)

- 💼 LinkedIn: [linkedin.com/in/vishwajitpatil-pythondev](https://www.linkedin.com/in/vishwajitpatil-pythondev/)

- 🌐 Portfolio: [vishwajit-patil-portfolio.vercel.app](https://vishwajit-patil-portfolio.vercel.app/)
 

## ❤️ Support

If you like this project, give it a ⭐ on [GitHub](https://github.com/VishwajitPatil0822/Online-Python-Compiler)!  
You can also share it with your friends.

Thank you for checking it out! 🚀


### Created with ❤️ by Vishwajit Patil
