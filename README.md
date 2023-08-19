# Life Organizer Backend API

The Life Organizer Backend API is the heart of a comprehensive life organization app, offering a range of features to help you manage your tasks, calendars, notes, habits, sleep patterns, and more. This Django-based backend provides a robust foundation for your life organization needs, allowing you to focus on staying productive and organized.

## Features

- Task Management: Create, update, and track your tasks effortlessly.
- Calendar Integration: Seamlessly schedule and manage your events and appointments.
- Notes: Capture and organize your thoughts, ideas, and important information.
- Habit Tracker: Build and maintain positive habits with a dedicated habit tracking system.
- Sleep Tracker: Monitor and analyze your sleep patterns to optimize your rest.
- And More: This API forms the backbone of your life organization app, with the potential for further expansion and customization.

## How to Use

Follow these steps to set up and run the Life Organizer Backend API on your local machine using `pipenv`:

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/life-organizer-backend.git
   cd life-organizer-backend
   ```

2. **Install Dependencies:**
   Ensure you have `pipenv` installed. If not, install it using:
   ```
   pip install pipenv
   ```

   Then, install the project dependencies:
   ```
   pipenv install
   ```

3. **Database Setup:**
   Make sure you have a PostgreSQL server installed and running. Create a database for the app to use and a user with access to that database. Update the `.env` file with the following configuration parameters:

   ```
   DB_NAME=planner
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. **Create .env File:**
   Create a `.env` file in the root directory of the project and add the following configuration parameters:

   ```
   DEBUG=True
   DOMAIN_NAME=example.com
   SECRET_KEY=your_secret_key
   ```

   Update the remaining properties in the `.env` file to match your project requirements.

5. **Run Migrations:**
   Apply the database migrations to set up the initial schema:
   ```
   pipenv run python manage.py makemigrations
   pipenv run python manage.py migrate
   ```

6. **Run the Development Server:**
   Start the development server with the following command:
   ```
   pipenv run python manage.py runserver
   ```

7. **Access the API:**
   The API will be accessible at `http://localhost:8000/`. You can explore the available endpoints and start integrating the backend into your life organization app.

Feel free to customize and extend the API to match your specific requirements and build a complete life organization solution. Happy organizing!

---

**Note:** This project is under active development, and improvements and new features are regularly added. If you encounter any issues or have suggestions, please open an issue or contribute to the repository. Your feedback is highly appreciated.
