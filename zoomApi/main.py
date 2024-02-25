import json
import pprint

real_data = {
  "topic": "string",
  "type": 2,
  "start_time": "2019-12-11T10:35:01",
  "duration": 60,
  "schedule_for": "",
  "timezone": "Asia/Shanghai",
  "password": "",
  "agenda": "string",
  "settings": {
    "host_video": True,
    "participant_video": False,
    "cn_meeting": False,
    "in_meeting": False,
    "join_before_host": True,
    "mute_upon_entry": True,
    "watermark": False,
    "use_pmi": False,
    "approval_type": 2,
    "registration_type": 1,
    "audio": "both",
    "auto_recording": "none",
    "enforce_login": False,
    "enforce_login_domains": "",
    "alternative_hosts": "",
    "global_dial_in_countries": None,
    "registrants_email_notification": False
  }
}



json_data = json.dumps(real_data, indent=2)
