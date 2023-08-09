# Webstack Monitoring - Project Tasks

This directory contains solutions and files for the Webstack Monitoring project tasks. Each task focuses on setting up monitoring and visualization of various metrics using Datadog.

## Task 0: Sign up for Datadog and install datadog-agent

**Task Description:** For this task, head to [Datadog](https://www.datadoghq.com/) and sign up for a free Datadog account. Select statistics from your current stack that Datadog can monitor. Once your account is set up, follow the instructions on the website to install the Datadog agent.

**Instructions:**
- Sign up for Datadog using the US website: [https://app.datadoghq.com](https://app.datadoghq.com)
- Use the US1 region
- Install datadog-agent on web-01
- Create an application key
- Copy-paste your Datadog API key and application key in your Intranet user profile
- Your server web-01 should be visible in Datadog under the host name XX-web-01
- Validate by using the provided API
- Update the hostname of your server if necessary

**Repository Information:**
- GitHub repository: [alx-system_engineering-devops](./https://github.com/gebretewodros73/alx-system_engineering-devops)
- Directory: 0x18-webstack_monitoring

## Task 1: Monitor some metrics

**Task Description:** Set up monitors within the Datadog dashboard to monitor and alert you about the number of read and write requests issued to the device per second.

**Instructions:**
- Set up a monitor that checks the number of read requests issued per second
- Set up a monitor that checks the number of write requests issued per second

**Repository Information:**
- GitHub repository: [alx-system_engineering-devops](./https://github.com/gebretewodros73/alx-system_engineering-devops)
- Directory: 0x18-webstack_monitoring

## Task 2: Create a dashboard

**Task Description:** Create a new dashboard with different metrics displayed to get various visualizations.

**Instructions:**
- Create a new dashboard
- Add at least 4 widgets to your dashboard of any type to monitor different metrics
- Create an answer file `2-setup_datadog` with the dashboard_id on the first line (use Datadog’s API to get the id)

**Repository Information:**
- GitHub repository: [alx-system_engineering-devops](./https://github.com/gebretewodros73/alx-system_engineering-devops)
- Directory: 0x18-webstack_monitoring
- File: [2-setup_datadog](./2-setup_datadog)
