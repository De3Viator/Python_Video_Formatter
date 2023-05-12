import cv2

def change_color_scheme(video_path):
    # Відкриття відео файлу
    video_capture = cv2.VideoCapture(video_path)

    while True:
        # Зчитування кадру з відео
        ret, frame = video_capture.read()

        if not ret:
            # Кінець відео
            break

        # Зміна кольорової схеми на відтінки сірого
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Відображення зміненого кадру
        cv2.imshow('Gray Video', gray_frame)

        # Відстеження натискання клавіші 'q' для виходу з програми
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Закриття відео захоплення та вікна відображення
    video_capture.release()
    cv2.destroyAllWindows()

# Виклик функції з вказанням шляху до відео файлу
change_color_scheme('D:\\video.mp4')