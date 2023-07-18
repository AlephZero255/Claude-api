#ONLY USA IP!!!!
import requests
import json
from uuid import uuid4
import pymailtm
import time

class Claude:
    def initialize(self):
        rand_mail = pymailtm.pymailtm.MailTm()
        self.email = rand_mail.get_account()
        self.client = requests.Session()
        #self.client.proxies = {
        #    'http': "",
        #    'https': ""
        #}


        self.client.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "*/*",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Content-Type": "application/json",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        }

        self.send_email()
        self.sessionKey = self.send_code()
        self.organization_uuid = self.get_organization()
        self.chat_uuid = self.create_chat(self.organization_uuid, self.sessionKey, "snusik")["uuid"]

    def send_email(self):
        url = "https://claude.ai/api/auth/send_code"
        data = {
            "email_address": self.email.address,
            "recaptcha_token": "03AAYGu2Sl7Laa23eQjMJwt4mBAuXaXZ993pU7Jmknyw1RVGXWw54HxdmZac8Vmq-ZiyV9oUzEyWf1xscZTX78he4-Ubwx0RpE003nep8LxgQwR0dvG8VUWTWwk4eI8NULe1q00xCHjWrRT2mKt7dD_AK8nopXIMuLfZqrg6KrbUfQgl3f9xIQahS2eqS7QD0IjQ_bJbSvKW5SlDkBWx_Ezv5X1I-yquJdBXTsJ1FNWs-uJ65X4SUHNBANvv7GekvcwcKWNJLIHh_m6x-I9XGn39Dr4IkT0PF75KJwSu_ke_Jkn2P-PXx8jirxqMyE6FfGM24mx9FuPPMGwdoSkvDup6I-5lM6DsXLt_9wIATrWqvk5PIy5Hmut-6a4V0Tv4j1O2VAkNLFa_U17_2baU8gNJ8__VFKc-EedNJ3Vo2CcxMc5NS85qsJ5Tq_vH5ILNnalOkDpveZqcvBk2A3OOt0ctRoyS3XTZZN7vPnHbtUUuuhUYLckcYj9r2bXETPMM2_F63UyiM5gzqInZnt2DicaNInY5Z8lcX9CdHdriKY3hBvWz42EFC5PT5Qp0jMy-JVdneb9gJYwSNtKhXfO4sZ0gDtqAeTRj_bBfs8L1D2hG4VStfDoSs6cy8JAEk1v20uQ-IXn8OHNI2fNI2n8tMs5FTs6RxioaTKI5KVW5bLF44Eo_ebJdm6p3BNdmjTgUWho0l9trlok5sFQjA1_txv9c43XsQ9zoOAmsCmNXXRtNjnGbL1tsdBZWWxp1WXGT_Wq6EmdHCZzonaqd3rn4QJcqUia7CJmjBdiuvDhZub-mkpDSQoYe4vHFv6flsI3oteV4dktasGCOybnrHDIAoy_YZE5HPp46lRHuo_eL4FDWPPPu3Z6EIsGFUPsdxjN4Tg3cz__Q7DaTdE_aqdI8aeZ8tnz38L3r5jAS3h8FHisukHAvE56bVolDThjMeC1A_Ci0wtG2WcrNHf6ztfMhg3ClQbkesWmcxiC7hS5zxEakv29vR9kKOYkBIZw3c8O9qnxd3slg-zircAX0mn_bkq4yhrhPUq7PeznqMBOdDHuRf53BMjP7OoZd4K6LiPndjyzhUXxwAZbrrSXpC78-W1SGUzPoqBO2wVtbAUh0lPe-blbxdgEoFaPfRbhYup9gVwJOUEYzAy-8pju7qG8hh_nHANcnkEgcWvkH9_xMYIFjGgRywNIho2PFal7KkfbQ1hL_JJM2BDTaxXXJk0HU03kebwWc2w4rxh_0j8Ks5yDfhJjwwqNbmQwD0Yos9O2i05gfV3etqEsMo2dSNW3qzJjMp4Y0BKGgpbsizym77i42EQbLzeAw4YETqxFom2x1FWYVe7KCZ-bclKDmcS-MmRhwb7cGPLooWmkOyD6Mh45ycyqxOaple2MjUfT--5WbnDyWdduOx7YC-y-6zkLQfpa9NDdDBXuxHQSa4GdFoID3FO-LVEWN8gIP9vWW_fJscjVcOBZstspF0Z_r7N0SDmGVVKVqG5qxqU7J2gFvtD-Rjhwfb9v0W75zZxZ9e3md8sNelhdT00iYghDXuTA5HlNF7O6whlovzo7LeKjbrSBovQHREVgAVcWaTPoMbqRyGV_mBKD9lrcPk7g34UeREFzKnVw9oCDAS-NA",
            "recaptcha_site_key": "6LcdsFgmAAAAAMfrnC1hEdmeRQRXCjpy8qT_kvfy"
        }

        response = self.client.post(url, data=json.dumps(data))
        return response
    def send_code(self):
        self.code = 0
        while 1:
            time.sleep(1)
            msgs = []
            try:
                msgs = self.email.get_messages()
            except:
                print("ERROR")
            if msgs != []:
                self.code = msgs[0].subject[-6:]
                print(self.code)
                break

        url = "https://claude.ai/api/auth/verify_code"
        
        body = {
            "email_address": self.email.address,
            "code": self.code,
            "recaptcha_token": "03AAYGu2Sl7Laa23eQjMJwt4mBAuXaXZ993pU7Jmknyw1RVGXWw54HxdmZac8Vmq-ZiyV9oUzEyWf1xscZTX78he4-Ubwx0RpE003nep8LxgQwR0dvG8VUWTWwk4eI8NULe1q00xCHjWrRT2mKt7dD_AK8nopXIMuLfZqrg6KrbUfQgl3f9xIQahS2eqS7QD0IjQ_bJbSvKW5SlDkBWx_Ezv5X1I-yquJdBXTsJ1FNWs-uJ65X4SUHNBANvv7GekvcwcKWNJLIHh_m6x-I9XGn39Dr4IkT0PF75KJwSu_ke_Jkn2P-PXx8jirxqMyE6FfGM24mx9FuPPMGwdoSkvDup6I-5lM6DsXLt_9wIATrWqvk5PIy5Hmut-6a4V0Tv4j1O2VAkNLFa_U17_2baU8gNJ8__VFKc-EedNJ3Vo2CcxMc5NS85qsJ5Tq_vH5ILNnalOkDpveZqcvBk2A3OOt0ctRoyS3XTZZN7vPnHbtUUuuhUYLckcYj9r2bXETPMM2_F63UyiM5gzqInZnt2DicaNInY5Z8lcX9CdHdriKY3hBvWz42EFC5PT5Qp0jMy-JVdneb9gJYwSNtKhXfO4sZ0gDtqAeTRj_bBfs8L1D2hG4VStfDoSs6cy8JAEk1v20uQ-IXn8OHNI2fNI2n8tMs5FTs6RxioaTKI5KVW5bLF44Eo_ebJdm6p3BNdmjTgUWho0l9trlok5sFQjA1_txv9c43XsQ9zoOAmsCmNXXRtNjnGbL1tsdBZWWxp1WXGT_Wq6EmdHCZzonaqd3rn4QJcqUia7CJmjBdiuvDhZub-mkpDSQoYe4vHFv6flsI3oteV4dktasGCOybnrHDIAoy_YZE5HPp46lRHuo_eL4FDWPPPu3Z6EIsGFUPsdxjN4Tg3cz__Q7DaTdE_aqdI8aeZ8tnz38L3r5jAS3h8FHisukHAvE56bVolDThjMeC1A_Ci0wtG2WcrNHf6ztfMhg3ClQbkesWmcxiC7hS5zxEakv29vR9kKOYkBIZw3c8O9qnxd3slg-zircAX0mn_bkq4yhrhPUq7PeznqMBOdDHuRf53BMjP7OoZd4K6LiPndjyzhUXxwAZbrrSXpC78-W1SGUzPoqBO2wVtbAUh0lPe-blbxdgEoFaPfRbhYup9gVwJOUEYzAy-8pju7qG8hh_nHANcnkEgcWvkH9_xMYIFjGgRywNIho2PFal7KkfbQ1hL_JJM2BDTaxXXJk0HU03kebwWc2w4rxh_0j8Ks5yDfhJjwwqNbmQwD0Yos9O2i05gfV3etqEsMo2dSNW3qzJjMp4Y0BKGgpbsizym77i42EQbLzeAw4YETqxFom2x1FWYVe7KCZ-bclKDmcS-MmRhwb7cGPLooWmkOyD6Mh45ycyqxOaple2MjUfT--5WbnDyWdduOx7YC-y-6zkLQfpa9NDdDBXuxHQSa4GdFoID3FO-LVEWN8gIP9vWW_fJscjVcOBZstspF0Z_r7N0SDmGVVKVqG5qxqU7J2gFvtD-Rjhwfb9v0W75zZxZ9e3md8sNelhdT00iYghDXuTA5HlNF7O6whlovzo7LeKjbrSBovQHREVgAVcWaTPoMbqRyGV_mBKD9lrcPk7g34UeREFzKnVw9oCDAS-NA",
            "recaptcha_site_key": "6LcdsFgmAAAAAMfrnC1hEdmeRQRXCjpy8qT_kvfy",
        }
        
        response = self.client.post(url, data=json.dumps(body))
        return response.cookies["sessionKey"]
    def get_organization(self):
        url = "https://claude.ai/api/auth/current_account"
        response = self.client.get(url).json()
        return response["account"]["memberships"][0]["organization"]["uuid"]
    def create_chat(self, org_uuid, sess_key, name):
        url = f'https://claude.ai/api/organizations/{org_uuid}/chat_conversations'
        headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
          'Accept': '*/*', 
          'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
          'Content-Type': 'application/json',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-origin'
        }
        
        data = {
          'uuid': str(uuid4()),
          'name': name
        }
        cookies = {"sessionKey": sess_key}
        response = requests.post(url, headers=headers, json=data, cookies=cookies)
        return response.json()
    def get_messages(self):
        url = f"https://claude.ai/api/organizations/{self.organization_uuid}/chat_conversations/{self.chat_uuid}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "*/*",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Content-Type": "application/json",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        }
        cookies = {"sessionKey": self.sessionKey}
    
        response = requests.get(url, headers=headers, cookies=cookies)
        return response.json()

    def append_message(self, message):
        url = "https://claude.ai/api/append_message"
        data = {
            "completion": {
                "prompt": message,
                "timezone": "Europe/Moscow",
                "model": "claude-2",
                "incremental": True
            },
            "organization_uuid": self.organization_uuid,
            "conversation_uuid": self.chat_uuid,
            "text": message,
            "attachments": []
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "text/event-stream, text/event-stream",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Content-Type": "application/json",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        }
        cookies = {"sessionKey": self.sessionKey}
    
        response = requests.post(url, data=json.dumps(data), headers=headers, cookies=cookies)
        return response

if __name__ == "__main__":
    text = "Hello"
    cl = Claude()
    cl.initialize()
    
    cl.append_message(text)
    txt = cl.get_messages()["chat_messages"]
    for i in txt:
        print(i["text"].encode('latin-1').decode('utf-8'))
    
    print(cl.organization_uuid)
    print(cl.chat_uuid)
    print(cl.sessionKey)    