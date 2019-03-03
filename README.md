## Beanstack

### About
Beanstack is the result of a team project for the Internet Technology Course of the Msc in Software Development at the University of Glasgow. 

The aim of the project was to implement a basic CRUD Django app, with some API integration. The app features information about various coffee beans, such as taste profile and where users around Glagow can expect to find beans, they find on the app. 

The app uses the ZingChart API to create a 'taste profile graph' for each coffee. Users can vote on the individual 'taste components' and update the graph. 

Integration with the GoogleMaps API allows users to see stores around them that stock the certain coffees and to look for real coffee shops in the area.



### Installation

"# beanstack" 

**Google Api key:**
1. Either go to  https://developers.google.com/maps/web-services/ , sign in 
and get the api key or use the provided api key.
2. Create a file called google_maps_api.key 
in the main project directory (ie the same directory as manage.py and requirements.py)
and put the key in it.
3. From there they key will automatically be read in to BeanStack

**Facebook Api Id and secret key:** 
1. Create two files in the same directory as the google api key above - 
social_auth_facebook_key.key and social_auth_facebook_secret.key.
2. Put the provided facebook keys into these files 


**PythonAnywhere URL for the app:**

https://beanstack.pythonanywhere.com/
