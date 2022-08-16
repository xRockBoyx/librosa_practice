
# 初始設定

## 安裝virtualenv
```
pip3 install virtualenv
```
## 建立虛擬pip環境
```
python3 -m venv .venv
```

## 進入虛擬環境並且安裝套件
```source .venv/bin/activate```
```pip install librosa``` 

## 離開虛擬環境
```
deactivate
```

# 安裝過程問題
---
1. **librosa**相依套件**numpy**版本不相容: <br>
   *raise ImportError("Numba needs NumPy 1.22 or less")*
    ```
    pip uninstall numba \
    pip uninstall numpy \
    pip install numba
    ```
---

# 套件列表
- librosa
- matplotlib(圖表)