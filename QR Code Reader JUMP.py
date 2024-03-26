import cv2
import datetime
import numpy as np

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
hoje = datetime.date.today()

hoje_format = hoje.strftime('%d/%m/%Y')
lastData =" "

with open("Presença_JUMP.txt", "a") as f:
    f.write(hoje_format + '\n')
    while True:
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)

        if data:
            bbox = np.ravel(bbox)  # Achatando a matriz bbox em 1D
            x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2] - bbox[0]), int(bbox[3] - bbox[1])  # Calculando largura e altura
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 2)  # Desenha retângulo ao redor do código QR
            cv2.putText(img, data, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # Mostra dados do QR
            cv2.putText(img, "Bem vindo: "+ data, (50,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # Mostra dados do QR

            if data != lastData:
                f.write(data + '\n')

            lastData = data

        else:
            cv2.putText(img, "Mostre sua ID", (50,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  # Mostra dados do QR

   
        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()