"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - class dokkaebi_RuleBasedChatBot_Handover
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
"""

import pandas as pd
from ChatBotData import *
from konlpy.tag import Hannanum

class dokkaebi_ChatBot_Handover:
    def __init__(self, data, hannanum):
        self.hannanum = hannanum
        self.dokkaebi_data = data
        self.chatbot_data = pd.read_excel("chatbot_data_handover.xlsx")
        self.chat_dic = {}
        self.initChatBot()
        self.step = 1

    def initChatBot(self):
        # rule의 데이터를 split하여 list형태로 변환 후, index값과 함께 dictionary 형태로 저장
        row = 0
        for rule in self.chatbot_data['rule']:
            self.chat_dic[row] = rule.split('|')
            row += 1

    def chat(self, request):
        for k, v in self.chat_dic.items():
            index = -1
            for word in v:
                try:
                    if index == -1:
                        index = request.index(word)
                    else:
                        # 이전 index 값은 현재 index값보다 이전이어야 한다.
                        if index < request.index(word, index):
                            index = request.index(word, index)
                        else:  # index 값이 이상할 경우 과감하게 break를 한다
                            index = -1
                            break
                except ValueError:
                    index = -1
                    break
            if index > -1:
                if self.chatbot_data['type'][k] == "classification":
                    self.dokkaebi_data.classification = self.chatbot_data['data'][k]
                elif self.chatbot_data['type'][k] == "time":

                return self.chatbot_data['response'][k]
        return '무슨 말인지 모르겠어요'

    def runChatBot(self):
        print("Seoul, my soul. 안녕하세요? 한강 도깨비 박스입니다.")
        if self.step == 1:
            print("어떤 물건을 맡기러 오셨나요?(스마트폰/지갑/기타)")
            while True:
                userResponse = input('입력 : ')
                chatBotResponse = self.chat(userResponse)
                print('도깨비박스 : ', chatBotResponse)
        elif self.step == 2:
            print("물건을 언제 주우셨나요?")
            while True:
                userResponse = input('입력 : ')
                chatBotResponse = self.chat(userResponse)
                print('도깨비박스 : ', chatBotResponse)
        elif self.step == 3:
            print("물건을 어디에서 주우셨나요?")
            while True:
                userResponse = input('입력 : ')
                chatBotResponse = self.chat(userResponse)
                print('도깨비박스 : ', chatBotResponse)
        elif self.step == 4:
            print("감사합니다. 도깨비 박스가 물건을 잘 보관할게요.")
            print("마음이 모이면 서울이 됩니다. Seoul, my soul")



if __name__ == "__main__":
    DokkaebiChatBot_Data=Dokkaebi_Data()
    hannanum = Hannanum()
    chatBot = dokkaebi_ChatBot(DokkaebiChatBot_Data, hannanum)
    chatBot.runChatBot()