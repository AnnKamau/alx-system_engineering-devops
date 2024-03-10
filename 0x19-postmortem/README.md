Duration: 
The outage lasted from 10:00 PM to 11:45 PM in January 2024. Impact: The service downtime affected 30% of our users, resulting in complete unavailability of the web application and API endpoints. Users experienced errors while trying to access the platform. Root Cause: The outage was identified as a misconfiguration in the load balancer settings.

TIMELINE: 
10:00 PM: Issue detected through monitoring alerts a sudden increase in HTTP 500 errors. 

10:05 PM: The Engineering team was alerted and began investigation into the cause of the errors.

10:20 PM: Initial assumptions were made that the database servers were experiencing issues due to high traffic load. Investigation focused on database performance metrics. 

10:45 PM: Database servers were found to be functioning normally. Attention shifted to the load balancer configuration. 

11:20 PM: Load balancer misconfiguration identified as root cause. 
11:30 PM: Incident escalated even further to the senior engineering management for awareness and additional support. 
11:45 PM: Load balancer configuration corrected, services restored, and users regained access to the platform.
ROOT CAUSE AND RESOLUTION: 
Root Cause:
 Misconfiguration in the load balancer settings led to incorrect routing of incoming requests, causing a portion of the traffic to be directed to non-responsive backend servers. This was identified as the root cause. 
Resolution: 
The misconfiguration settings in the load balancer were corrected, ensuring proper routing of incoming requests to healthy backend servers. Additionally, automated checks were implemented to prevent similar misconfigurations in the future.
CORRECTIVE AND PREVENTIVE MEASURES: 
IMPROVEMENTS/FIXES: 
Implement stricter configuration management processes to prevent inadvertent changes to critical infrastructure components. Enhance monitoring and alerting systems to provide granular visibility into the load balancer behavior and configuration changes. Conduct regular audits or infrastructure configurations to proactively identify and address potential misconfigurations.
TASKS TO ADDRESS THE ISSUES: 
Conduct thorough review of the load balancer configurations to identify additional misconfigurations. Implement automated configuration validations checks for critical infrastructure components. Schedule regular training sessions for engineering teams to reinforce best practices for infrastructure management and configuration.


Impelementing these corrective measures and addressing the identified tasks, we aim to minimize the risk of similar outages in the future and ensures the continued reliability and availability of our services for our users.

