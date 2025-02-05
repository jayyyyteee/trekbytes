# TrekBytes Blog

Welcome to the TrekBytes Blog! This project is a Django-based web application that serves as a personal blog to document travels and experiences. The blog features posts with images, geolocation tracking, and an about me section.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Home Page**: Displays recent blog posts with images.
- **All Posts Page**: Lists all blog posts.
- **Post Detail Page**: Shows detailed view of a single post with additional images and content.
- **About Me Page**: Provides information about the blog author.
- **Geolocation Tracking**: Allows users to track and display their location on a map.
- **Responsive Design**: Ensures the blog is accessible on various devices.

## Installation

To get a local copy up and running, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/trekbytes-blog.git
    cd trekbytes-blog
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following variables:
    ```env
    SECRET_KEY=your_secret_key
    AWS_ACCESS_KEY_ID=your_aws_access_key_id
    AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
    ```

5. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## Usage

- **Home Page**: Visit [http://127.0.0.1:8000/](http://_vscodecontentref_/0) to see the home page with recent posts.
- **All Posts**: Visit [http://127.0.0.1:8000/posts](http://_vscodecontentref_/1) to see all blog posts.
- **Post Detail**: Click on any post to see its detailed view.
- **About Me**: Visit [http://127.0.0.1:8000/aboutme](http://_vscodecontentref_/2) to learn more about the author.
- **Track Location**: Visit [http://127.0.0.1:8000/trackme](http://_vscodecontentref_/3) to track and display your location.

