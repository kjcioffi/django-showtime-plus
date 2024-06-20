# ShowTime+ Application

## Project Overview

**Ever wonder what's currently in theaters?**

While Google, Rotten Tomatoes, and IMDb provide movie information, they can sometimes be cumbersome and overwhelming when you need quick, concise details to make an informed decision.

**ShowTime+** is a streamlined platform designed for users who want just enough information about movies currently in theaters, all in one place. Our goal is to offer an experience that is both informative and easy to navigate, helping you make an informed decision without the clutter.

The platform features a list of popular movies, and users can click on each movie to view more details.

## Running the Project

To run the ShowTime+ project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone [repository-url]
    cd showtime-plus
    ```

2. **Create an account** on [The Movie Database (TMDB)](https://developer.themoviedb.org/docs/getting-started) and request an API key.

3. **Set up environment variables**:
    - At the root of the directory, create a `.env` file with the following configurations:
        ```env
        DEBUG=TRUE
        ALLOWED_HOSTS=localhost,127.0.0.1
        SECRET_KEY=<your-secret-key>  # Optionally create one using: python -c 'from django.core.management.utils get_random_secret_key; print(get_random_secret_key())'
        TMDB_API_KEY=<your-tmdb-api-key>
        ```

4. **(Optional) Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

5. **Install dependencies**:
    ```bash
    pip install -r requirements/requirements.txt
    pip install -r requirements/dev/requirements-dev.txt
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

You should now be able to access the application at `http://localhost:8000`.

---

Feel free to customize the repository URL, add any additional setup instructions, or include more details about the project as needed.
