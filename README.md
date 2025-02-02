# Youtube Video Downloder

## 環境

- [Python 3.13.1](https://www.python.org/ftp/python/3.13.1/python-3.13.1-amd64.exe)
- [yt-dlp](https://pypi.org/project/yt-dlp/)
- [Django](https://pypi.org/project/Django/)

## インストール

```bash
git clone https://github.com/Hakuprogramming/youtubedl.git
cd youtubedl
```

### 仮想環境

#### windows

```bash
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

#### Mac\Linux

```bash
python3 -m venv
source ./.venv/bin/active
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

## [webページ](http://127.0.0.1:8000)
