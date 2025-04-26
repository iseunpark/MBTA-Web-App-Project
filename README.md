# MBTA Web App Project

## 1. Project Overview

This project is a Flask-based web application designed to help users find the nearest MBTA station given a place name or address. Users can also interact with a Boston Tourist Chatbot to ask questions about Boston attractions, food, and travel tips. Key features include geocoding user input with the Mapbox API, finding nearby stations using the MBTA API, and integrating an AI chatbot directly onto the main page. In addition to meeting the basic requirements, I extended the project by embedding the chatbot directly within the home page, styling the web pages with an external CSS file, and organizing code into separate helper files for cleaner architecture.

---

## 2. Reflection

### Development Process

The development process began with setting up the APIs and testing basic functionality separately. One of the main challenges I faced was integrating the Mapbox and MBTA APIs correctly. Initially, I encountered errors when trying to retrieve latitude and longitude coordinates, mostly due to incorrect URL formatting and misunderstanding how the Mapbox API structured its responses. Once that was resolved, I also had to troubleshoot the MBTA API's requirements for latitude/longitude filters and response structures. I used ChatGPT during this process to help me pinpoint mistakes in the URL construction, clarified how to handle empty API responses, and suggested debugging techniques like adding print statements to inspect incoming data. 

### Work Division

I worked individually on this project. I planned to divide the work by first completing the MBTA location search functionality, then extending the app with the tourist chatbot integration afterward. This plan largely stayed on track. After implementing the basic MBTA search, I focused on improving the user experience by adding chatbot interaction and styling the website. I did not encounter major coordination issues since it was a solo project, but I did have to adjust my schedule slightly after realizing that setting up and correctly parsing API responses took longer than expected. Overall, careful pacing and early debugging helped keep the project under control.

### Learning Perspective

Through this project, I learned how to work with multiple APIs at once within a Flask web application. I gained significant experience with reading and handling JSON API responses, URL encoding, API key security, and modularizing helper functions for maintainability. I also practiced using AI tools like ChatGPT not just for coding help, but as a debugging partner, asking it to explain error messages, suggest tests, or check my logic. This made the development process faster and helped me understand common issues like incorrect URL construction or missing fields in API results. In the future, I plan to rely even more on structured debugging rather than assuming large chunks of code work correctly immediately. Overall, this project strengthened both my technical skills and my ability to approach problems systematically.

## Screenshots
**Error Message**  
![Error Message](screenshots/Capture.png)

**Debug Output**  
![Debug Output](screenshots/Capture2.png)

**Style Assistance**  
![Style Assistance](screenshots/Capture3.png)

---
Formatting assisted by ChatGPT