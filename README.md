# Task Management App with Google Login

## **Overview**

This is a simple task management web application built using **Django**. The app allows users to manage their personal tasks after logging in with their **Google account**. It demonstrates Google authentication and basic CRUD (Create, Read, Update, Delete) operations for tasks.

---

## **Features**

1. **Google Authentication**:  
   - Users can log in securely with their Google account.  
   - Google OAuth integration ensures seamless and secure authentication.
<br>


   <img src="https://github.com/vish1108/Django_task_management_app/blob/master/task_management_app/static/auth_error.png" alt="Google Auth Error" width="500"/>   

3. **Task Management**:  
   - **Create** tasks with a title and description.  
   - **View** a list of all tasks.  
   - **Edit** task details.  
   - **Delete** tasks.
   <br>
  
   <img src="https://raw.githubusercontent.com/vish1108/Django_task_management_app/master/task_management_app/static/google_login.png" alt="Google Login" width="500"/>


4. **Bootstrap Styling**:  
   - Basic UI enhancements using Bootstrap for a clean and responsive design.
<br>

  <img src="https://github.com/vish1108/Django_task_management_app/blob/master/task_management_app/static/bootstarp_on_website.png" alt="Bootstrap on Website" width="500"/>

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.x
- Django
- Google Developer Console account for creating credentials

### **Steps to Run the Project**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vish1108/Django_task_management_app.git
   cd task-management-app


### Project Status

1. **Implemented Features**:
   - User task list with CRUD functionality.
   - Token-based user invitation and partial registration flow.

2. **Pending Work**:
   - Completing the registration form logic after receiving a valid token.
   - Handling invalid or expired tokens gracefully.

3. **Challenges**:
   - Encountered issues with integrating the token validation with the user registration form.

4. **Next Steps**:
   - Plan to refine the `register` view and connect it with the user model to complete the registration process.

