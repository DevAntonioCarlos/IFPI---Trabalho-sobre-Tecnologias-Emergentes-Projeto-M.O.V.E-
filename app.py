import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from utils.gesture_utils import detectar_gesto

st.title("🖐️ Projeto M.O.V.E - Controle por Gestos")

run = st.checkbox('Iniciar câmera')

frame_placeholder = st.empty()
gesture_text = st.empty()

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = None
if run:
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
        while run:
            ret, frame = cap.read()
            if not ret:
                st.error("Erro ao acessar a câmera")
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            gesture = "Nenhuma mão detectada"
            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    h, w, _ = frame.shape
                    pontos = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
                    gesture = detectar_gesto(pontos)

            gesture_text.markdown(f"**Gesto detectado:** {gesture}")
            frame_placeholder.image(frame, channels='BGR')

    cap.release()

