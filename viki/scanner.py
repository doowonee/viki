import logging
from pathlib import Path
import subprocess as pcs

from .video import Video
from .conf import MEDIAINFO_PATH

logger = logging.getLogger(__name__)


def scan_video_file(file_path):
    """Mediainfo를 사용하여 비디오 파일을 파싱 한다.
    
    Args:
        file_path: 비디오 파일 절대 경로 이다.

    Returns:
        Video 인스턴스를 리턴 한다.

    Raises:
        FileNotFoundError: 스캔할 파일이 존재 하지 않으면 발생 한다.
        CalledProcessError: 서브프로세스로 Mediainfo 프로그램 실행이 실패 하면 발생 한다.
    """
    path_obj = Path(file_path)
    if path_obj.exists() is False:
        raise FileNotFoundError(f"{file_path} does not exist.")
    cmd = [MEDIAINFO_PATH, file_path, '--Output=JSON']
    completed = pcs.run(cmd, capture_output=True)
    completed.check_returncode()
    result = completed.stdout.decode('utf-8')

    # Todo: json 파싱 구현 ㄱ
    print("그냥 출력", result)

    return Video(path_obj)
