User Accesses Website:
https://github.com/EDWINWASARI/alx-system_engineering-devops/commit/70bcad3242b5cc31bfa1d0fad486e643f63e7bec#commitcomment-139031540

A user types www.foobar.com into their web browser.
Domain Name:

The domain name, foobar.com, serves as a human-readable alias for the server's IP address (e.g., 8.8.8.8).
DNS Record:

The DNS (Domain Name System) record for www.foobar.com points to the server's IP address (e.g., 8.8.8.8). The www record is a CNAME (Canonical Name) record that acts as an alias for the domain.
Server:

A server is a physical or virtual machine that hosts the web infrastructure. It stores and serves website files, processes requests, and communicates with clients over the internet.
Web Server (Nginx):

Nginx is the web server software responsible for handling incoming HTTP requests from clients (browsers) and serving static content (HTML, CSS, JavaScript files). It forwards dynamic requests to the application server.
Application Server:

The application server is responsible for executing application code (e.g., PHP, Python, Ruby) and generating dynamic content based on client requests. It communicates with the web server to process and deliver dynamic content to clients.
Application Files:

The application files contain the website's code base, including scripts, templates, and other resources required to generate dynamic web pages.
Database (MySQL):

MySQL is the relational database management system (RDBMS) used to store and manage website data, such as user accounts, posts, and other information. It interacts with the application server to retrieve and store data as requested by the application.
Communication with User's Computer:

The server communicates with the user's computer using the HTTP (Hypertext Transfer Protocol) or HTTPS (HTTP Secure) protocols. When a user requests a webpage, the server responds with the corresponding HTML content, which the browser renders for the user to view.
Issues with this infrastructure:

Single Point of Failure (SPOF):

Since all components are hosted on a single server, any hardware or software failure can lead to downtime for the entire website.
Downtime During Maintenance:

When deploying new code or performing maintenance tasks, the web server needs to be restarted, causing downtime for the website.
Limited Scalability:

The infrastructure may struggle to handle a large influx of traffic, as the single server may become overwhelmed. Scaling horizontally by adding more servers is challenging due to the tightly coupled nature of the components on a single server.
