import numpy as np #numpy ライブラリをnpという名前で導入
import cv2 #OpenCV ライブラリを導入
img = np.zeros((500,500,3), np.uint8) #img 変数を 500*500*3 の大きさにし, 0で初期化
img = cv2.rectangle(img,(1,1),(100,100),(0,255,0),3)
cv2.imshow('imgame',img) #画面表示
cv2.waitKey(0) #キーボード入力を待つ
cv2.destroyAllWindows() #すべての画面を閉じる
