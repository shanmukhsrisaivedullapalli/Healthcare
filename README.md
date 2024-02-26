# Healthcare Management System
![Screenshot (129)](https://github.com/shanmukhsrisaivedullapalli/Healthcare/assets/90882705/2ae66965-fc17-40c9-842a-7a64f755ec58)
![Screenshot (130)](https://github.com/shanmukhsrisaivedullapalli/Healthcare/assets/90882705/86642171-8c46-4318-83af-f09256fddabf)
![Screenshot (131)](https://github.com/shanmukhsrisaivedullapalli/Healthcare/assets/90882705/16d4061e-36c9-4353-8609-d8df47b9ee39)



## Introduction

Healthcare Management System is a web application designed to streamline the management of healthcare facilities. It provides an integrated platform for managing patients, appointments, medical records, and more.

## Features

- **Patient Management**: Easily add, edit, and delete patient records.
- **Medical Records**: Maintain detailed medical records for each patient.
- **Billing and Invoicing**: Generate invoices and manage billing for services provided.
- **User Management**: Admin dashboard for managing users with different roles and permissions.

## Installation

To run the Healthcare Management System on your local machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/healthcare-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Healthcare
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

4. Set up the database:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

1. **Admin Dashboard**: Log in with the superuser account to access the admin dashboard.
2. **Patient Management**: Add, edit, or delete patient records.
3. **Appointment Scheduling**: Schedule appointments for patients with doctors.
4. **Medical Records**: View and manage detailed medical records for each patient.
5. **Billing and Invoicing**: Generate invoices and manage billing for services provided.

## Contributing

Contributions are welcome! Please follow these guidelines when contributing:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive messages.
- Push your changes to your fork.
- Submit a pull request to the main repository.
