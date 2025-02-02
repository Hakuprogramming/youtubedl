import yt_dlp
import os
from django.conf import settings
from django.shortcuts import render, redirect

def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link')  # リンクを安全に取得
        if not link:
            return render(request, 'hello/youtube.html', {'error': 'リンクが提供されていません。'})  # エラー処理

        print(f"リンク: {link}")
        
        # yt-dlp で動画をダウンロード
        ydl_opts = {
            
            # 'cookiesfrombrowser': ('chrome', 'default', None, 'Meta'),
            'outtmpl': os.path.join(settings.MEDIA_ROOT, 'videos', '%(id)s.%(ext)s'), # 動画IDをファイル名に使用
            'noplaylist': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)
                video_id = info_dict.get('id')  # 動画IDを取得
                video_file_path = os.path.join(settings.MEDIA_ROOT, 'videos', f"{video_id}.mp4")
                print(f"ダウンロード完了: {video_file_path}")
        except Exception as e:
            return render(request, 'hello/youtube.html', {'error': f"動画ダウンロード中にエラーが発生しました: {str(e)}"})

        # ダウンロード完了後、send_video ビューにリダイレクト
        return redirect('send_video', video_id=video_id)

    return render(request, 'hello/youtube.html')
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os

def send_video(request, video_id):
    # 動画ファイルのパスを設定 (video_id に基づいてファイル名を決定)
    video_file_path = os.path.join(settings.MEDIA_ROOT, 'videos', f"{video_id}.mp4")

    # ファイルが存在しない場合
   

    # ファイルが存在する場合
    try:
        with open(video_file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename="{video_id}.mp4"'
        return response
    except FileNotFoundError:
        return HttpResponse(f"ファイルが見つかりません: {video_file_path}", status=404)
    except PermissionError:
        return HttpResponse(f"ファイルへのアクセス権限がありません: {video_file_path}", status=403)
    except Exception as e:
        return HttpResponse(f"ファイルを開く際にエラーが発生しました: {str(e)}", status=500)
