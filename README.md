# 🐍 Snake Game (Tkinter & OOP)

---

## 🇬🇧 English Section

An upgraded, modern, and challenging version of the nostalgic classic Snake game, built using Python's **Tkinter** GUI library based on **Object-Oriented Programming (OOP)** principles.

### 🚀 Features
- **Smart Settings Menu:** Customize the game before starting via a separate GUI window (`Toplevel`).
- **Dynamic Difficulty Levels:**
  - **Easy:** No obstacles, slow and steady speed.
  - **Normal:** 8 random obstacles, medium speed, and progressive acceleration upon eating food.
  - **Hard:** 15 challenging obstacles, high initial speed, and rapid acceleration (a true test of reflexes).
- **Modern Game Themes:** - *Candy:* Purple background, pink/red snake, white obstacles.
  - *Classic:* Black background, green snake, red food (Nostalgic vibe).
  - *Neon:* Cyberpunk style with cyan snake, magenta food, and yellow obstacles on a black screen.
- **Wrap-around Logic:** Hitting the main walls doesn't result in a Game Over! The snake teleports to the opposite side of the screen.
- **Smart Object Distribution:** An algorithm ensures food and obstacles never spawn at the snake's starting point or overlap with each other.

### 🛠️ Technologies Used
- **Python 3.x:** Core game logic.
- **Tkinter (Canvas & Toplevel):** For window management, graphics rendering, and the settings menu.
- **Random Library:** For random coordinate generation.
- **Git & GitHub:** Version control, debugging `.lock` conflicts, and managing isolated repositories.

### 🧠 What I Learned (Engineering Achievements)
1. **Object-Oriented Programming (OOP):** Decoupling game entities into independent `Snake`, `Food`, and `Obstacle` classes for better maintainability and scalable code.
2. **Game Loop & Time Management:** Using Tkinter's `.after()` method to advance frames (Ticks) without blocking the main thread or keyboard event listeners.
3. **Collision Detection Algorithms:** Implementing mathematical coordinate comparisons between the snake's head, its body parts, and static obstacle arrays.
4. **Wrap-around Logic:** Handling screen boundaries via `if/else` conditions to create a seamless wall-passing experience.
5. **State & Global Variables Management:** Dynamically updating game states (Score, Slowness, Direction) across different functions.
6. **Advanced Git Debugging:** Resolving deep repository issues like `index.lock` errors, directory permission denials, and executing isolated force-pushes (`--force`).

### 📺 Gameplay Demo


https://github.com/user-attachments/assets/a2bf486d-ace2-4887-8d16-8e5679faab92



بخش فارسی
یک نسخه ارتقایافته، مدرن و کاملاً چالشی از بازی نوستالژیک و کلاسیک مار که با استفاده از کتابخانه گرافیکی در پایتون و بر پایه اصول برنامه‌نویسی شیءگرایی طراحی و پیاده‌سازی شده است.

🚀 ویژگی‌ها
منوی تنظیمات هوشمند: امکان سفارشی‌سازی کامل بازی قبل از شروع در یک پنجره مجزا (Toplevel).

سطوح سختی داینامیک:

Easy: بدون موانع محیطی، سرعت حرکت آرام و ثابت.

Normal: دارای ۸ مانع تصادفی در نقشه، سرعت متوسط و افزایش شتاب تدریجی با خوردن هر غذا.

Hard: دارای ۱۵ مانع چالش‌برانگیز، سرعت اولیه بالا و شتاب‌گیری بسیار سریع (تست تمرکز و واکنش).

تم‌های گرافیکی جذاب: پشتیبانی از ۳ استایل رنگی (Candy, Classic, Neon).

قانون عبور از دیوارها (Wrap-around): برخورد با دیوارهای اصلی باعث باختن نمی‌شود! مار با عبور از هر لبه صفحه، از سمت مقابل خارج می‌شود.

سیستم هوشمند توزیع اشیاء: الگوریتم توزیع غذا و موانع به شکلی پیاده‌سازی شده که هیچ مانع یا غذایی در نقطه شروع حرکت مار یا روی یکدیگر ظاهر نشوند.

🛠️ ابزارها و تکنولوژی‌ها
Python 3.x: زبان برنامه‌نویسی اصلی پروژه.

Tkinter: برای مدیریت پنجره اصلی، لایه گرافیکی بازی و منوی تنظیمات.

Random Library: جهت پیاده‌سازی محاسبات تصادفی.

Git & GitHub: کنترل نسخه، کالبدشکافی خطاهای سیستمی و ایزوله‌سازی مخازن.

🧠 دستاوردهای مهندسی و آموخته‌ها
۱. برنامه‌نویسی شیءگرا (OOP): تفکیک کامل موجودیت‌های بازی در قالب کلاس‌های مجزای Snake، Food و Obstacles جهت توسعه‌پذیری و تمیزی کد.


۲. حلقه بازی و مدیریت زمان: تسلط بر متد .after() برای تولید فریم‌های بازی بدون فریز شدن ترد اصلی سیستم.


۳. الگوریتم‌های سنجش برخورد (Collision Detection): طراحی منطق بررسی تداخل‌های مختصات سر مار با کل تکه‌های بدنش و آرایهٔ موانع ثابت.


۴. منطق مرزی (Wrap-around Logic): مدیریت مرزهای صفحه نمایش با دستورات شرطی.


۵. مدیریت State و متغیرهای سراسری: کنترل داینامیک سرعت بازی، امتیاز و جهت حرکت.


۶. دیباگ پیشرفته گیت: یادگیری ریشه‌ای خطاهای قفل مخزن (index.lock)، تداخل‌های مسیر و مدیریت فضاهای محلی امن (Force Push).
