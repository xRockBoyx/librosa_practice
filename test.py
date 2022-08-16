import librosa
import matplotlib.pyplot as plt
import librosa.display
import tkinter


# 產圖視窗
def rosaView():
    filename = librosa.example('nutcracker')

    y, sr = librosa.load(filename)
    plt.figure()
    librosa.display.waveshow(y, sr=sr)
    plt.title('nutcracker waveform')
    plt.show()

# UI測試
root = tkinter.Tk()
root.configure(bg = '#BA8811')
root.title('LibrosaTest')
root.geometry('500x500')

Button = tkinter.Button(root,
                        text = 'Normal Button',
                        relief = "ridge",
                        activebackground = '#BE77FF',#設定滑鼠位於按鈕時的背景顏色
                        activeforeground = '#FFFFFF',#設定滑鼠位於按鈕時的前景顏色
                        state=tkinter.NORMAL,        #設定按鈕的狀態
                        command = rosaView
                        )
# Canvas = tkinter.Canvas(root, 
#                         width = 100, 
#                         height = 100,
#                         bg = '#DCB5FF'
#                         )

# Canvas.pack()
Button.pack()
root.mainloop()

