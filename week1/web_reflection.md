What happens when you type a URL in your browser and press Enter?
When you type a URL like "facebook.com" into your browser and press Enter, the first thing that happens is that your computer, which is called the client, does not know the IP address of the website. The computer cannot understand the website name directly because it works with numbers. Therefore, it needs help from the Domain Name System (DNS). The DNS translates the typed URL into an IP address that the computer understands.

After that, the request goes through a load balancer. The load balancer controls the number of users trying to access the website at the same time by distributing the requests across different servers so that there is no traffic overload.

The web server then displays the interface of the website. If there is no need to process any logic, the request ends at the web server. However, if the website needs to process logic, the request is sent to the application server.

The application server is responsible for handling the logic behind the website. If the application server needs more information, it communicates with the database.

The database stores and manages the data used by the website.

Difference between web server and application server

A web server is responsible for displaying the interface of a website and serving static content such as images and web pages. For example, when you visit a school portal and only view announcements or course information, the web server sends that information to your browser.

An application server is responsible for processing the logic of a website. For example, when you  log into the school portal to check you results or register for courses, the application server processes the request and retrieves information from the database.

why the client never talks directly to the database 

  The database is only for retrieving information stored by the developers; therefore, a client does not have the right to access it.The client will need the help of a server to communicate with the database.If clients were to talk directly to  the database, it would create a massive risk as hackers could easily attack their credentials.