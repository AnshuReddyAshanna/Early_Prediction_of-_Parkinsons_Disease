import warnings
warnings.filterwarnings('ignore')
from tkinter import messagebox
import tensorflow as tf

classifierLoad = tf.keras.models.load_model('diabetic.h5')

import numpy as np
from keras.preprocessing import image

test_image = image.load_img('./Output/Out/Test.jpg', target_size=(200, 200))
# test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifierLoad.predict(test_image)

out = ''
if result[0][0] == 1:
    print("DR1")
    out = "DR1"

    messagebox.showinfo("Result", 'Type 1 Diabetes')
    messagebox.showinfo("prescription", 'Short-acting (regular) insulin')


elif result[0][1] == 1:
    print("DR2")
    out = "DR2"
    messagebox.showinfo("Result", 'Type 2 Diabetes')
    messagebox.showinfo("prescription", 'Possibly, diabetes medication or insulin therapy')

elif result[0][2] == 1:
    print("Normal")
    out = "Normal"
    messagebox.showinfo("Result", "Classification Result : " + str(out))