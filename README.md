# Web-Flask

Web application built with Flask.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Execution](#execution)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/frozin01/Web-Flask.git
    cd Web-Flask
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        venv\scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. **Setup Flask:**
    ```sh
    DEBUG=TRUE
    FLASK_PORT=5000
    FLASK_HOST=0.0.0.0
    ```

## Execution

1. **Ensure the virtual environment is activated.**

2. **Run the application:**
    ```sh
    python app.py
    ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Contributing

1. **Fork the repository.**

2. **Create a new branch:**
    ```sh
    git checkout -b feature/your-feature-name
    ```

3. **Make your changes.**

4. **Stage your changes:**
    ```sh
    git add .
    ```

5. **Commit your changes:**
    ```sh
    git commit -m 'Add some feature'
    ```

6. **Push to the branch:**
    ```sh
    git push origin feature/your-feature-name
    ```
    
7. **Submit a pull request.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.