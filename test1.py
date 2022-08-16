from cProfile import label
import librosa
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import librosa.display

def showFigure(val):
    clicked
    
def clicked():
    plt.title('nutcracker waveform')
    filename = librosa.example('nutcracker')
    y, sr = librosa.load(filename)
    librosa.display.waveshow(y, sr=sr)
    plt


#Button
BShowFigure = Button(plt.axes([0.7, 0.9, 0.1, 0.075]),
                     label = 'show'
                    )
BShowFigure.on_clicked(showFigure)
plt.show()


