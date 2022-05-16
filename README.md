# Simmi Foundation Job Hub
# Assignment Submission related to the post of Intern @ Simmi FOundation
By Abhijit Barui            Ph: +91-8335076174              email: abhijitongit@gmail.com

# Description:
        This project required following features to be implemented:
        Authentication(Register/Login functionality)
        Database Integration
        Django Forms Data Submission through Web Application
        Rendering Data from Database to Frontend        
        However we were asked to use some Creativity to make the project look professional.

        So I decided to design a Web Application where devs can put up job openings available in
        the company and applicants can check for vacancies and apply from the website itself.
        Additional features include 
        <a>reviewing those applications and shortlisting them from webapp.
        <b>Dashboard/Profile where applicants can check their job application status.

# requirements
        Python programming language installed in the desktop environment
        Terminal
        Source Code Editor(used VSCode for this particular project)
        PostgreSQL for Database(No need since Default sql database is set for making process easier)

# how-to-operate:
        Creating and activating a Virtual environment before cloning in the machine is suggested.
        Install dependencies using the requirements.txt
        run makemigrations and migrate the database to default database(since postgres needs to be set up)
        create a superuser and go to localhost:port/admin and log in for viewing full functionality]
                or you can just run it normally and register as a normal user
        runserver

# Challenges faced while making this:
        •FrontEnd was involved and due to lack of experience I chose to go with normal HTML scripts but found a nice
         Bootstrap usable. Learnt how to work well with bootstrap.Made minor changes in HTML 
        •Database relations became complicated with three tables Applications Jobs and Users but solving it helped me
        learn more about table relations and django models
        •Learned how to upload files through forms
        •Logout functioning using JavaScript

# Features to be implemented:
        Search function in 
        careers page to navigate through jobs, 
        admin area/view job types page to navigate through job types, 
        admin area/view job types/view applications page to navigate through applications
        Proper Frontend
        Host it in a cloud service

# Apologies
        for exposing secret key not being able to share .env file