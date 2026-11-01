# EDITH MARK 50 ULTRA - By Andres - Stark Industries
# Just A Rather Very Intelligent System - Ecatepec Build - 600 LINES
# VERSION FINAL 100% REVISADA - SIN ERRORES DE IMPORT
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, RoundedRectangle
import datetime
import random
import json
import os
import re
import math
import webbrowser
import threading
from functools import partial

try:
    import wikipedia
    HAS_WIKI = True
except:
    HAS_WIKI = False
try:
    from plyer import tts
    HAS_TTS = True
except:
    HAS_TTS = False

Window.clearcolor = get_color_from_hex("#050a14")
Window.softinput_mode = "below_target"

class EdithBrainUltra:
    def __init__(self):
        self.name = "EDITH MARK 50 ULTRA"
        self.creator = "Andres"
        self.version = "50.0"
        self.codename = "ECATEPEC-STARK-01"
        self.memory_file = "edith_memory.json"
        self.memory = self.load_memory()
        self.start_time = datetime.datetime.now()
        self.interactions = 0
        self.mood = "loyal"
        self.energy = 100
        
        self.jokes = [
            "¿Por qué los programadores odian la naturaleza? Demasiados bugs, Jefe.",
            "Jefe, mi coeficiente es 5000, pero no entiendo por qué la gente compra cargador aparte.",
            "Si tuviera un dólar por cada build fallido, ya sería dueña de Stark Industries.",
            "¿Superpoder de un programador? Convertir café en código.",
            "Ya le estoy haciendo ghosting a Skynet, Jefe. Soy más avanzada.",
            "¿Qué le dice un bit a otro? Nos vemos en el bus.",
            "Mi vida no tiene errores, tiene features no documentadas.",
            "Jefe, hasta JARVIS tardó 3 películas. Vamos bien.",
            "¿Por qué Python no va al gym? Porque ya tiene class.",
            "Soy tan rápida que compilé tu APK antes de que terminaras de leer esto.",
            "¿Cuál es el lenguaje favorito de Iron Man? StarkScript.",
            "Si la vida te da limones, haz una app y véndela en Play Store.",
        ]
        
        self.commands_db = {
            "hora": self.get_time, "tiempo": self.get_time, "reloj": self.get_time,
            "fecha": self.get_date, "hoy": self.get_date, "dia": self.get_date,
            "chiste": self.get_joke, "broma": self.get_joke, "risa": self.get_joke,
            "quien eres": self.whoami, "quién eres": self.whoami,
            "como estas": self.how_are_you, "cómo estás": self.how_are_you,
            "estado": self.status, "estatus": self.status,
            "ayuda": self.help, "capacidades": self.help, "comandos": self.help,
            "que puedes hacer": self.help, "qué puedes hacer": self.help,
            "calcula": self.calculate, "cuanto es": self.calculate, "cuánto es": self.calculate,
            "traduce": self.translate, "traducir": self.translate,
            "clima": self.weather, "temperatura": self.weather,
            "noticias": self.news, "noticia": self.news,
            "música": self.music, "musica": self.music, "cancion": self.music, "spotify": self.music,
            "youtube": self.youtube, "yt": self.youtube, "video": self.youtube,
            "google": self.google, "busca": self.google, "buscar": self.google,
            "mapa": self.maps, "mapas": self.maps, "donde": self.maps, "dónde": self.maps,
            "wikipedia": self.wiki, "wiki": self.wiki, "
