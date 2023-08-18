# Application Server Tasks

This directory contains solutions to tasks related to setting up and configuring an application server for different projects.

## Task 0: Set up Development with Python

**Objective:** Serve the AirBnB clone v2 - Web framework on web-01. Set up the development environment for testing and debugging before deploying to production.

Requirements:
- Install the net-tools package: `sudo apt install -y net-tools`
- Git clone AirBnB_clone_v2 on web-01.
- Configure `web_flask/0-hello_route.py` to serve content from `/airbnb-onepage/` on port 5000.

[Task 0 Solution](./0-the_sky_is_the_limit_not.pp)

## Task 1: Set up Production with Gunicorn

**Objective:** Set up the production application server using Gunicorn on web-01, port 5000. Ensure the Flask application object is named `app`.

[Task 1 Solution](./1-user_limit.pp)

## Task 2: Serve a Page with Nginx

**Objective:** Configure Nginx to serve a page from the route `/airbnb-onepage/`. Nginx should proxy requests to the process listening on port 5000.

[Task 2 Solution](./2-app_server-nginx_config)

## Task 3: Add a Route with Query Parameters

**Objective:** Configure Nginx to proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance on port 5001.

[Task 3 Solution](./3-app_server-nginx_config)

## Task 4: Serve Your API

**Objective:** Set up Nginx to serve the AirBnB clone v3 - RESTful API on web-01.

[Task 4 Solution](./4-app_server-nginx_config)

## Task 5: Serve Your AirBnB Clone

**Objective:** Serve the AirBnB clone - Web dynamic on web-01. Configure Gunicorn to serve content from `web_dynamic/2-hbnb.py` on port 5003.

[Task 5 Solution](./5-app_server-nginx_config)

## Repository Information

- GitHub Repository: [alx-system_engineering-devops](https://github.com/gebretewodros73/alx-system_engineering-devops)
- Directory: 0x1A-application_server

Each task's solution can be found in the corresponding configuration file within the directory.
