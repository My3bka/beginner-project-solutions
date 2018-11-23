#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import kivy
kivy.require(kivy.__version__)
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
import random

class EightLayout(FloatLayout):

    def __init__(self, **kwargs):
        super(EightLayout, self).__init__(**kwargs)
        #define triger for progress bar
        #https://stackoverflow.com/q/52186990/7051733
        self.update_bar_trigger = Clock.create_trigger(self.update_bar)
        self.play = True
        #put answers.txt in list self.answers
        with open('answers.txt', 'r') as f:
            self.answers = [line.strip() for line in f]

    #func for clearing input window work while we dont have answer
    def clear(self):
        if self.play:
            self.ids.txtin.text = ''
        
    #button exit anction
    def close(self):
        App.get_running_app().stop()
        
    #making progress bar update and set text answer when doit
    def update_bar(self, dt):
        if self.i <= 100:
            self.ids.pbar.value = self.i
            self.i += 1
            self.update_bar_trigger()
            if self.i == 100:
                print(str(self.i))
                self.ids.lanswer.text = self.choose()
    
    #func on button ask
    def giveanswer(self):
        if len(self.ids.txtin.text) > 2 and self.play:
            self.play = False
            self.i = 0
            self.update_bar_trigger()
        elif len(self.ids.txtin.text) <= 2:
            self.ids.lanswer.text = 'short answer'
            
    def playagain(self):
        if not self.play:
            self.ids.txtin.text = ''
            self.ids.lanswer.text = ''
            self.play = True
            self.ids.pbar.value = 0
        
    def choose(self):
        return random.sample(self.answers, 1)[0]

class EightLayoutApp(App):
    def build(self):
        return EightLayout()

if __name__ == '__main__':
    EightLayoutApp().run()