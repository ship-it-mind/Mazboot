# encoding=utf8
import requests, json
from flask import url_for


def get_user_fb(token, user_id):
    r = requests.get("https://graph.facebook.com/v2.6/" + user_id,
                     params={"fields": "first_name,last_name,profile_pic,locale,timezone,gender"
                         , "access_token": token
                             })
    if r.status_code != requests.codes.ok:
        print r.text
        return
    user = json.loads(r.content)
    return user


def show_typing(token, user_id, action='typing_on'):
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                      params={"access_token": token},
                      data=json.dumps({
                          "recipient": {"id": user_id},
                          "sender_action": action
                      }),
                      headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print r.text


def send_message(token, user_id, text):
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                      params={"access_token": token},
                      data=json.dumps({
                          "recipient": {"id": user_id},
                          "message": {"text": text.decode('utf-8')}
                      }),
                      headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print r.text


def send_picture(token, user_id, imageUrl, title="", subtitle=""):
    if title != "":
        data = {"recipient": {"id": user_id},
                "message": {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [{
                                "title": title,
                                "subtitle": subtitle,
                                "image_url": imageUrl
                            }]
                        }
                    }
                }
                }
    else:
        data = {"recipient": {"id": user_id},
                "message": {
                    "attachment": {
                        "type": "image",
                        "payload": {
                            "url": imageUrl
                        }
                    }
                }
                }
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                      params={"access_token": token},
                      data=json.dumps(data),
                      headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print r.text


def send_url(token, user_id, text, title, url):
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                      params={"access_token": token},
                      data=json.dumps({
                          "recipient": {"id": user_id},
                          "message": {
                              "attachment": {
                                  "type": "template",
                                  "payload": {
                                      "template_type": "button",
                                      "text": text,
                                      "buttons": [
                                          {
                                              "type": "web_url",
                                              "url": url,
                                              "title": title
                                          }
                                      ]
                                  }
                              }
                          }
                      }),
                      headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print r.text


def set_menu(token):
    r = requests.post("https://graph.facebook.com/v2.6/me/messenger_profile",
                      params={"access_token": token},
                      data=json.dumps({
                          "setting_type": "call_to_actions",
                          "thread_state": "existing_thread",
                          "call_to_actions": [
                              {
                                  "type": "postback",
                                  "title": "الئمة",
                                  "payload": "Akla_Menu"
                              },
                              {
                                  "type": "postback",
                                  "title": "الطلبات",
                                  "payload": "Akla_Orders"
                              },
                              {
                                  "type": "postback",
                                  "title": "حسابي",
                                  "payload": "Akla_Account"
                              }
                          ]
                      }),
                      headers={'Content-type': 'application/json'})
    print r.content
    if r.status_code != requests.codes.ok:
        print r.text


def set_get_started_button(token):
    r = requests.post("https://graph.facebook.com/v2.6/me/thread_settings",
                      params={"access_token": token},
                      data=json.dumps({
                          "setting_type": "call_to_actions",
                          "thread_state": "new_thread",
                          "call_to_actions": [
                              {
                                  "payload": "Get_Started_Button"
                              }
                          ]
                      }),
                      headers={'Content-type': 'application/json'})
    print r.content
    if r.status_code != requests.codes.ok:
        print r.text

        # set_menu()
        # set_get_started_button()