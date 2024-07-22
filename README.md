# Angular User Management Project

This is an Angular project that includes a login screen and functionalities for listing users and performing CRUD (Create, Read, Update, Delete) operations on users.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)

## Features

- **Login Screen**: Secure authentication for users.
- **User Listing**: Display a list of all users.
- **CRUD Operations**: Create, Read, Update, and Delete user details.

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/angular-user-management.git
    cd angular-user-management
    ```

2. **Install dependencies**
    ```bash
    npm install
    ```

3. **Run the application**
    ```bash
    ng serve
    ```

    The application will be available at `http://localhost:4200/`.

## Usage

1. **Login**
   - Navigate to the login page and enter your credentials.
   
2. **User Management**
   - After logging in, you will be redirected to the user list page.
   - You can add a new user by clicking on the "Add User" button.
   - Edit or delete an existing user by using the corresponding buttons next to each user.

## Project Structure

```plaintext
src/
├── app/
│   ├── login/
│   │   ├── login.component.html
│   │   ├── login.component.ts
│   ├── user/
│   │   ├── user-list/
│   │   │   ├── user-list.component.html
│   │   │   ├── user-list.component.ts
│   │   ├── user-detail/
│   │   │   ├── user-detail.component.html
│   │   │   ├── user-detail.component.ts
│   │   ├── user.service.ts
│   ├── app-routing.module.ts
│   ├── app.component.html
│   ├── app.component.ts
│   ├── app.module.ts
└── assets/
    └── (images, styles, etc.)
```

## Technologies Used
	•	Angular: Frontend framework for building the application.
	•	Angular CLI: Command-line interface for Angular.
	•	TypeScript: Superset of JavaScript for type safety.
	•	HTML/CSS: Markup and styling

## Future Enhancements

	1.	Handle Pagination: Implement pagination to improve the user experience when dealing with large datasets.
	2.	Handle Loading State: Add loading indicators to improve user feedback during data fetch operations.
	3.	Add Unit Testing: Implement unit tests to ensure the reliability and maintainability of the codebase.

